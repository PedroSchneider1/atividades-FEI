/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex02 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Integer[] itens = new Integer[10];
        itens[0] = 1;
        
        for(int i = 0; i < itens.length; i++){
            try{
                System.out.println(itens[i].toString());
            }
            catch(NullPointerException e){
                System.err.println("Exception NullPointer no indice: " + i);
            }
        }
    }
    
}
