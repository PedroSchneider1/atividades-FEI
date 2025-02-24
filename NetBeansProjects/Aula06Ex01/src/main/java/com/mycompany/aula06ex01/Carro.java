package com.mycompany.aula06ex01;

public class Carro {
    private String modelo, cor;
    private int ano;
    private double km, preco;
    
    //Construtor não parametrizado (construtor padrão)
    public Carro(){
    }
    
    //Construtor parcialmente parametrizado
    public Carro(String modelo, int ano, double preco){
        this.modelo = modelo;
        this.ano = ano;
        this.preco = preco;
    }
    
    //Construtor totalmente parametrizado
    public Carro(String modelo, String cor, int ano, double km, double preco) {
        this.modelo = modelo;
        this.cor = cor;
        this.ano = ano;
        this.km = km;
        this.preco = preco;
    }

    //Getters and setters
    public String getModelo() {
        return modelo;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

    public String getCor() {
        return cor;
    }

    public void setCor(String cor) {
        this.cor = cor;
    }

    public int getAno() {
        return ano;
    }

    public void setAno(int ano) {
        this.ano = ano;
    }

    public double getKm() {
        return km;
    }

    public void setKm(double km) {
        this.km = km;
    }

    public double getPreco() {
        return preco;
    }

    public void setPreco(double preco) {
        this.preco = preco;
    }

    @Override
    public String toString() {
        return "Carro{" + "modelo=" + modelo + ", cor=" + cor + ", ano=" + ano
                        + ", km=" + km + ", preco=" + preco + '}';
    }
    
}
