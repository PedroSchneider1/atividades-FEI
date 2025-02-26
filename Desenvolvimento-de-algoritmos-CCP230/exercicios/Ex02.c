// Ex02: Manipulação de Strings
// Desenvolva um programa que recebe uma string do usuário e conta o número de vogais nela.

#include <stdio.h>

int main(int argc, char* argv[])
{
    char str[15];
    int soma = 0;

    printf("Digite uma string de ate 15 letras: ");
    fgets(str, 15, stdin);

    for(int i = 0; str[i] != '\0'; i++){
        if (str[i] == 'a' || str[i] == 'A' || str[i] == 'e' || str[i] == 'E' ||
        str[i] == 'i' || str[i] == 'I' || str[i] == 'o' || str[i] == 'o' ||
        str[i] == 'u' || str[i] == 'U')
            soma++;
    }

    printf("%i", soma);

	return 0;
}