package com.mycompany.aula02exe03;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double altura;
        double somaAlturas = 0;
        int contPessoas = 0;
        
        while(contPessoas < 5){
            System.out.println("Informe uma altura: ");
            altura = sc.nextDouble();
            
            somaAlturas = somaAlturas + altura;
            contPessoas = contPessoas + 1;
        }
        
        double media = somaAlturas/contPessoas;
        
        System.out.println("A media das alturas é: " + media);
    }
}
