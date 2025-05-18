#include <stdio.h>
#include <stdbool.h>

short lerOpcao() {
    int opcao;
    printf("Escolha uma opçao: \n");
    printf("1, Converter para MPH");
    printf("2. Converter para KPH");
    return opcao;
}

bool validarOpcao(short opcao) {
    return (opcao == 1 || opcao ==2 );
}

bool validarVelocidade(float velocidade) {
    return velocidade >=0;
}

float lerVelocidade() {
    float velocidade;
    printf("Digite a velocidade:");
    scanf("%f", &velocidade);
    return velocidade;
}

float converterParaMPH(float velocidade) {
    return velocidade * 0.621371;
}

float converterParaKPH(float velocidade) {
    return velocidade * 1.60934;
}

void imprimirVelocidadeConvertida(float velocidadadeLida, float velocidadeConvertida, short opcao) {
    if (opcao ==1) {
        printf("%.2f KPH é igual a %.2f MPH\n", velocidadadeLida, velocidadeConvertida);
    }
    else {
        printf("%.2f  MPH é igual a %.2f KPH\n", velocidadadeLida, velocidadeConvertida);
    }
}

int main() {

    short opcao = lerOpcao();
    if (validarOpcao(opcao) == false) {
        printf("Opção inválida!\n");
        return 1;
    }

    float velocidadeLida = lerVelocidade();
    float velocidadeConvertida;
    if (opcao ==1) {
        velocidadeConvertida = converterParaMPH(velocidadeLida);
    }
    else {
        velocidadeConvertida = converterParaKPH(velocidadeLida);
    }
    imprimirVelocidadeConvertida(velocidadeLida, velocidadeConvertida, opcao);

    return 0;
}