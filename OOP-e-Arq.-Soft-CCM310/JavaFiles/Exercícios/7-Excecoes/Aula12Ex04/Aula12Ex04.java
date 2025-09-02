/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex04 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            throw new Except("Esta é uma nova classe de exceção.");
        } catch (Except e) {
            System.err.println("Nova exceção capturada: " + e.showMessage());
        } finally {
            System.out.println("Bloco finally executado.");
        }
    }
    
}
