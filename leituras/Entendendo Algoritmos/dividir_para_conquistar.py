print("Página 77 - atividades")

print(
"""
EXERCÍCIOS


""")

print("\n4.1 Escreva o código para a função soma, vista anteriormente.")
def soma(numbers):

    if len(numbers) == 0:
        return 0

    primeiro = numbers[0]
    resto = numbers[1:]

    return primeiro + soma(resto)

resposta = soma([2, 4, 6])
print(resposta)


print("\n4.2 Escreva uma função recursiva que conte o número de itens em uma lista.")

def contador_de_lista(lista):

    if len(lista) == 0:
        return 0
    
    first = lista[0]
    leftover = lista[1:]

    return 1 + contador_de_lista(leftover)


resultado = contador_de_lista([1,2,3,4,5])
print(resultado)

print("\n4.3 Encontre o valor mais alto de uma lista.")

def highest_number(numbers):
    if len(numbers) == 1:
        return numbers[0]
    
    first = numbers[0]
    leftover = numbers[1:]

    highest = highest_number(leftover)

    return first if first > highest else highest

result = highest_number([2, 5, 8, 10, 2])
print(result)

print("\n4.4 Você se lembra da pesquisa binária do Capítulo 1? Ela também é um algoritmo do tipo dividir para conquistar." 
      " Você Consegue determinar o caso-base e o caso recursivo para a pesquisa binária?")