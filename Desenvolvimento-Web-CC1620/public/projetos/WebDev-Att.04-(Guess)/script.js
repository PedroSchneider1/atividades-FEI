let y = Math.floor(Math.random()*100);

function guess(){
    let x = parseInt(document.getElementById("num").value);
    console.log(y);
    if (x == y){
        document.getElementById("resposta").style.setProperty("background-color", "green");
        document.getElementById("resposta").innerHTML = "Número correto!";
        document.getElementById("X").innerHTML = x;
    }
    else{
        document.getElementById("resposta").style.setProperty("background-color", "red");
        document.getElementById("resposta").innerHTML = "Número incorreto!";
        if(x < y && isNaN(x) == false){
            var menor = document.getElementById("menores");
            menor.innerHTML += x + '| ';
        }
        else if (x > y && isNaN(x) == false){
            var maior = document.getElementById("maiores");
            maior.innerHTML += x + '| ';
        }
        
    }
}