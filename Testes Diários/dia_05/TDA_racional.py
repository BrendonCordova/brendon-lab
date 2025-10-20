"""
TDA Racional - 1022
Por Neilor Tonin, URI  Brasil

Timelimit: 1
A tarefa aqui neste problema é ler uma expressão matemática na forma de dois números Racionais (numerador / denominador) e apresentar o resultado da operação. Cada operando ou operador é separado por um espaço em branco. A sequência de cada linha que contém a expressão a ser lida é: número, caractere, número, caractere, número, caractere, número. A resposta deverá ser apresentada e posteriormente simplificada. Deverá então ser apresentado o sinal de igualdade e em seguida a resposta simplificada. No caso de não ser possível uma simplificação, deve ser apresentada a mesma resposta após o sinal de igualdade.

Considerando N1 e D1 como numerador e denominador da primeira fração, segue a orientação de como deverá ser realizada cada uma das operações:
Soma: (N1*D2 + N2*D1) / (D1*D2)
Subtração: (N1*D2 - N2*D1) / (D1*D2)
Multiplicação: (N1*N2) / (D1*D2)
Divisão: (N1/D1) / (N2/D2), ou seja (N1*D2)/(N2*D1)

Entrada
A entrada contem vários casos de teste. A primeira linha de cada caso de teste contem um inteiro N (1 ≤ N ≤ 1*104), indicando a quantidade de casos de teste que devem ser lidos logo a seguir. Cada caso de teste contém um valor racional X (1 ≤ X ≤ 1000), uma operação (-, +, * ou /) e outro valor racional Y (1 ≤ Y ≤ 1000).

Saída
A saída consiste em um valor racional, seguido de um sinal de igualdade e outro valor racional, que é a simplificação do primeiro valor. No caso do primeiro valor não poder ser simplificado, o mesmo deve ser repetido após o sinal de igualdade.
"""

import sys
from fractions import Fraction

# entrada de dados

N = int(sys.stdin.readline())

for i in range(N):

    n1, barra1, d1, operador, n2, barra2,  d2 = sys.stdin.readline().split()

    n1, n2 , d1, d2 = map(int, [n1, n2, d1, d2])

    # validação / conta / saída de dados

    if operador == "+":
        numerador = (n1 * d2 + n2 * d1)
        denominador = (d1 * d2)
        simplificado = Fraction(numerador, denominador)
        print(f"{numerador}/{denominador} = {simplificado.numerator}/{simplificado.denominator}")

    elif operador == "-":
        numerador = (n1 * d2 - n2 * d1)
        denominador = (d1 * d2)
        simplificado = Fraction(numerador, denominador)
        print(f"{numerador}/{denominador} = {simplificado.numerator}/{simplificado.denominator}")



    elif operador == "*":
        numerador = n1 * n2
        denominador = d1 * d2
        simplificado = Fraction(numerador, denominador)
        print(f"{numerador}/{denominador} = {simplificado.numerator}/{simplificado.denominator}")


    else:
        numerador = n1 * d2
        denominador = n2 * d1
        simplificado = Fraction(numerador, denominador)
        print(f"{numerador}/{denominador} = {simplificado.numerator}/{simplificado.denominator}")

# só tenho a agradecer pela função Fraction, que função incrível!!