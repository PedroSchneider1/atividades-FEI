package com.mycompany.aula02exe05;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        double salHora, qttHora;
        
        System.out.println("Digite o valor do seu salario/hora e as horas trabalhadas: ");
        salHora = sc.nextDouble();
        qttHora = sc.nextDouble();
        
        double salario = salHora * qttHora;
        
        System.out.println("Seu salário é: " + salario);
        sc.close();
    }
}
