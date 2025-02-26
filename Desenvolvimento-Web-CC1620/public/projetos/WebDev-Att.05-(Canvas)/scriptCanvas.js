let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');

function desenhar_quadrado(x, y, cor, w, h){
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = cor;
    ctx.fillStyle = cor;
    ctx.strokeRect(x, y, w, h);
    ctx.fillRect(x, y, w, h);
    ctx.closePath();
}

function desenhar_linha(x1,y1,x2,y2,cor){
    ctx.beginPath();
    ctx.lineWidth = 1;
    ctx.strokeStyle = cor;
    ctx.moveTo(x1, y1);
    ctx.lineTo(x2, y2);
    ctx.stroke();
    ctx.closePath();
}

function desenhar_arco(x,y,r,ang1,ang2,cor1, cor2, fill){
    ctx.beginPath();
    ctx.lineWidth = 2;
    ctx.strokeStyle = cor1;
    ctx.fillStyle = cor2;
    ctx.arc(x, y, r, ang1, ang2);
    ctx.stroke();
    if(fill == true){
        ctx.fill();
    }
    ctx.closePath();
}

function escrever(x, y, texto, cor){
    ctx.beginPath();
    ctx.lineWidth = 0.1;
    ctx.strokeStyle = cor;
    ctx.fillStyle = cor;
    ctx.font = "28px Arial"
    ctx.strokeText(texto, x, y)
    ctx.fillText(texto, x, y);
    ctx.closePath();
}

// Quadrados
desenhar_quadrado(0,0,'blue', 50, 50); // Quadrado azul (sup. esq.)
desenhar_quadrado(250,0,'red', 50, 50); // Quadrado vermelho (sup. dir.)
desenhar_quadrado(0,270,'yellow', 30, 30); // Quadrados amarelos (sup. esq.)
desenhar_quadrado(0,240,'yellow', 30, 30);
desenhar_quadrado(30,270,'yellow', 30, 30);
desenhar_quadrado(270,270,'black', 30, 30); // Quadrados pretos (sup. dir.)
desenhar_quadrado(270,240,'black', 30, 30);
desenhar_quadrado(240,270,'black', 30, 30);
desenhar_quadrado(110,150,'red', 40, 40); // Quadrado vermelho (centro esq.)
desenhar_quadrado(0,150,'cyan', 30, 30); // Quadrados azuis (centro esq.)
desenhar_quadrado(0,120,'cyan', 30, 30);
desenhar_quadrado(270,135,'cyan', 30, 15); // Quadrados azuis (centro dir.)
desenhar_quadrado(270,150,'cyan', 30, 15);

// Linhas
desenhar_linha(0,0,150,150,'blue'); // Linha azul
desenhar_linha(300,0,150,150,'red'); // Linha vermelha
desenhar_linha(0,150,300,150,'green'); // Linha verde
desenhar_linha(150,300,150,150,'gray'); // Linha cinza

// (Semi)Círculos
desenhar_arco(75,225,15, 0, 2*Math.PI, 'green', 'yellow', true); // Círculo amarelo (inf. esq.)
desenhar_arco(225,225,15, 0, 2*Math.PI, 'green', 'yellow', true); // Círculo amarelo (inf. dir.)
desenhar_arco(150,115,15, 0, 2*Math.PI, 'blue', 'cyan', true); // Círculo azul (acima do centro)
desenhar_arco(150,150,60, Math.PI, 2*Math.PI, 'green', 'white', false); // Semicírculo verde (centro)
desenhar_arco(150,150,75, 1*Math.PI, 1.25*Math.PI, 'green', 'white', false); // Arco verde (centro esq.)
desenhar_arco(150,150,75, 1.75*Math.PI, 2*Math.PI, 'green', 'white', false); // Arco verde (centro esq.)
desenhar_arco(150,300,40, Math.PI, 2*Math.PI, 'green', 'cyan', true); // Semicírculo azul (baixo)
desenhar_arco(150,300,60, 1.5*Math.PI, 2*Math.PI, 'green', 'white', false); // Arco verde (baixo dir.)
desenhar_arco(150,300,75, 1*Math.PI, 1.5*Math.PI, 'green', 'white', false); // Arco verde (baixo esq.)

// Texto
escrever(100,50,'Canvas', 'black');