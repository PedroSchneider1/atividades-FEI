package com.mycompany.aula04ex01;

public class TesteFuncionario {
    public static void main(String[] args) {
        Funcionario f1 = new Funcionario();
        Funcionario f2 = new Funcionario("Elder", "Machado",
                                        20000.58, 54, "Masculino", 5);
        
        System.out.println("f1 " + f1.getNome() + " " + f1.getSobrenome()
                           + " " + f1.getSalario_mensal() + " " + f1.getIdade()
                           + " " + f1.getNumero());
        System.out.println("f2 " + f2.getNome() + " " + f2.getSobrenome()
                           + " " + f2.getSalario_mensal() + " " + f2.getIdade()
                           + " " + f2.getNumero());
        
    }
}
