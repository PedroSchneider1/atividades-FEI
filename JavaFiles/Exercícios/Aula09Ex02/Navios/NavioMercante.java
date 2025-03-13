/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Navios;

/**
 *
 * @author unifpschneider
 */
public class NavioMercante extends Navio{
     private double capacidadeCarga, carga;

    public NavioMercante(int numTripulantes, String nome,
                         double capacidadeCarga, double carga) {
        super(numTripulantes, nome);
        this.capacidadeCarga = capacidadeCarga;
        this.carga = carga;
    }
     
    public void carregamento(){
        super.exibirInfoGeral();
        System.out.printf("\nVolume: " + (this.carga)/(this.capacidadeCarga));
    }
}
