/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Navios;

/**
 *
 * @author unifpschneider
 */
public class NavioDeGuerra extends Navio{
    private double blindagem, ataque;

    public NavioDeGuerra(int numTripulantes, String nome,
                         double blindagem, double ataque) {
        super(numTripulantes, nome);
        this.blindagem = blindagem;
        this.ataque = ataque;
    }

    public double getAtaque() {
        return ataque;
    }
    
    public void poderDeFogo(){
        System.out.printf("\nPoder de fogo: " + this.ataque);
    }
    
    public void exibirArmas(){
        super.exibirInfoGeral();
        System.out.printf("\nBlindagem: " + this.blindagem);
        this.poderDeFogo();
    }
}