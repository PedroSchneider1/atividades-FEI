// Ex04: Operações Matriciais
// Implemente funções para multiplicação de matrizes e transposição. Utilize ponteiros para alocar dinamicamente o espaço de memória.

#include <stdio.h>
#include <stdlib.h>

int** alloc_matriz(int n, int m){
	int **A;
	int i,j;

	// Aloca as linhas
	A = (int**)malloc(n * sizeof(int));
	// Checa se alocou corretamente
	if (A == NULL) {
		printf("Memoria nao alocada.\n");
		exit(0);
	}

	// Aloca as colunas pra cada linhas
	for(i = 0; i < n; i++){
		A[i] = (int*)malloc(m * sizeof(int));
		// Checa se alocou corretamente
		if (A[i] == NULL) {
			printf("Memoria nao alocada.\n");
			exit(0);
		}
	}

	printf("\n");
	return A;
}

void free_matriz(int **A, int n) {
	// Libera a memoria
    for (int i = 0; i < n; i++) {
        free(A[i]);
    }
    free(A);
}

void print_matriz(int **A, int n, int m){
	// Printa a matriz
	printf("Os elementos da matriz sao:\n");
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < m; j++) {
			printf("%5d ", A[i][j]);
		}
		printf("\n");
	}
}

void mult_matriz(int **A, int **B, int n, int m, int y){
	int **AB = alloc_matriz(n,y);

	// Multiplica as duas matrizes
	for(int i = 0; i < n; i++){
		for(int j = 0; j < y; j++){
			AB[i][j] = 0;
			for(int k = 0; k < m; k++){
				AB[i][j] += A[i][k]*B[k][j];
			}
		}
	}

	print_matriz(AB,n,y);

	free_matriz(AB,n);
}

int** transpor_matriz(int **A, int n, int m){
	int **At = alloc_matriz(m,n);
	
	// Transpoe a matriz A
	for(int i = 0; i < n; i++){
		for(int j = 0; j < m; j++){
			At[j][i] = A[i][j];
		}
	}

	print_matriz(At,m,n);

	free_matriz(At,n);
}

int main(int argc, char* argv[])
{
	char menu;
	int n,m,i,j;

	// Menu para operacao
	printf("Deseja realizar qual operacao?\na. Multiplicacao de matrizes\nb. Transpor uma matriz\n");
	scanf("%c",&menu);

	printf("\n");

	// Aloca matriz A (obrigatoria)
	printf("Digite o numero de linhas da matriz A (N): ");
	scanf("%i",&n);
	printf("Digite o numero de colunas da matriz A (M): ");
	scanf("%i",&m);

	int **A = alloc_matriz(n,m);

	// Inicializa a matriz
	printf("Digite os valores da matriz (NxM): \n");
	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			scanf("%i",&A[i][j]);
		}
	}

	print_matriz(A,n,m);

	if(menu == 'a'){
		// Aloca matriz B (necessaria para a operacao) e realiza operacao
		
		int x,y;

		printf("\nDigite o numero de linhas da matriz B (X): ");
		scanf("%i",&x);
		printf("Digite o numero de colunas da matriz B (Y): ");
		scanf("%i",&y);
		
		int **B = alloc_matriz(x,y);

		// Inicializa a matriz
		printf("Digite os valores da matriz (XxY): \n");
		for (i = 0; i < x; i++) {
			for (j = 0; j < y; j++) {
				scanf("%i",&B[i][j]);
			}
		}

		print_matriz(B,x,y);
		
		if(m == x){
			mult_matriz(A,B,n,m,y);
		}
		else{
			printf("Operacao impossivel.");
		}

		// Libera matriz B
		free_matriz(B,n);
	}
	else if(menu == 'b'){
		// Realiza operacao com matriz A
		transpor_matriz(A,n,m);
	}
	else{
		printf("Opcao invalida.");
	}

	// Libera matriz A
	free_matriz(A,n);

	return 0;
}