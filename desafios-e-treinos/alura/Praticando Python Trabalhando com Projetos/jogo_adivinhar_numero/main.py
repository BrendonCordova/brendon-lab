import random

def adivinhe_numero():
    
    numero_sorteado = random.randint(1,100)
   
    while True:

        try:
            escolha = int(input('Tente adivinhar o número de (1-100): '))

            if not 0 <= escolha <= 100:
                raise ValueError("Número fora do intervalo! Digite um número entre 1 e 100.")

            if escolha == numero_sorteado:
                print(f'Parabéns! Você acertou o número {numero_sorteado}.')
                return

            if escolha > numero_sorteado:
                print('Muito alto! Tente novamente')
            else:
                print('Muito baixo! Tente novamente')


        except ValueError as e:
            print(f'Entrada inválida: {e}')
            
adivinhe_numero()