/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Navios;

/**
 *
 * @author unifpschneider
 */
public class Navio {
    protected int numTripulantes;
    protected String nome;

    public Navio(int numTripulantes, String nome) {
        this.numTripulantes = numTripulantes;
        this.nome = nome;
    }
    
    public void exibirInfoGeral(){
        System.out.printf("Nome do navio: " + this.nome +
                            "\nNúmero de tripulantes: " + this.numTripulantes);
    }
}
