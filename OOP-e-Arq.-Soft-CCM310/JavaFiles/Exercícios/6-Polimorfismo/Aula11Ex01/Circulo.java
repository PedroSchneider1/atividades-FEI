/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Circulo extends Formas{
    private double raio;

    public double area(){
        return Math.PI*Math.pow(this.raio,2);
    }

    @Override
    public double perimetro() {
        return 2*Math.PI*raio;
    }
    
    @Override
    public void print(){
        super.print();
        System.out.println("Área: " + this.area());
        System.out.println("Perímetro: " + this.perimetro());
    }
    
    public double getRaio() {
        return raio;
    }

    public void setRaio(double raio) {
        this.raio = raio;
    }
}
