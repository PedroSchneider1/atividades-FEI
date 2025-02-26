// Ex09: Cálculo de Estatísticas em um Array
// Escreva um programa que recebe um array de números e calcula a média, mediana e moda dos elementos.

#include <stdio.h>
#include <stdlib.h>

int* aloca(int n){
	int* a;
	a = malloc(n * sizeof(int));
	
	if (a == NULL) {
		printf("Memoria nao alocada.\n");
		exit(0);
	}

	return a;
}

float media(int* array, int n){
	float media;
	int sum = 0;

    for (int i = 0; i < n; i++) {
        sum += array[i];
    }
    
	media = (float)sum/n;
	
	return media;
}

void mediana(int* array, int n){
	float mediana;
	if (n % 2 != 0){
		mediana = array[(n/2)];
	}
	else{
		mediana = ((array[(n/2)-1] + array[(n/2)]) / 2.0);
	}

	printf("\nMediana: %.2f", mediana);
}

void moda(int* array, int n){
	int* frequencia = (int*)calloc(n+1, sizeof(int));
	int freq_max = 0;

	// Conta a frequencia de cada elemento
	for (int i = 0; i < n; i++) {
		frequencia[array[i]]++;
		if (frequencia[array[i]] > freq_max) {
			freq_max = frequencia[array[i]];
		}
	}

	// Coleta todas as modas
	int* moda = (int*)malloc(n * sizeof(int));
	int conta_moda = 0;

	for (int i = 0; i < n; i++) {
		// Checa se o numero é a frequencia maxima encontrada (se nao for, nao pode ser uma moda)
		if (frequencia[array[i]] == freq_max) {
			// Checa se ja foi adicionado
			int ja_add = 0;

			for (int j = 0; j < conta_moda; j++) {
				if (moda[j] == array[i]) {
					ja_add = 1;
					break;
				}
			}
			if (!ja_add) {
				moda[conta_moda++] = array[i];
			}
		}
	}

	// Printa a moda
	if (conta_moda == n) {
		printf("\nModa:    Nao existe\n");
	} else {
		printf("\nModa:    ");
		for (int i = 0; i < conta_moda; i++) {
			printf("%d ", moda[i]);
		}
		printf("\n");
	}

	free(frequencia);
	free(moda);
}

int main(int argc, char* argv[])
{
	int n;
	printf("Digite o tamanho do array: ");
	scanf("%i", &n);
	getchar();

	int* array = aloca(n);

	printf("Preencha o array com %i numeros: \n", n);
	for(int i = 0; i < n; i++){
		scanf("%i", &array[i]);
	}

	printf("Array:   ");
	for(int i = 0; i < n; i++){
		printf("%i ", array[i]);
	}

	float m = media(array, n);
	printf("\nMedia:   %.2f", m);

	mediana(array, n);
	moda(array, n);

	return 0;
}