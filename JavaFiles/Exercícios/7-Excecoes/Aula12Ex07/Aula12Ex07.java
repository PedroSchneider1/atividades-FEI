
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

class WrongLoginException extends Exception{
    public WrongLoginException(String message) {
        super(message);
    }
}

class Login{
    private String usuario, senha;

    public Login(String usuario, String senha) {
        this.usuario = usuario;
        this.senha = senha;
    }

    public void logar(String usuario, String senha) throws WrongLoginException{
        if(usuario.equals(this.getUsuario()) && senha.equals(this.getSenha())){
            return;
        }
        throw new WrongLoginException("Usuário e/ou senha incorretos.");
    }
    
    public String getUsuario() {
        return usuario;
    }

    public void setUsuario(String usuario) {
        this.usuario = usuario;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }
}

/**
 *
 * @author unifpschneider
 */
public class Aula12Ex07 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Login login = new Login("adm","adm");
        Scanner sc = new Scanner(System.in);
        
        try{
            System.out.print("Digite o usuario: ");
            String usuario = sc.nextLine();

            System.out.print("Digite a senha: ");
            String senha = sc.nextLine();
            
            login.logar(usuario, senha);
            System.out.println("Login realizado com sucesso.");
        }
        catch(WrongLoginException e){
            System.out.println("");
            System.err.println("Exceção capturada: " + e.getMessage());
        }

        sc.close();
        
    }
    
}
