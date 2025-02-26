package com.mycompany.aula06ex01;

public class Main {
    public static void main(String[] args) {
        Laser l[] = new Laser[10];
        
        for(int i = 0; i < l.length; i++){
            l[i] = new Laser("Xiami", 10*i, 20/(i+1), Math.pow(2,i));
        }
        
        for(int i = 0; i < l.length; i++){
            System.out.println(l[i]);
        }
    }
}
