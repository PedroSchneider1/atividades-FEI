package com.mycompany.aula06ex03;

import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        ArrayList<String> cores1 = new ArrayList<>();
        ArrayList<String> cores2 = new ArrayList<>();
        
        cores1.add("vermelho");
        cores1.add("azul");
        cores1.add("roxo");
        cores1.add("marrom");
        
        cores2.add("vermelho");
        cores2.add("laranja");
        cores2.add("azul");
        cores2.add("verde");
        
//        for(int i = 0; i < cores1.size(); i++){
//            if(cores1.get(i).equalsIgnoreCase(cores2.get(i))){
//                System.out.println("Cores iguais no indice " + i);
//            }
//            else{
//                System.out.println("Cores diferentes no indice " + i);
//            }
//        }
        
        int flag = 1;
        for(int i = 0; i < cores1.size(); i++){
            if(!(cores1.contains(cores2.get(i)))){
                System.out.println("Divergencia nas cores");
                flag = 0;
                break;
            }
        }
        
        if(flag == 1){
            System.out.println("Cores iguais");
        }
    }
}
