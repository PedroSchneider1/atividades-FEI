package com.mycompany.aula03exe02;

public class Swapper {
    private double x, y;

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public void setX(double x) {
        this.x = x;
    }

    public void setY(double y) {
        this.y = y;
    }
    
    public void swap(){
        double temp;
        temp = this.x;
        this.x = this.y;
        this.y = temp;
    }
}
