/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import Model.Operacoes;
import View.Janela;

/**
 *
 * @author unifpschneider
 */

// CORRIGIR O ERRO DE FAZER MAIS DE UMA OPERAÇÃO SEQUENCIAL
public class Control extends Operacoes{
    private Janela view;
    private Operacoes o = new Operacoes();
    private double resultado = 0;
    private char operacao;


    public Control(Janela view) {
        this.view = view;
    }
    
    public void controlLimpa(){
        view.getTXT_1().setText("");
        resultado = 0;
    }
    
    public void controlIgual(){
        double n2 = Double.parseDouble(view.getTXT_1().getText());
        switch(this.operacao){
            case 's':
                view.getTXT_1().setText(String.valueOf(o.soma(resultado, n2)));
                break;
            case 'u':
                view.getTXT_1().setText(String.valueOf(o.subtracao(resultado, n2)));
                break;
            case 'm':
                view.getTXT_1().setText(String.valueOf(o.multiplicacao(resultado, n2)));
                break;
            case 'd':
                view.getTXT_1().setText(String.valueOf(o.divisao(resultado, n2)));
                break;
            default:
                System.err.println("Erro na escolha de operação.");
                break;
        }
    }
    
    public void controlSomar(){
        double n1 = Double.parseDouble(view.getTXT_1().getText());
        resultado = o.soma(resultado, n1);
        this.operacao = 's';
        view.getTXT_1().setText("");
    }
    
    public void controlSubtrair(){
        double n1 = Double.parseDouble(view.getTXT_1().getText());
        resultado = n1;
        this.operacao = 'u';
        view.getTXT_1().setText("");
    }
    
    public void controlMultiplicacao(){
        double n1 = Double.parseDouble(view.getTXT_1().getText());
        resultado = n1;
        this.operacao = 'm';
        view.getTXT_1().setText("");
    }
    
    public void controlDivisao(){
        double n1 = Double.parseDouble(view.getTXT_1().getText());
        resultado = n1;
        this.operacao = 'd';
        view.getTXT_1().setText("");
    }
}
