package com.mycompany.aula02exe06;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a, b, c;
        
        System.out.println("Digite o valor de 'a': ");
        a = sc.nextInt();

        System.out.println("Digite o valor de 'b': ");
        b = sc.nextInt();

        System.out.println("Digite o valor de 'c': ");
        c = sc.nextInt();

        int temp;
        if(a>b){
            temp = a;
            a = b;
            b = temp;
        }
        if(a>c){
            temp = a;
            a = c;
            c = temp;
        }
        if(b>c){
            temp = b;
            b = c;
            c = temp;
        }
        
        System.out.printf("A: %d | B: %d | C: %d", a,b,c);
        
        sc.close();
    }
}
