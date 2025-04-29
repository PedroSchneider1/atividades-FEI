/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import javax.swing.*;
import java.sql.Connection;
import java.sql.SQLException;
import View.CadastroFrame;
import Model.Aluno;
import DAO.*;

/**
 *
 * @author unifpschneider
 */
public class ControllerCadastro {
    private CadastroFrame view;

    public ControllerCadastro(CadastroFrame view) {
        this.view = view;
    }
    
    public void salvarAluno(){
        String nome = view.getTxt_nome_cadastro().getText();
        String usuario = view.getTxt_usuario_cadastro().getText();
        String senha = view.getTxt_senha_cadastro().getText();
        Aluno aluno = new Aluno(nome,usuario,senha);
        
        Conexao conexao = new Conexao();
        try{
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            dao.inserir(aluno);
            JOptionPane.showMessageDialog(view,
                                              "Usuário cadastrado com sucesso!",
                                              "Inserção!",
                                              JOptionPane.INFORMATION_MESSAGE);
        } catch(SQLException e){
            JOptionPane.showMessageDialog(view,
                                              "Erro de conexão.",
                                              "ERRO!",
                                              JOptionPane.ERROR_MESSAGE);
        }
    }
}
