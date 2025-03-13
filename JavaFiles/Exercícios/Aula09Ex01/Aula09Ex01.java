import Politicos.Prefeito;
import Politicos.Vereador;
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
public class Aula09Ex01 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<Prefeito> prefeitos = new ArrayList<>();
        ArrayList<Vereador> vereadores = new ArrayList<>();
        
        for(int i = 0; i < 3; i++){
            System.out.println("==Cadastre os prefeitos==");
            System.out.println("Digite seu nome: ");
            String nome = sc.nextLine();
            System.out.println("Digite seu partido: ");
            String partido = sc.nextLine();
            System.out.println("Digite seu estado: ");
            String estado = sc.nextLine();
            System.out.println("Digite seu municipio: ");
            String municipio = sc.nextLine();
            System.out.println("Digite sua função: ");
            String funcao = sc.nextLine();
            
            Prefeito p1 = new Prefeito(nome, partido, estado, funcao, municipio);
            prefeitos.add(p1);
        }
        for(int i = 0; i < 3; i++){
            System.out.println("==Cadastre os vereadores==");
            System.out.println("Digite seu nome: ");
            String nome = sc.nextLine();
            System.out.println("Digite seu partido: ");
            String partido = sc.nextLine();
            System.out.println("Digite seu estado: ");
            String estado = sc.nextLine();
            System.out.println("Digite seu municipio: ");
            String municipio = sc.nextLine();
            System.out.println("Digite sua função: ");
            String funcao = sc.nextLine();
            
            Vereador v1 = new Vereador(nome, partido, estado, funcao, municipio);
            vereadores.add(v1);
        }
        
        System.out.println();
        System.out.println("PREFEITOS");
        for(Prefeito p : prefeitos){
            p.apresentacao();
        }
        System.out.println("VEREADORES");
        for(Vereador v : vereadores){
            v.apresentacao();
        }
    }
}