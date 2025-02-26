package com.mycompany.aula03exe01;

import java.util.Scanner;

public class TestePessoa {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String nome, cpf;
        int idade;
        
        Pessoa p1 = new Pessoa();
        
        System.out.println("---- DADOS DA PESSOA 1 ----");
        System.out.println("Digite o nome: ");
        nome = sc.nextLine();
        p1.setNome(nome);
        System.out.println("Digite o CPF: ");
        cpf = sc.nextLine();
        p1.setCpf(cpf);
        System.out.println("Digite a idade: ");
        idade = sc.nextInt();
        p1.setIdade(idade);
        
        System.out.println("");
        System.out.println("Nome....: " + p1.getNome());
        System.out.println("CPF.....: " + p1.getCpf());
        System.out.println("Idade...: " + p1.getIdade());
        
        //limpando o buffer
        sc.nextLine();
        
        Pessoa p2 = new Pessoa();
        
        System.out.println("\n---- DADOS DA PESSOA 2 ----");
        System.out.println("Digite o nome: ");
        nome = sc.nextLine();
        p2.setNome(nome);
        System.out.println("Digite o CPF: ");
        cpf = sc.nextLine();
        p2.setCpf(cpf);
        System.out.println("Digite a idade: ");
        idade = sc.nextInt();
        p2.setIdade(idade);
        
        System.out.println("");
        System.out.println("Nome....: " + p2.getNome());
        System.out.println("CPF.....: " + p2.getCpf());
        System.out.println("Idade...: " + p2.getIdade());
        
        //limpando o buffer
        sc.nextLine();
        
        Pessoa p3 = new Pessoa();
        
        System.out.println("\n---- DADOS DA PESSOA 3 ----");
        System.out.println("Digite o nome: ");
        nome = sc.nextLine();
        p3.setNome(nome);
        System.out.println("Digite o CPF: ");
        cpf = sc.nextLine();
        p3.setCpf(cpf);
        System.out.println("Digite a idade: ");
        idade = sc.nextInt();
        p3.setIdade(idade);
        
        System.out.println("");
        System.out.println("Nome....: " + p3.getNome());
        System.out.println("CPF.....: " + p3.getCpf());
        System.out.println("Idade...: " + p3.getIdade());
    }
    
}
