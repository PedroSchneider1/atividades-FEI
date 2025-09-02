
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

class VelocidadeMinException extends Exception{
    public VelocidadeMinException(String message) {
        super(message);
    }
}

class VelocidadeMaxException extends Exception{
    public VelocidadeMaxException(String message) {
        super(message);
    }
}

class Carro{
    private double velocidade, velocidadeMax;

    public Carro() {
    }

    public Carro(double velocidade, double velocidadeMax) {
        this.velocidade = velocidade;
        this.velocidadeMax = velocidadeMax;
    }

    public void acelerar(double valor) throws VelocidadeMaxException{
        this.velocidade += valor;
        if(this.getVelocidade() >= this.getVelocidadeMax()){
            this.setVelocidade(this.getVelocidadeMax());
            throw new VelocidadeMaxException("Velocidade máxima atingida.");
        }
    }
    
    public void frear(double valor) throws VelocidadeMinException{
        this.velocidade -= valor;
        if(this.getVelocidade() < 0){
            this.setVelocidade(0);
            throw new VelocidadeMinException("Velocidade mínima atingida, carro parado.");
        }
        
    }
    
    public double getVelocidade() {
        return velocidade;
    }

    public void setVelocidade(double velocidade) {
        this.velocidade = velocidade;
    }

    public double getVelocidadeMax() {
        return velocidadeMax;
    }

    public void setVelocidadeMax(double velocidadeMax) {
        this.velocidadeMax = velocidadeMax;
    }
    
    
}

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex08 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Carro carro = new Carro(100, 170);
        double vel = 1;
        
        while(vel > 0){
            try{
                System.out.println("Velocidade atual: " + carro.getVelocidade());

                System.out.printf("Deseja acelarar ou frear? (a/f) ");
                char opt = sc.next().charAt(0);
                
                if(opt == 'a' || opt == 'A'){
                    System.out.printf("Digite a velocidade: ");
                    vel = sc.nextDouble();
                    carro.acelerar(vel);
                }
                else if(opt == 'f' || opt == 'F'){
                    System.out.printf("Digite a velocidade: ");
                    vel = sc.nextDouble();
                    carro.frear(vel);
                }
                else{
                    System.out.println("Opção inválida.\n");
                }
            }
            catch(VelocidadeMinException | VelocidadeMaxException e){
                System.err.println("Exceção: " + e.getMessage());
            }
        }
    }
    
}
