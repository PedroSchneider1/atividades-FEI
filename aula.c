#include <stdio.h>
#include <stdlib.h>

int soma(int a, int b) { return a + b; }
int subtrai(int a, int b) { return a - b; }

void imprime_valor(void *ptr, char tipo) {
    if (tipo == 'i')
        printf("Valor int: %d\n", *((int *)ptr));
    else if (tipo == 'f')
        printf("Valor float: %.2f\n", *((float *)ptr));
}

// Função de comparação para inteiros
int compara_inteiros(const void *a, const void *b) { return (*(int *)a - *(int *)b); }

int main()
{
    // Ponteiro de funções

    /*
    int (*ptr_func)(int, int) = soma;
    int resultado = ptr_func(2,3);
    printf("Resultado: %i", resultado);
    */

    /*
    int (*operacoes[])(int, int) = {soma, subtrai};

    printf("Resultado soma: %i\n", operacoes[0](5,2));
    printf("Resultado subtrai: %i\n", operacoes[1](5,2));
    */

    // =============================

    // Ponteiros de void
    
    /*
    void *ptr;
    int x = 10;
    ptr = &x;
    int *int_ptr = (int *)ptr;

    printf("Valor de x: %i\n", *int_ptr);

    imprime_valor(ptr, 'i');
    */

    int arr[] = {5, 2, 9, 1, 5, 6};
    int n = sizeof(arr) / sizeof(arr[0]);

    // Ordenando o array usando qsort
    qsort(arr, n, sizeof(int), compara_inteiros);
    // Exibindo o array ordenado
    for (int i = 0; i < n; i++) {
    printf("%d ", arr[i]);
    }
    printf("\n");
    return 0;
}
