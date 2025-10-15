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