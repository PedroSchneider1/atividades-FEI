package com.mycompany.aula03exe01;

public class Pessoa {
    private String nome;
    private String cpf;
    private int idade;
    
    public String getNome() {
        return nome;
    }
    
    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCpf() {
        return cpf;
    }

    public void setCpf(String cpf) {
        this.cpf = cpf;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        if (idade < 0 || idade > 150)
            idade = 0;
        this.idade = idade;
    }
}
