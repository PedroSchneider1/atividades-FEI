/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Model;

/**
 *
 * @author unifpschneider
 */
public class Operacoes extends Calculadora{
    @Override
    public double soma(double a, double b){
        return a + b;
    }
    
    @Override
    public double subtracao(double a, double b){
        return a - b;
    }
    
    @Override
    public double multiplicacao(double a, double b){
        return a * b;
    }
    
    @Override
    public double divisao(double a, double b){
        return a / b;
    }
}
