/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Navios;

/**
 *
 * @author unifpschneider
 */
public class PortaAvioes extends NavioDeGuerra{
    private int numAvioes;

    public PortaAvioes(int numTripulantes, String nome, double blindagem, double ataque, int numAvioes) {
        super(numTripulantes, nome, blindagem, ataque);
        this.numAvioes = numAvioes;
    }
    
    @Override
    public void poderDeFogo(){
        double atk = this.getAtaque()*((double)(Math.pow((this.numAvioes), 2)));
        System.out.printf("\nPoder de fogo do porta-aviões: " + atk);
    }
}