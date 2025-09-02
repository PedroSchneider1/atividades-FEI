import java.lang.ArrayIndexOutOfBoundsException;
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] array = {1,132,32,43,631,6};
        
        while(1==1){
            int idx = 0;
            try{
                System.out.printf("Digite um indice do array: ");
                idx = sc.nextInt();
                System.out.println(array[idx]);
                System.out.println("Indíce válido!");
                break;
            }
            catch(ArrayIndexOutOfBoundsException e){
                System.err.println("Exceção: " + e);
            }
        }
    }
}
