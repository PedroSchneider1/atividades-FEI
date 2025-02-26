let retangulo = { // Cria o objeto "retangulo"
    x: 0,
    y: 0,
    largura: 50,
    altura: 50,
    cor_linha: "black",
    cor_preenchimento: "red",
    desenha: function(){ // Cria a função "desenha" para desenhar o retangulo com base nos seus atributos
        ctx.beginPath();
        ctx.strokeStyle = this.cor_linha;
        ctx.fillStyle = this.cor_preenchimento;
        ctx.strokeRect(this.x, this.y, this.largura, this.altura);
        ctx.fillRect(this.x, this.y, this.largura, this.altura);
        ctx.closePath();
    }
};

function animacao(){ // Cria a função "animacao" que apaga os pixels do canvas, chama a função "desenha" e espera um tempo para começar novamente
    ctx.clearRect(0,0,300,300);
    
    if(retangulo.x < 0)
        retangulo.x = 0
    if(retangulo.x > 250)
        retangulo.x = 250
    if(retangulo.y < 0)
        retangulo.y = 0
    if(retangulo.y > 250)
        retangulo.y = 250
        
    retangulo.desenha();
    requestAnimationFrame(animacao);
}

let canvas = document.getElementById("canvas");
let ctx = canvas.getContext("2d");

document.addEventListener('mousemove', function(evento){
    rect = canvas.getBoundingClientRect();
    x_mouse = evento.clientX - rect.left - 25,
    y_mouse = evento.clientY - rect.top - 25;

    retangulo.x = x_mouse;
    retangulo.y = y_mouse;

});

animacao();