package com.mycompany.aula03exe02;

import java.util.Scanner;

public class SwapperDemo {
    public static void main(String[] args) {
        Swapper troca = new Swapper();
        Scanner sc = new Scanner(System.in);
        
        double x, y;
        System.out.println("Digite o valor de X e Y: ");
        x = sc.nextDouble();
        y = sc.nextDouble();
        
        troca.setX(x);
        troca.setY(y);
        troca.swap();
        
        System.out.println("Os valores trocados são: " + troca.getX() + " e " + troca.getY());
    }
}
