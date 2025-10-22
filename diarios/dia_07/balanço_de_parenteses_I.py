"""
Balanço de Parênteses I - 1068
Por Neilor Tonin, URI  Brasil

Timelimit: 1
Dada uma expressão qualquer com parênteses, indique se a quantidade de parênteses está correta ou não, sem levar em conta o restante da expressão. Por exemplo:

a+(b*c)-2-a        está correto
(a+b*(2-c)-2+a)*2  está correto

enquanto

(a*b-(2+c)         está incorreto
2*(3-a))           está incorreto
)3+b*(2-c)(        está incorreto

Ou seja, todo parênteses que fecha deve ter um outro parênteses que abre correspondente e não pode haver parênteses que fecha sem um previo parenteses que abre e a quantidade total de parenteses que abre e fecha deve ser igual.

Entrada
Como entrada, haverá N expressões (1 <= N <= 10000), cada uma delas com até 1000 caracteres.

Saída
O arquivo de saída deverá ter a quantidade de linhas correspondente ao arquivo de entrada, cada uma delas contendo as palavras correct ou incorrect de acordo com as regras acima fornecidas.
"""

import sys

N = int(sys.stdin.readline())

for i in range(N):

    expressoes = sys.stdin.readline().strip()
    parenteses = 0

    for expressao in expressoes:

        if expressao == ")":
            parenteses -= 1
            if parenteses < 0:
                break

        elif expressao == "(":
            parenteses += 1
    
    if parenteses == 0:
        print("correct")

    else:
        print("incorrect")

# se for == 0, então está equilibrado, porém se antes ele ficar negativo já quebra, porém com o break
# ali, ele simplesmente quebra e joga para onde irá verificar novamente, por isso rever... agora vou pra aula!!