// Ex07: Ordenação de Structs
// Crie um programa que ordena um array de structs com base em um dos campos (por exemplo, idade) usando qsort da biblioteca glibc.

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    int id;
    char nome[255];
    int idade;
    float altura;
} Cadastro;

typedef enum {
    SORT_ID,
    SORT_IDADE,
    SORT_ALTURA
} SortParametro;

SortParametro criterio;

int comparar(const void *p, const void *q) {
    const Cadastro *a = (const Cadastro *)p;
    const Cadastro *b = (const Cadastro *)q;

    switch (criterio) {
        case SORT_ID:
            return (a->id - b->id);
        case SORT_IDADE:
            return (a->idade - b->idade);
        case SORT_ALTURA:
            return (a->altura > b->altura) - (a->altura < b->altura);
        default:
            return 0;
    }
}

int main(int argc, char* argv[]) {
    if (argc != 2) {
        printf("sort_parametros: id, idade, altura\n");
        return 1;
    }

    if (strcmp(argv[1], "id") == 0) {
        criterio = SORT_ID;
    } else if (strcmp(argv[1], "idade") == 0) {
        criterio = SORT_IDADE;
    } else if (strcmp(argv[1], "altura") == 0) {
        criterio = SORT_ALTURA;
    } else {
        printf("Parametro invalido. Use: id, idade ou altura\n");
        return 1;
    }

	int x;
	printf("Digite o numero de cadastros a serem organizados por %s: ", argv[1]);
	scanf("%i",&x);
	getchar();
    Cadastro novo[x];

	for(int i = 0; i < x; i++){
		novo[i].id = i;
		printf("Nome: ");
		fgets(novo[i].nome, 255, stdin);
    	novo[i].nome[strcspn(novo[i].nome, "\n")] = '\0'; // Remove \n

		printf("Idade: ");
		scanf("%i", &novo[i].idade);
		getchar();

		printf("Altura: ");
		scanf("%f", &novo[i].altura);
		getchar();
		
		printf("\n");
	}

    qsort(novo, x, sizeof(Cadastro), comparar);

    printf("Sorted array: \n");
    for (int i = 0; i < x; i++) {
		printf("ID:[%2i] | ", novo[i].id);
        printf("Nome: %-10s ", novo[i].nome);
        printf("Idade: %3i ", novo[i].idade);
        printf("Altura: %3.2f ", novo[i].altura);
		printf("\n");
    }

    return 0;
}
