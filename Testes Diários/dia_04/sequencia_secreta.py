"""
beecrowd | 3048
Sequência Secreta
Por BR Brazil

Timelimit: 1
Na calçada em frente ao Palácio Imperial, não se sabe a razão, existe uma sequência de N números desenhados no chão. A sequência tem a seguinte forma: ela começa e termina com o número 1; apenas os números 1 e 2 aparecem nela; e o número 2 aparece pelo menos uma vez. Veja um exemplo na coluna (a) da figura ao lado. Ninguém sabe o significado da sequência e, justamente por isso, várias teorias malucas surgiram. Uma delas diz que a sequência representa, na verdade, apenas um valor que estaria relacionado a um segredo dos imperadores. Esse valor é a quantidade máxima de números da sequência que poderiam ser marcados com um círculo, de modo que a sequência de números marcados não contenha dois números iguais consecutivos. A coluna (b) da figura ao lado ilustra uma sequência de 4 números marcados que obedece a restrição acima. Só que é possível marcar 7 números, como mostra a coluna (c) da figura.

Neste problema, dada a sequência original de números desenhados no chão da calçada, seu programa deve computar e imprimir a quantidade máxima de números da sequência que poderiam ser marcados com um círculo sem que haja dois números iguais consecutivos na sequência marcada.
"""

import sys

N = int(sys.stdin.readline())

sequencia = []
sequencia_dif = 1

for i in range(N):
    
    V = int(sys.stdin.readline())

    sequencia.append(V)


    # saída
    
for i in range(len(sequencia) - 1):
    if sequencia[i] != sequencia[i+1]:
        sequencia_dif += 1

print(sequencia_dif)