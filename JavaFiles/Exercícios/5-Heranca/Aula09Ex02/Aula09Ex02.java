/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */

import Navios.Navio;
import Navios.NavioMercante;
import Navios.NavioDeGuerra;
import Navios.Cruzador;
import Navios.PortaAvioes;

/**
 *
 * @author unifpschneider
 */
public class Aula09Ex02 {

    public static void main(String[] args) {
        // Criando os objetos
        Navio navio = new Navio(100, "Navio Genérico");
        NavioMercante navioMercante = new NavioMercante(100, "Mercante Esperança", 200.5, 500);
        NavioDeGuerra navioDeGuerra = new NavioDeGuerra(500, "Guerra Invencível", 300.8, 5);
        Cruzador cruzador = new Cruzador(75, "Cruzador Relâmpago", 150.6, 8, 12);
        PortaAvioes portaAvioes = new PortaAvioes(50, "Porta Aviões Gigante", 400.0, 20, 15);

        // Exibindo as informações de maneira organizada
        System.out.println("=== INFORMAÇÕES DOS NAVIOS ===");
        System.out.println("NAVIO");
        navio.exibirInfoGeral();
        System.out.println();

        System.out.printf("\nNAVIO MERCANTE\n");
        navioMercante.carregamento();
        System.out.println();

        System.out.printf("\nNAVIO DE GUERRA\n");
        navioDeGuerra.exibirArmas();
        System.out.println();

        System.out.printf("\nCRUZADOR\n");
        cruzador.exibirArmas();
        System.out.println();

        System.out.printf("\nPORTA-AVIÕES\n");
        portaAvioes.exibirArmas();
        System.out.println();
    }
}
