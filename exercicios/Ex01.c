// Ex01: Soma de Elementos em um Array
// Crie um programa que solicita ao usuário inserir elementos em um array e calcule a soma desses elementos.

#include <stdio.h>

int main(int argc, char* argv[])
{
    int array[10], soma;

	printf("Digite 10 elementos: ");

    for(int i=0; i<10; i++){
        scanf("%i", &array[i]);
    }

    soma = 0;
    for(int i=0; i<10; i++){
        soma += array[i];
    }

    printf("Soma final: %i", soma);

	return 0;
}