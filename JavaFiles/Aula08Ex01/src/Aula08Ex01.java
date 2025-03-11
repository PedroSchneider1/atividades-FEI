
import Pessoas.Aluno;
import java.util.ArrayList;
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

/**
 *
 * @author unifpschneider
 */
public class Aula08Ex01 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList alunos = new ArrayList<>();
        
        System.out.println("Digite o nome: ");
        String nome = sc.nextLine();
        
        System.out.println("Digite o sobrenome: ");
        String sobrenome = sc.nextLine();
        
        System.out.println("Digite a idade: ");
        int idade = sc.nextInt();
        sc.nextLine();

        System.out.println("Digite o curso: ");
        String curso = sc.nextLine();
        
        Aluno a1 = new Aluno(nome, sobrenome, curso, idade);
        Aluno a2 = new Aluno();
        
        alunos.add(a1);
        alunos.add(a2);
        
        alunos.forEach(_item -> {System.out.println(_item);} );
        
    }
    
}
