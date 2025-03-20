/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Navios;

/**
 *
 * @author unifpschneider
 */
public class Cruzador extends NavioDeGuerra{
    private int numCanhoes;

    public Cruzador(int numTripulantes, String nome, double blindagem, double ataque, int numCanhoes) {
        super(numTripulantes, nome, blindagem, ataque);
        this.numCanhoes = numCanhoes;
    }
    
    @Override
    public void poderDeFogo(){
        double atk = this.getAtaque()*((double)(Math.pow((this.numCanhoes), 2)));
        System.out.printf("\nPoder de fogo do cruzador: " + atk);
    }
}
