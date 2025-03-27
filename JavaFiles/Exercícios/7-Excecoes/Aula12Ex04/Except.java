/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Except extends Exception{
    private String msg;
    
    public Except(String msg) {
        this.msg = msg;
    }
    
    public String showMessage(){
        return this.msg;
    }
}
