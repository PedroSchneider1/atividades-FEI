// Ex06: Leitura e Escrita de Registros em Arquivos Binários
/*
Desenvolva um programa que cria e manipula um arquivo binário para armazenar registros de funcionários.
Cada registro deve conter nome, idade e salário. Permita ao usuário adicionar novos registros, listar todos os registros e buscar por registros específicos pelo nome.
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char nome[255];
    int idade;
    float salario;
} Registro;

void escreve_novo_registro() {
    FILE *fptr;
    Registro novo;

    fptr = fopen("registros.bin", "ab");
    if (fptr == NULL) {
        printf("Erro ao abrir arquivo.\n");
        exit(1);
    }

    printf("Digite um novo registro (nome, idade, salario): ");
    fgets(novo.nome, sizeof(novo.nome), stdin);
    novo.nome[strcspn(novo.nome, "\n")] = '\0'; // Remove \n
    scanf("%d %f", &novo.idade, &novo.salario);
    getchar(); // Limpa o buffer do stdin

    if (fwrite(&novo, sizeof(Registro), 1, fptr) != 1) {
        printf("Erro ao escrever no arquivo.\n");
    }

    fclose(fptr);
}

void lista_todos_registros() {
    FILE *fptr;
    Registro r;

    fptr = fopen("registros.bin", "rb");
    if (fptr == NULL) {
        printf("Erro ao abrir arquivo.\n");
        exit(1);
    }

    while (fread(&r, sizeof(Registro), 1, fptr) == 1) {
        printf("Nome: %s\n", r.nome);
        printf("Idade: %d\n", r.idade);
        printf("Salario: %.2f\n", r.salario);
        printf("==============================\n");
    }

    fclose(fptr);
}

void busca_nome(char *nome_busca) {
    FILE *fptr;
    Registro r;
    int found = 0;

    fptr = fopen("registros.bin", "rb");
    if (fptr == NULL) {
        printf("Erro ao abrir arquivo.\n");
        exit(1);
    }

    while (fread(&r, sizeof(Registro), 1, fptr) == 1) {
        if (strcasecmp(nome_busca, r.nome) == 0) {
            printf("\nNome: %s\n", r.nome);
            printf("Idade: %d\n", r.idade);
            printf("Salario: %.2f\n", r.salario);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("\nRegistro nao encontrado.\n");
    }

    fclose(fptr);
}

int main() {
    int opcao;
    char nome_busca[50];

    do {
        printf("Escolha uma opcao:\n");
        printf("1. Adicionar novo registro\n");
        printf("2. Listar todos os registros\n");
        printf("3. Buscar registro por nome\n");
        printf("4. Sair\n");
        printf("Opcao: ");
        scanf("%d", &opcao);
        getchar(); // Limpa o buffer do stdin

        switch (opcao) {
            case 1:
                escreve_novo_registro();
                break;
            case 2:
                lista_todos_registros();
                break;
            case 3:
                printf("Digite o nome a ser buscado: ");
                fgets(nome_busca, sizeof(nome_busca), stdin);
                nome_busca[strcspn(nome_busca, "\n")] = '\0'; // Remove \n
                busca_nome(nome_busca);
                break;
            case 4:
                return 0;
            default:
                printf("Opcao invalida!\n");
        }
        printf("\n");
    } while (opcao != 4);

    return 0;
}