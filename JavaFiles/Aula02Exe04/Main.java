package com.mycompany.aula02exe04;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double soma = 0;
        double num = 1;
        
        while(num != 0){
            System.out.println("Digite um numero (0 para sair): ");
            num = sc.nextDouble();
            
            soma = soma + num;
        }
        
        System.out.println("A soma dos números é: " + soma);
    }
}
