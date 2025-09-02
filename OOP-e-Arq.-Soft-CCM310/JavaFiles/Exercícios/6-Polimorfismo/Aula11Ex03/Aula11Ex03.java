/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula11Ex03 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        MovablePoint p1 = new MovablePoint(0,0,0,0);
        MovableCircle c1 = new MovableCircle(p1, 10);
        
        System.out.println(c1);
        System.out.println(p1);
        
        p1.moveUp();
        p1.moveRight();
        p1.moveUp();
        
        System.out.println(p1);
        System.out.println(c1);
    }
    
}
