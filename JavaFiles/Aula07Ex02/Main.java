package com.mycompany.aula06ex02;

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class Main {
    public static void main(String[] args) {
        ArrayList <Pessoa> p = new ArrayList<>();
        
        p.add(new Pessoa("Fulano", 43));
        p.add(new Pessoa("Sicrano", 28));
        p.add(new Pessoa("Beltrano", 61));
        
//        Examplo for-each
//        for(Pessoa pessoa : p){
//            System.out.println(pessoa.getNome());
//            System.out.println(pessoa.getIdade());
//            System.out.println();
//        }

//        Examplo iterator
        Iterator<Pessoa> itr = p.iterator();
        
        while(itr.hasNext()){
            Pessoa pessoa = itr.next();
            System.out.println(pessoa.getNome());
            System.out.println(pessoa.getIdade());
            System.out.println();
        }
    }
}
