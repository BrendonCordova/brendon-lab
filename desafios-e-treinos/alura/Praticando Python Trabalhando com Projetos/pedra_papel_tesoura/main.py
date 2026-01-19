import random

# def escolha_adversario():
#     opcoes = ['Pedra', 'Papel', 'Tesoura']
#     adversario = random.choice(opcoes)

#     return f'Computador escolheu {adversario}'


def pedra_papel_tesoura():
    opcoes = ['pedra', 'papel', 'tesoura']
    adversario = random.choice(opcoes)
    escolha = input('Escolha entre pedra, papel e tesoura: ').lower()

    if escolha not in opcoes:
        print('Escolha inválida')
        return
    
    print(f'Computador escolheu: {adversario}')

    if escolha == adversario:
        print('Empate!')
    elif (
        (escolha == 'pedra' and adversario == 'tesoura') or
        (escolha == 'tesoura' and adversario == 'papel') or
        (escolha == 'papel' and adversario == 'pedra')
    ):
        print('Você venceu!')
    else:
        print('Você perdeu!')


    # Feito Anteriormente - funciona, mas muito enrolado

    # if escolha == 'Pedra':

    #     match adversario:

    #         case 'Papel':
    #             print(f'Computador escolheu {adversario}\n Você perdeu!')
    #         case 'Tesoura':
    #             print(f'Computador escolheu {adversario}\n Você venceu!')
    #         case _:
    #             print(f'Computador escolheu {adversario}\n Empate!')
    # elif escolha == 'Papel':

    #     match adversario:

    #         case 'Tesoura':
    #             print(f'Computador escolheu {adversario}\n Você perdeu!')
    #         case 'Pedra':
    #             print(f'Computador escolheu {adversario}\n Você venceu!')
    #         case _:
    #             print(f'Computador escolheu {adversario}\n Empate!')
    # else:
    #     match adversario:

    #         case 'Pedra':
    #             print(f'Computador escolheu {adversario}\n Você perdeu!')
    #         case 'Papel':
    #             print(f'Computador escolheu {adversario}\n Você venceu!')
    #         case _:
    #             print(f'Computador escolheu {adversario}\n Empate!')

pedra_papel_tesoura()