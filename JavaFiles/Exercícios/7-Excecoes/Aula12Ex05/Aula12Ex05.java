/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

class ExcecaoA extends Exception {
    public ExcecaoA(String message) {
        super(message);
    }
}

class ExcecaoB extends Exception {
    public ExcecaoB(String message) {
        super(message);
    }
}

class ExcecaoC extends Exception {
    public ExcecaoC(String message) {
        super(message);
    }
}

class LancaExcecoes {
    public void lancaExcecoes(int tipo) throws ExcecaoA, ExcecaoB, ExcecaoC{
        switch (tipo) {
            case 1 -> throw new ExcecaoA("Exceção A lançada!");
            case 2 -> throw new ExcecaoB("Exceção B lançada!");
            case 3 -> throw new ExcecaoC("Exceção C lançada!");
            default -> {
            }
        }
    }
}

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex05 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        LancaExcecoes lancaExcecoes = new LancaExcecoes();

        try {
            lancaExcecoes.lancaExcecoes(1);
        } catch (Exception e) {
            System.out.println("Exceção capturada: " + e.getMessage());
        }
    }
    
}
