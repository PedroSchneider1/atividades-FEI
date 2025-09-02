/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package DAO;

import Model.Aluno;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.sql.ResultSet;

/**
 *
 * @author unifpschneider
 */
public class AlunoDAO {
    private Connection conn;

    public AlunoDAO(Connection conn) {
        this.conn = conn;
    }
    
    public ResultSet consultar(Aluno aluno) throws SQLException{
        // String que da brecha pra SQL injection
        // String sql = "SELECT * FROM aluno WHERE usuario='"
        //              + aluno.getUsuario() + "' AND senha='"
        //              + aluno.getSenha() + "'";
        String sql = "SELECT * FROM aluno WHERE usuario=? AND senha=?";
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, aluno.getUsuario());
        statement.setString(2, aluno.getSenha());
        statement.execute();
        ResultSet resultado = statement.getResultSet();
        return resultado;
    }
    
    public void inserir(Aluno aluno) throws SQLException{
        String sql = "INSERT INTO aluno (nome, usuario, senha) values ('"
                   + aluno.getNome()    + "','"
                   + aluno.getUsuario() + "','"
                   + aluno.getSenha()   + "')";
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.execute();
        conn.close();
    }
    
    public void atualizar(Aluno aluno) throws SQLException{
        String sql = "UPDATE aluno SET senha=? WHERE usuario=?";
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, aluno.getSenha());
        statement.setString(2, aluno.getUsuario());
        statement.execute();
        conn.close();
    }
    
    public void remover(Aluno aluno) throws SQLException{
        String sql = "DELETE FROM aluno WHERE usuario=?";
        PreparedStatement statement = conn.prepareStatement(sql);
        statement.setString(1, aluno.getUsuario());
        statement.execute();
        conn.close();
    }

}
