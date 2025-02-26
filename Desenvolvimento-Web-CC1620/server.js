const MongoClient = require("mongodb").MongoClient;
const uri = "mongodb+srv://fei-ps:P123456@cluster-web.ztokaoy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster-Web"
const client = new MongoClient(uri, { useNewUrlParser: true });

var http = require('http');
var express = require('express');
var bodyParser = require('body-parser');
const res = require("express/lib/response");

var app = express();
app.use(bodyParser.urlencoded({extended: false}))
app.use(bodyParser.json())
app.set('view engine', 'ejs')
app.set('views','./views');
app.use(express.static('./public'));

var server = http.createServer(app);
server.listen(80);

console.log("Servidor rodando...");

//===FUNÇÕES===//

app.get('/', function (requisicao, resposta){ // Redireciona para a página de projetos
    resposta.redirect('Project.html')
})

app.post("/cadastra", function(req, res){
    newUser = req.body.user;
    newPass = req.body.password;
    enter = "Cadastrado com sucesso!"
    res.render('resposta', {newUser, enter})

})

app.post("/login", function(req, res){
    currentUser = req.body.user;
    currentPass = req.body.password;
    enter = "Falha!";

    if(currentUser == newUser && currentPass == newPass){
        enter = "Sucesso!";
        res.render('resposta', {newUser, enter})
    }else{
        res.render('resposta', {newUser, enter})
    }
})

// CRUD com MongoDB
app.post('/cadastrar_usuario', function(req, res) {
    // Salva os dados no DB
    client.db("Cluster-Web").collection("usuarios").insertOne(
        { 
            db_nome: req.body.nome, // req (function), body (html), nome (form name)
            db_login: req.body.login,
            db_senha: req.body.password 
        }, function (err) {
            if (err) {
                res.render('resposta_usuario', {resposta: "Erro ao cadastrar usuário!"})
            }else {
                res.render('resposta_usuario', {resposta: "Usuário cadastrado com sucesso!"})       
            };
      });   
});

app.post("/logar_usuario", function(req, res) {
    // Busca um usuário no banco de dados
    client.db("Cluster-Web").collection("usuarios").find(
      {db_login: req.body.login, db_senha: req.body.password }).toArray(function(err, items) {
        console.log(items);
        if (items.length == 0) {
          res.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
          res.render('resposta_usuario', {resposta: "Erro ao logar usuário!"})
        }else {
          res.render('resposta_usuario', {resposta: "Usuário logado com sucesso!"})       
        };
      });
 });

 app.post("/atualizar_usuario", function(req, res) {
    // Atualiza um usuário no banco de dados
    client.db("Cluster-Web").collection("usuarios").updateOne(
      {db_login: req.body.login_update, db_senha: req.body.current_password }, {$set: {db_senha: req.body.new_password}},
      function(err, result){
        console.log(result);
        if (result.modifiedCount == 0) {
          res.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
          res.render('resposta_usuario', {resposta: "Erro ao logar usuário!"})
        }else {
          res.render('resposta_usuario', {resposta: "Usuário atualizado com sucesso!"})       
        };
      });
 });

 app.post("/remover_usuario", function(req, resp) {
    // Remove do usuário
    client.db("Cluster-Web").collection("usuarios").deleteOne(
      { db_login: req.body.login_remove, db_senha: req.body.password_remove } , function (err, result) {
        console.log(result);
        if (result.deletedCount == 0) {
          resp.render('resposta_usuario', {resposta: "Usuário/senha não encontrado!"})
        }else if (err) {
          resp.render('resposta_usuario', {resposta: "Erro ao remover usuário!"})
        }else {
          resp.render('resposta_usuario', {resposta: "Usuário removido com sucesso!"})       
        };
      });
 });
 
// ========================

// Funções Att. 9 - Blog
app.get('/blog', function (req, res){ // Redireciona para a página principal
    // Busca todos os posts no banco de dados
    client.db("Cluster-Web").collection("posts").find().toArray(function(err,items) {
        res.render('resposta_blog', { posts: items });
    });
})

app.get('/criacao_post', function(req, res){ // Redireciona para a página de criação de posts
    app.use(express.static('./public/projetos/WebDev-Att.09-(Blog)'))
    res.redirect('criarPost.html')
    app.use(express.static('./public'))
})

app.get('/pagina_projects', function(req, res){ // Redireciona para a página de projetos
    res.redirect('Project.html')
})


app.get('/post_criado', function (req, res){ // Redireciona para a página resposta
    // Salva posts no banco
    if ((req.query.title != "") || (req.query.abstract != "") || (req.query.content != "")){
        client.db("Cluster-Web").collection("posts").insertOne(
        { db_title: req.query.title, db_abs: req.query.abstract, db_cont: req.query.content }, function (err) {
        if (err) {
            res.render('resposta_post', {mensagem: "Erro ao cadastrar post!"})
        }else {
            res.render('resposta_post', {mensagem: "Post cadastrado"})       
        };
        });
    }
    else{
        res.render('resposta_post', {mensagem: "Erro ao cadastrar post!"})
    }
})

// ========================

// Funções Att. 10 - Shop
/* Login para administrador:
User: admin
Password: admin */

app.get('/page_login_shop', function(req, res){ // Redireciona para a página de login
    app.use(express.static('./public/projetos/WebDev-Att.10-(Shop)'))
    res.redirect('loginShop.html')
    app.use(express.static('./public'))
});

app.get('/gerenciar_carros', function(req, res){ // Redireciona para a página de gerencimento de carros
    app.use(express.static('./public/projetos/WebDev-Att.10-(Shop)'))
    res.redirect('gerenciarCarros.html')
    app.use(express.static('./public'))
});

app.post('/cadastrar_usuario_shop', function(req, res){ // Cadastra um novo usuário no DB
    client.db("Cluster-Web").collection("users_shop").insertOne({
        db_full_name: req.body.new_name_shop,
        db_user: req.body.new_login_shop,
        db_password: req.body.new_pass_shop 
    }, function(err){
        if(err){
            res.render('cadastro_shop_resp', {resposta: "Erro ao cadastrar usuário! Por favor, tente novamente!"})
        }else {
            res.render('cadastro_shop_resp', {resposta: "Usuário cadastrado com sucesso!"})
        }
    })
});

var info_user = {};
app.post("/login_shop", function(req, res) { // Busca um usuário no DB e redireciona para a listagem de carros
    client.db("Cluster-Web").collection("users_shop").find(
        {db_user: req.body.user_shop, db_password: req.body.pass_shop }).toArray(function(err, info) {
            info_user = info;
            if (info_user.length == 0) {
                res.render('erro_login_shop', {resposta: "Usuário/senha não encontrado!"})
            }else if (err) {
                res.render('erro_login_shop', {resposta: "Erro ao logar usuário!"})
            }else {
                    admin = 0;
                    if(info_user[0].db_user == 'admin' && info_user[0].db_password == 'admin')
                        admin = 1;
                    client.db("Cluster-Web").collection("cars_shop").find().toArray(function(err, info_car) {
                        res.render('lista_shop', { resposta: "Usuário logado com sucesso!", carros: info_car, user_info: info_user, admin});
                    });
            };
        });
 });
    
app.get('/cadastrar_carro_shop', function(req, res){ // Cadastra um carro no DB
    client.db("Cluster-Web").collection("cars_shop").insertOne({
        db_brand: req.query.new_car_brand,
        db_model: req.query.new_car_model,
        db_year: req.query.new_car_year,
        db_qtt: req.query.new_car_qtt 
    }, function(err){
        if(err){
            res.render('lista_shop', {resposta: "Erro ao cadastrar carro! Por favor, tente novamente!"})
        }else {
            client.db("Cluster-Web").collection("cars_shop").find().toArray(function(err, items) {
                res.render('lista_shop', { resposta: "Carro cadastrado com sucesso!", carros: items, user_info: info_user });
            });
        }
    })
});

app.get("/atualizar_carro_shop", function(req, res) { // Atualiza um carro no banco de dados
    client.db("Cluster-Web").collection("cars_shop").updateOne({
        db_brand: req.query.car_brand,
        db_model: req.query.car_model,
        db_year: req.query.car_year
    }, {$set: {db_brand: req.query.upd_car_brand, db_model: req.query.upd_car_model, db_year: req.query.upd_car_year, db_qtt: req.query.upd_car_qtt}},
      function(err, result){
        if (result.modifiedCount != 0 && !err) {
            client.db("Cluster-Web").collection("cars_shop").find().toArray(function(err, items) {
                res.render('lista_shop', { resposta: "Carro atualizado com sucesso!", carros: items, user_info: info_user });
            });     
        };
      });
 });

app.get("/remover_carro_shop", function(req, res) { // Remove um carro do banco de dados
        client.db("Cluster-Web").collection("cars_shop").deleteOne({
            db_brand: req.query.rem_car_brand,
            db_model: req.query.rem_car_model,
            db_year: req.query.rem_car_year
        } , function (err, result) {
            if (result.deletedCount != 0 && !err) {
                client.db("Cluster-Web").collection("cars_shop").find().toArray(function(err, items) {
                    res.render('lista_shop', { resposta: "Carro removido com sucesso!", carros: items, user_info: info_user });
                });     
            };
        });
});

app.get("/venda_carro", function(req, res) { // Atualiza a quantidade de um carro no banco de dados
    var procura = {
        db_brand: req.query.car_brand,
        db_model: req.query.car_model,
        db_year: req.query.car_year
    };
    client.db("Cluster-Web").collection("cars_shop").findOne(procura, function(err, car) {
        let newQtt = car.db_qtt - 1;
        client.db("Cluster-Web").collection("cars_shop").updateOne(procura, {$set: {db_qtt: newQtt}}, function(err, result){
            if (result.modifiedCount != 0 && !err) {
                client.db("Cluster-Web").collection("cars_shop").find().toArray(function(err, items) {
                    res.render('lista_shop', { resposta: "Carro comprado com sucesso!", carros: items, user_info: info_user });
                });     
            };
        });
      });
 });