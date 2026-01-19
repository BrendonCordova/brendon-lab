import random
lista_maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWYZ'
lista_minusculo = 'abcdefghijklmnopqrstuvwyz'
lista_caracteres_especiais = '.,/!@#$%&*(-_=+)'
lista_numeros = '0123456789'
todos_caracteres = 'ABCDEFGHIJKLMNOPQRSTUVWYZabcdefghijklmnopqrstuvwyz.,/!@#$%&*(-_=+)0123456789'
def gerador_de_senha():

    senha = [
        random.choice(lista_maiusculo),
        random.choice(lista_minusculo),
        random.choice(lista_caracteres_especiais),
        random.choice(lista_numeros)
    ]
    
    senha.extend(random.choices(todos_caracteres, k=8))
    
    random.shuffle(senha)
    
    return ''.join(senha)

print(f'Senha gerada: {gerador_de_senha()}')