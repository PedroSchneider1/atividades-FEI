/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        try {
            throw new Exception("Esta é uma exceção.");
        } catch (Exception e) {
            System.err.println("Exceção capturada: " + e.getMessage());
        } finally {
            System.out.println("Bloco finally executado.");
        }
    }
}
