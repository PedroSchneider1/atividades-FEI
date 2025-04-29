/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Controller;

import DAO.AlunoDAO;
import DAO.Conexao;
import Model.Aluno;
import View.AltExcFrame;
import View.LoginFrame;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.SQLException;
import javax.swing.JOptionPane;

/**
 *
 * @author unifpschneider
 */
public class ControllerLogin {
    private LoginFrame view;

    public ControllerLogin(LoginFrame view) {
        this.view = view;
    }
    
    public void loginAluno(){
        Aluno aluno = new Aluno(null,
                                view.getTxt_usuario_login().getText(),
                                view.getTxt_senha_login().getText());
        Conexao conexao = new Conexao();
        try{
            Connection conn = conexao.getConnection();
            AlunoDAO dao = new AlunoDAO(conn);
            ResultSet res = dao.consultar(aluno);
            if(res.next()){
                JOptionPane.showMessageDialog(view,
                                              "Login efetuado com sucesso!",
                                              "Aviso!",
                                              JOptionPane.INFORMATION_MESSAGE);
                String nome = res.getString("nome");
                String usuario = res.getString("usuario");
                Aluno alunoLogado = new Aluno(nome, usuario, null);
                AltExcFrame aec = new AltExcFrame(alunoLogado);
                aec.setVisible(true);
                view.setVisible(false);
            }
            else{
                JOptionPane.showMessageDialog(view,
                                              "Login NÃO efetuado!",
                                              "Aviso!",
                                              JOptionPane.ERROR_MESSAGE);
            }
        } catch(SQLException e){
            JOptionPane.showMessageDialog(view,
                                              "Erro de conexão.",
                                              "ERRO!",
                                              JOptionPane.ERROR_MESSAGE);
        }
    }
}
