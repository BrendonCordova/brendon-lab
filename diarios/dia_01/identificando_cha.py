T = int(input())

A, B, C, D, E = map(int, input().split())

participantes = [A, B, C, D, E]
ganhadores = 0

for participante in participantes:
    if participante == T:
        ganhadores += 1

print(ganhadores)