// Ex05: Manipulação de Ponteiros em String
// Implemente uma função que recebe uma string como entrada e retorna a mesma string, mas com todas as letras convertidas para maiúsculas. Use ponteiros para percorrer a string.

#include <stdio.h>

char converte_maiuscula(char *str){
	while (*str){
  		if (*str >= 'a' && *str <= 'z') {
            *str = *str - 32;
        }
        str++;
	}
}

int main(int argc, char* argv[])
{
	char *s;
	printf("Digite uma string com letras minusculas: ");
    scanf("%s",s);
	printf("Antes da conversao: %s\n", s);

	converte_maiuscula(s);
	printf("Depois da conversao: %s", s);

	return 0;
}