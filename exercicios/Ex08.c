// Ex08: Manipulação de Ponteiros
// Implemente uma função que recebe um array e seu tamanho como argumentos e retorna um novo array invertido, utilizando ponteiros.

#include <stdio.h>

int inverter(int *array, int n){
	int *comeco = array;
	int *fim = array + (n-1);
	int temp;

	while(comeco < fim){
		temp = *comeco;
		*comeco = *fim;
		*fim = temp;

		comeco++;
		fim--;
	}
	printf("\n");
}

int main(int argc, char* argv[])
{
	int array[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
	int n = sizeof(array) / sizeof(array[0]);

	printf("Antes de inverter:  ");
	for(int i = 0; i < n; i++){
		printf("%2d ", array[i]);
	}

	inverter(array, n);

	printf("Depois de inverter: ");
	for(int i = 0; i < n; i++){
		printf("%2d ", array[i]);
	}
	
	return 0;
}