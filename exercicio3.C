#include <stdio.h>
#include <stdlib.h>


int lerTamanhoArray(int n) {
    printf("Digite o tamanho do array: ");
    scanf("%d", &n);
    printf("Endereço do parâmetro de 'n' %p\n", &n);
    return n;
}

void lerTamanhoArrayPorReferencia(int* n) {
    printf("Digite o tamanho do array: ");
    scanf("%d", n);
    printf("Endereço do parâmetro de 'n': %p\n", n);

}

    // 1. ler um tamanho de array 'n';
    // 2. Criar um array de inteiros de tamanho 'n';
    // 3. preencher o array com números inteiros;
    // 4. ordenar o array em ordem crescente;
    // 5. imprimir o array.

int main() {
    int n;

    n = lerTamanhoArray(n);
    int* array = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        printf("Valor: %d\nEndereço: %p", array[i], &array[i]);
    }
    printf("\n");
    printf("Tamanho do Array: %d", sizeof(array));

    return 0;
}