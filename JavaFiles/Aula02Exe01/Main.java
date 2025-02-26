package com.mycompany.aula02exe01;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        // recurso do tipo teclado
        Scanner teclado = new Scanner(System.in);
        
        System.out.println("Informe o ano atual: ");
        int anoAtual = teclado.nextInt();
        
        System.out.println("Informe o ano de nascimento: ");
        int anoNasc = teclado.nextInt();
        
        int idade = anoAtual - anoNasc;
        
        System.out.println("Sua idade é: " + idade);
        
        teclado.close();
    }
}
