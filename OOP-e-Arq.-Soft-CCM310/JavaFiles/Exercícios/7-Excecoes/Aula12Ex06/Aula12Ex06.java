
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

class CPFException extends Exception{
    public CPFException(String message) {
        super(message);
    }
    
}

class Pessoa{
    private String nome, sobrenome, CPF;
    private int idade;

    public Pessoa(String nome, String sobrenome, String CPF, int idade) throws CPFException {
        if(CPF.contains(".") || CPF.contains("-")){
            throw new CPFException("Erro: CPF não deve conter caracteres especiais (pontos ou hífens).");
        }
        this.nome = nome;
        this.sobrenome = sobrenome;
        this.CPF = CPF;
        this.idade = idade;
    }
    
    @Override
    public String toString() {
        return "Pessoa [nome=" + nome + ", sobrenome=" + sobrenome
                + ", idade=" + idade + ", CPF=" + CPF + "]";
    }
}

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex06 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Pessoa p1 = null;
        
        while(p1 == null){
            try{
                System.out.print("Digite o nome: ");
                String nome = sc.nextLine();

                System.out.print("Digite o sobrenome: ");
                String sobrenome = sc.nextLine();

                System.out.print("Digite a idade: ");
                int idade = sc.nextInt();
                sc.nextLine(); // limpa buffer

                System.out.print("Digite o CPF (sem pontos ou hífens): ");
                String cpf = sc.nextLine();

                p1 = new Pessoa(nome, sobrenome, cpf, idade);
            }
            catch(CPFException e){
                System.out.println("");
                System.err.println("Exceção capturada: " + e.getMessage());
                System.out.println("Por favor, digite o CPF novamente.");
                continue;
            }
            
            System.out.println("");
            System.out.println("Pessoa criada com sucesso:");
            System.out.println(p1);
        }
        sc.close();
    }
    
}
