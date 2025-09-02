/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class MovableCircle implements Movable{
    private int radius;
    private MovablePoint center;

    public MovableCircle(MovablePoint center, int radius) {
        this.center = center;
        this.radius = radius;
    }

    @Override
    public String toString() {
        return "Center => " + this.center.toString()
                + "| Radius = " + this.radius;
    }
    
    @Override
    public void moveUp() {
        this.center.moveUp();
    }

    @Override
    public void moveDown() {
        this.center.moveDown();
    }

    @Override
    public void moveLeft() {
        this.center.moveLeft();
    }

    @Override
    public void moveRight() {
        this.center.moveRight();
    }
}
