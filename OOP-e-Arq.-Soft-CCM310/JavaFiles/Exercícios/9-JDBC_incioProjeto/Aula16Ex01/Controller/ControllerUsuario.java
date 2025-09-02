/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import javax.swing.*;
import java.sql.Connection;
import java.sql.SQLException;
import View.AltExcFrame;
import Model.Aluno;
import DAO.*;

/**
 *
 * @author unifpschneider
 */
public class ControllerUsuario {
    private AltExcFrame view;
    private Aluno aluno;

    public ControllerUsuario(AltExcFrame view, Aluno aluno) {
        this.view = view;
        this.aluno = aluno;
    }
    
    public void atualizar(){
        String nome = view.getLbl_nome_altexc().getText();
        String usuario = view.getLbl_usuario_altexc().getText();
        String senha = view.getTxt_senha_altexc().getText();
        Aluno aluno = new Aluno(nome, usuario, senha);
        
        Conexao conexao = new Conexao();
        try{
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            dao.atualizar(aluno);
            JOptionPane.showMessageDialog(view,
                                              "Senha atualizada com sucesso!",
                                              "Atualização!",
                                              JOptionPane.INFORMATION_MESSAGE);
        } catch(SQLException e){
            JOptionPane.showMessageDialog(view,
                                              "Erro de conexão.",
                                              "ERRO!",
                                              JOptionPane.ERROR_MESSAGE);
        }
    }
    
    public void remover(){
        int option = JOptionPane.showConfirmDialog(view,
                                              "Deseja realmente excluir?",
                                              "Confirme",
                                              0);
        if(option != 1){
            Conexao conexao = new Conexao();
            try{
                Connection conn = conexao.getConnection();
                AlunoDAO dao = new AlunoDAO(conn);
                dao.remover(aluno);
                JOptionPane.showMessageDialog(view,
                                                  "Usuário removido com sucesso!",
                                                  "Remoção!",
                                                  JOptionPane.INFORMATION_MESSAGE);
            } catch(SQLException e){
                JOptionPane.showMessageDialog(view,
                                                  "Erro de conexão.",
                                                  "ERRO!",
                                                  JOptionPane.ERROR_MESSAGE);
            }
        }
    }
}
