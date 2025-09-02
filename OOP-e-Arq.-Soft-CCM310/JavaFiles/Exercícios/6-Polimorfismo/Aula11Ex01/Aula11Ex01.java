
import java.util.ArrayList;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula11Ex01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        ArrayList<Formas> formas = new ArrayList<>();
        formas.add(new Circulo());
        formas.add(new Retangulo());
        
        formas.get(0).setTipo("Circulo");
        ((Circulo)formas.get(0)).setRaio(7.5);
        
        formas.get(1).setTipo("Retangulo");
        ((Retangulo)formas.get(1)).setComprimento(8);
        ((Retangulo)formas.get(1)).setLargura(9);
        
        ((Circulo)formas.get(0)).print();
        ((Retangulo)formas.get(1)).print();
    }
}
