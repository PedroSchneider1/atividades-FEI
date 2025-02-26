package com.mycompany.aula06ex02;

public class Main {
    public static void main(String[] args) {
        Retangulo ret = new Retangulo(2,3,5,3,2,2,5,2);
        
        if (ret.verificaRetangulo() == 1){
            System.out.println("É retangulo");
            System.out.println(ret.calculaComprimento());
            System.out.println(ret.calculaLargura());
            System.out.println(ret.calculaPerimetro());
        }
        else{
            System.out.println("Não é retangulo");
        }
    }
}
