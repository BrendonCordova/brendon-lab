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