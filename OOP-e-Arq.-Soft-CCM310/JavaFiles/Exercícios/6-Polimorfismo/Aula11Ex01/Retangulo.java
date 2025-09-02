/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Retangulo extends Formas{
    private double comprimento,largura;

    @Override
    public double perimetro() {
        return (2*comprimento)+(2*largura);
    }

    @Override
    public void print() {
        super.print();
        System.out.println("Largura: " + this.largura);
        System.out.println("Comprimento: " + this.comprimento);
        System.out.println("Perimetro: " + this.perimetro());
    }

    public double getLargura() {
        return largura;
    }

    public double getComprimento() {
        return comprimento;
    }

    public void setLargura(double largura) {
        this.largura = largura;
    }

    public void setComprimento(double comprimento) {
        this.comprimento = comprimento;
    }
}