/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Politicos;

/**
 *
 * @author unifpschneider
 */
public class Politico {
    protected String nome, partido, estado, funcao;

    public Politico() {
    }
    
    public Politico(String nome, String partido, String estado, String funcao) {
        this.nome = nome;
        this.partido = partido;
        this.estado = estado;
        this.funcao = funcao;
    }
    
    public void apresentacao(){
        System.out.printf("Olá! Sou o político " + nome
                            + ", do partido " + partido
                            + ", na função de " + funcao
                            + ", estado de " + estado);
    }
}
