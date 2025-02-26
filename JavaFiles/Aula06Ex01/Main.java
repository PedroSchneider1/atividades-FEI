package com.mycompany.aula06ex01;

public class Main {
    public static void main(String[] args) {
        Carro c1 = new Carro();
        Carro c2 = new Carro("Uno", 2012, 12499.99);
        Carro c3 = new Carro("Polo", "Preto", 2015, 15327, 9999.98);
        
        System.out.println("===CARRO 1===");
        System.out.println("Modelo: " + c1.getModelo() + " Cor: "
                           + c1.getCor() + " Ano: " + c1.getAno()
                           + " KM: " + c1.getKm() + " Preço: "
                           + c1.getPreco());
        
        System.out.println("===CARRO 2===");
        System.out.println("Modelo: " + c2.getModelo() + " Cor: "
                           + c2.getCor() + " Ano: " + c2.getAno()
                           + " KM: " + c2.getKm() + " Preço: "
                           + c2.getPreco());
        
        System.out.println("===CARRO 3===");
        System.out.println("Modelo: " + c3.getModelo() + " Cor: "
                           + c3.getCor() + " Ano: " + c3.getAno()
                           + " KM: " + c3.getKm() + " Preço: "
                           + c3.getPreco());
        
        System.out.println("===CARRO teste===");
        System.out.println(c3);
    }
}