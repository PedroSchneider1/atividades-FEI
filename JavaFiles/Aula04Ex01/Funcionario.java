package com.mycompany.aula04ex01;

public class Funcionario {
    private String nome;
    private String sobrenome;
    private double salario_mensal;
    private int idade;
    private String sexo;
    private int numero;

    public Funcionario(){
    }
    
    public Funcionario(String nome, String sobrenome, double salario_mensal,
                       int idade, String sexo, int numero) {
        setNome(nome);
        setSobrenome(sobrenome);
        setSalario_mensal(salario_mensal);
        setIdade(idade);
        setSexo(sexo);
        setNumero(numero);
    }
    
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getSobrenome() {
        return sobrenome;
    }

    public void setSobrenome(String sobrenome) {
        this.sobrenome = sobrenome;
    }

    public double getSalario_mensal() {
        return salario_mensal;
    }

    public void setSalario_mensal(double salario_mensal) {
        this.salario_mensal = salario_mensal;
    }

    public int getIdade() {
        return idade;
    }

    public void setIdade(int idade) {
        if(idade < 0 || idade > 150)
            idade = 0;
        this.idade = idade;
    }

    public String getSexo() {
        return sexo;
    }

    public void setSexo(String sexo) {
        this.sexo = sexo;
    }

    public int getNumero() {
        return numero;
    }

    public void setNumero(int numero) {
        this.numero = numero;
    }
}
