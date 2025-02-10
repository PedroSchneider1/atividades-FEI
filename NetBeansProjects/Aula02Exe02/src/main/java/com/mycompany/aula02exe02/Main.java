package com.mycompany.aula02exe02;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        System.out.println("Informe a nota da P1: ");
        double P1 = sc.nextDouble();
        
        System.out.println("Informe a nota da P2: ");
        double P2 = sc.nextDouble();
        
        double media = (P1+P2)/2;
        
        if(media < 3){
            System.out.println("Reprovado direto!");
        }
        else{
            if(media >= 7){
                System.out.println("Aprovado direto!");
            }
            else {
                System.out.println("Informe a nota da P3: ");
                double P3 = sc.nextDouble();
                
                media = (media+P3)/2;
                
                if(media >= 5){
                    System.out.println("Aprovado por P3.");
                }
                else {
                    System.out.println("Reprovado por P3");
                }
            }
        }
    }
}
