// Ex03: Cadastro de Produtos usando Struct
/*  Crie uma estrutura de dados chamada "Produto" que armazena nome, preço e quantidade em estoque.
    Permita ao usuário cadastrar produtos, exibir as informações e calcular o valor total em estoque (preço * quantidade).
*/

#include <stdio.h>

typedef struct
{
    char nome[15];
    float preco;
    int qtt_estoque;
} Produto;

Produto produtos[15];
int i_produtos = 0;

void cadastrar_produto(){
    if(i_produtos < 15){
        printf("Digite o nome do produto: ");
        scanf("%s", produtos[i_produtos].nome);
        printf("Digite o preco do produto: ");
        scanf("%f", &produtos[i_produtos].preco);
        printf("Digite a quantidade em estoque: ");
        scanf("%d", &produtos[i_produtos].qtt_estoque);
        printf("Nome: %s\tPreco: %.2f\tQuantidade: %d\n", produtos[i_produtos].nome, produtos[i_produtos].preco, produtos[i_produtos].qtt_estoque);
        i_produtos++;
    }
    else{
        printf("Limite de produtos atingidos.\n");
    }
}

void exibir_info(){
    for(int i=0; i < i_produtos; i++){
        printf("%i. Nome: %s\tPreco: %.2f\tQuantidade: %d\n", i+1, produtos[i].nome, produtos[i].preco, produtos[i].qtt_estoque);
    }
}

float calcular_valor_estoque(int selec){
    float valor_total = 0.0;
    if(selec <= 0){
        for (int i = 0; i < i_produtos; i++) {
            valor_total += produtos[i].preco * produtos[i].qtt_estoque;
        }
        return valor_total;
    }
        valor_total = produtos[selec-1].preco * produtos[selec-1].qtt_estoque;
        return valor_total;
}

int main(int argc, char* argv[])
{
    char menu;
    int selec_produto = 0;
    float valor_estoque = 0;
    
    do{
        printf("\n===CADASTRO DE PRODUTOS USANDO STRUCT===\n");
        printf("a. Cadastrar produto (max. 15)\nb. Exibir informacoes\nc. Calcular valor total em estoque\nx. Sair\n");
        scanf(" %c", &menu);

        switch (menu)
        {
        case 'a':
            cadastrar_produto();
            break;
        case 'b':
            exibir_info();
            break;
        case 'c':
            printf("Escolha o produto a ser calculado: \n");
            exibir_info();
            printf("(Ou digite '0' para calcular o valor do estoque total)\n");
            scanf("%i", &selec_produto);
            valor_estoque = calcular_valor_estoque(selec_produto);
            printf("R$%.2f\n", valor_estoque);
            break;
        case 'x':
            break;
        default:
            printf("Opcao invalida.");
            break;
        }
    }while(menu != 'x');

    return 0;
}
