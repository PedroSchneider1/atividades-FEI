// Ex10: Manipulação de Tempo
// Utilize a biblioteca time.h para calcular o tempo que um determinado trecho de código leva para ser executado.

#include <stdio.h>
#include <time.h>

long long int fatorial(long long int a){
	long long int result = 1;
	while(a > 1){
		result *= a;
		a--;
	}
	return result;
}

int main(int argc, char* argv[])
{
	clock_t tempo_req;
	float tempo_exec;

	// Inicia a contagem do tempo
	tempo_req = clock();

	// Codigo a ser medido
	long long int n = 10000000;
	long long int fat = fatorial(n);

	tempo_req = clock() - tempo_req;

	// Calculate the execution time in seconds
	tempo_exec = (float)(tempo_req) / CLOCKS_PER_SEC;

	printf("Tempo de execucao: %.6f segundos\n", tempo_exec);

    return 0;
}