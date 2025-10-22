"""
LED - 1168
Autor Desconhecido
Timelimit: 1
João quer montar um painel de leds contendo diversos números. Ele não possui muitos leds, e não tem certeza se conseguirá montar o número desejado. Considerando a configuração dos leds dos números abaixo, faça um algoritmo que ajude João a descobrir a quantidade de leds necessário para montar o valor.

Obs.: Para programadores de Javascript, recomenda-se o uso de "input.trim().split('\n')" para evitar erros conhecidos.




Entrada
A entrada contém um inteiro N, (1 ≤ N ≤ 1000) correspondente ao número de casos de teste, seguido de N linhas, cada linha contendo um número (1 ≤ V ≤ 10100) correspondente ao valor que João quer montar com os leds.

Saída
Para cada caso de teste, imprima uma linha contendo o número de leds que João precisa para montar o valor desejado, seguido da palavra "leds".
"""

import sys

N = int(sys.stdin.readline())

for i in range(N):

    numeros = 0
    quantidade_led = 0

    numeros = sys.stdin.readline().strip()

    for numero in numeros:

        if numero == "1":
            quantidade_led += 2

        elif numero == "2":
            quantidade_led += 5

        elif numero == "3":
            quantidade_led += 5

        elif numero == "4":
            quantidade_led += 4

        elif numero == "5":
            quantidade_led += 5

        elif numero == "6":
            quantidade_led += 6

        elif numero == "7":
            quantidade_led += 3

        elif numero == "8":
            quantidade_led += 7

        elif numero == "9":
            quantidade_led += 6

        else:
            quantidade_led += 6

    print(f"{quantidade_led} leds")

"""
LEDS tem a composição:

1 = 2 leds
2 = 5 leds
3 = 5 leds
4 = 4 leds
5 = 5 leds
6 = 6 leds
7 = 3 leds
8 = 7 leds
9 = 6 leds
0 = 6 leds

"""