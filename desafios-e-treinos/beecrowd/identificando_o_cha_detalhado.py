"""
Identificando o Chá - 2006
Por Inês Kereki UY Uruguay

Timelimit: 1
Degustação de chá às escuras é a habilidade de identificar um chá usando apenas seus sentidos do olfato e paladar.

Isto faz parte da Competição Ideal de Consumidores de Chá Puro (da sigla em inglês ICPC), que um programa de TV local está organizando. Durante o show, um bule de chá completo é preparado e são entregues uma xícara de chá para cada um dos cinco competidores. Os participantes devem cheirar, saborear e avaliar a amostra, de modo a identificar o tipo de chá, que pode ser: (1) o chá branco; (2) chá verde; (3) chá preto; ou (4) chá de ervas. No final, as respostas são verificadas para determinar o número de suposições corretas.

Dado o tipo de chá real e as respostas fornecidas, determinar o número de participantes que receberam a resposta correta.

Entrada
A primeira linha contém um inteiro T representando o tipo de chá (1 ≤ T ≤ 4). A segunda linha contém cinco inteiros A, B, C, D e E, que indica a resposta dada por cada competidor (1 ≤ A, B, C, D, E ≤ 4).

Saída
A saída contém um inteiro representando o número de concorrentes que obtiveram a resposta correta. 
"""

#entradas

while True:
    try:
        T = int(input("Número do chá real: "))
        if 1 <= T <= 4:
            break
        print("número do chá incorreto, valores de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

# repostas dos participantes

while True:
    try:
        A = int(input("Resposta do participante A: "))
        if 1 <= A <= 4: 
            break
        print("números de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

while True:
    try:
        B = int(input("Resposta do participante B: ")) 
        if 1 <= B <= 4:
            break
        print("número de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

while True:
    try:
        C = int(input("Resposta do participante C: "))
        if 1 <= C <= 4:
           break
        print("número de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

while True:
    try:
        D = int(input("Resposta do participante D: "))
        if 1 <= D <= 4:
            break
        print("número de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

while True:
    try:
        E = int(input("Resposta do participante E: "))
        if 1 <= E <= 4:
            break
        print("número de 1 à 4!")
    except ValueError:
        print("Aceito apenas números, de 1 à 4!")

#Saídas

participantes = [A, B, C, D, E]
i = 0

for participante in participantes:
    if participante == T:
        i += 1

print(i)