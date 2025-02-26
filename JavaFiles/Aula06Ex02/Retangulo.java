package com.mycompany.aula06ex02;

import static java.lang.Math.sqrt;
import static java.lang.Math.pow;

public class Retangulo {
    private double x1,y1;
    private double x2,y2;
    private double x3,y3;
    private double x4,y4;

    public Retangulo() {
    }

    public Retangulo(double x1, double y1, double x2, double y2, double x3, double y3, double x4, double y4) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
        this.x3 = x3;
        this.y3 = y3;
        this.x4 = x4;
        this.y4 = y4;
    }
    
    public int verificaRetangulo(){
        if((this.y1 != this.y2) || (this.y3 != this.y4))
            return 0;
        else{
            if((this.x1 != this.x3) || this.x2 != this.x4)
                return 0;
        }
        return 1;
    }

    public double calculaComprimento(){
        double lado1 = sqrt(pow((this.x1-this.x2),2)+pow((this.y1-this.y2),2));
        double lado2 = sqrt(pow((this.x3-this.x4),2)+pow((this.y3-this.y4),2));
        return (lado1 > lado2) ? lado1 : lado2;
    }
    
    public double calculaLargura(){
        double lado1 = sqrt(pow((this.x1-this.x2),2)+pow((this.y1-this.y2),2));
        double lado2 = sqrt(pow((this.x3-this.x4),2)+pow((this.y3-this.y4),2));
        return (lado1 < lado2) ? lado1 : lado2;
    }
    
    public double calculaPerimetro(){
        double comp = this.calculaComprimento();
        double larg = this.calculaLargura();
        
        double perimetro = (2*comp) + (2*larg);
        return perimetro;
    }
    
    public double getX1() {
        return x1;
    }

    public void setX1(double x1) {
       this.x1 = (x1 >= 0 && x1 <= 20.0) ? x1 : 0;
    }

    public double getY1() {
        return y1;
    }

    public void setY1(double y1) {
        this.y1 = (y1 >= 0 && y1 <= 20.0) ? y1 : 0;
    }

    public double getX2() {
        return x2;
    }

    public void setX2(double x2) {
        this.x2 = (x2 >= 0 && x2 <= 20.0) ? x2 : 0;
    }

    public double getY2() {
        return y2;
    }

    public void setY2(double y2) {
        this.y2 = (y2 >= 0 && y2 <= 20.0) ? y2 : 0;
    }

    public double getX3() {
        return x3;
    }

    public void setX3(double x3) {
        this.x3 = (x3 >= 0 && x3 <= 20.0) ? x3 : 0;
    }

    public double getY3() {
        return y3;
    }

    public void setY3(double y3) {
        this.y3 = (y3 >= 0 && y3 <= 20.0) ? y3 : 0;
    }

    public double getX4() {
        return x4;
    }

    public void setX4(double x4) {
        this.x4 = (x4 >= 0 && x4 <= 20.0) ? x4 : 0;
    }

    public double getY4() {
        return y4;
    }

    public void setY4(double y4) {
        this.y4 = (y4 >= 0 && y4 <= 20.0) ? y4 : 0;
    }
    
    
}
