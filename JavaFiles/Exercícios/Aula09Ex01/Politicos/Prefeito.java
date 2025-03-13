/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Politicos;

/**
 *
 * @author unifpschneider
 */
public class Prefeito extends Politico{
    private String municipio;

    public Prefeito(String nome, String partido, String estado, String funcao, String municipio) {
        super(nome, partido, estado, funcao);
        this.municipio = municipio;
    }
    
    @Override
    public void apresentacao(){
        super.apresentacao();
        System.out.printf(", no municipio de " + municipio + "\n");
    }
}
