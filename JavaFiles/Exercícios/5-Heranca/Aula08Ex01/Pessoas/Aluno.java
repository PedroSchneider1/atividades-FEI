/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Pessoas;

/**
 *
 * @author unifpschneider
 */
public class Aluno extends Pessoa {
    protected String curso;

    public Aluno() {
    }
    
    public Aluno(String curso, String nome, String sobrenome, int idade) {
        super(nome, sobrenome, idade);
        this.curso = curso;
    }

    public String getCurso() {
        return curso;
    }

    public void setCurso(String curso) {
        this.curso = curso;
    }

    @Override
    public String toString() {
        return "Aluno{" + "nome=" + nome 
                        + ", sobrenome=" + sobrenome 
                        + ", idade=" + idade 
                        + ", curso=" + curso + '}';
    }
}
