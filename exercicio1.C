#include <stdio.h>

float lerCelsius() {
    float celsius;
    printf("Digite a temperatura em Celsius: ");
    scanf("%f", &celsius);
    return celsius;
}
float calcularFahrenheit(float celsius) {
    return (celsius * 9 / 5) + 32;
}

float calcularKelvin(float celsius) {
    return celsius + 273.15;
}

void imprimirTemperatura(float celsius, float fahrenheit, float kelvin) {
        printf("%2f Celsius é igual a:\n%.2f Fahrenheit\n%.2f Kelvin\n", celsius, fahrenheit, kelvin);
}

int main() {
    float celsius, fahrenheit, kelvin;

    celsius = lerCelsius();
    fahrenheit = calcularFahrenheit(celsius);
    kelvin = calcularKelvin(celsius);
    imprimirTemperatura(celsius, fahrenheit, kelvin);
    

    return 0;
}