/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import Model.Soma;
import View.Janela;

/**
 *
 * @author unifpschneider
 */
public class Control {
    private Janela view;

    public Control(Janela view) {
        this.view = view;
    }
    
    public void controlSomar(){
        double n1 = Double.parseDouble(view.getTxt_1().getText());
        double n2 = Double.parseDouble(view.getTxt_2().getText());
        Soma s = new Soma();
        view.getTxt_result().setText(String.valueOf(s.calcular(n1, n2)));
    }
    
    public void controlLimpar(){
        view.getTxt_1().setText("");
        view.getTxt_2().setText("");
        view.getTxt_result().setText("");
    }
}
