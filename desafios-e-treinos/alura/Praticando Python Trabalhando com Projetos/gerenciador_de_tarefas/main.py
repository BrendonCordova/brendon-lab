import os

def adicionar_tarefa():
    nome_tarefa = input('Digite a tarefa: ').strip()
    tarefas.append(nome_tarefa)
    print('Tarefa adicionada!')

def visualizar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        print('\nTarefas:')
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i}. {tarefa}')
        input()

def remover_tarefa():
    if not tarefas:
        print('Erro: Nenhuma tarefa para remover.')
        return
    
    try:
    
        numero_tarefa = int(input('Digite o número da tarefa a ser removida: '))
        if 0 <= numero_tarefa < len(tarefas):

            print(f'Tarefa "{tarefas[numero_tarefa-1]}" removida!')
            tarefas.remove(tarefas[numero_tarefa-1])
        else:
            print('Erro: Índice inválido! Digite um número válido.')
    except ValueError:
        print('Erro: Entrada inválida! Digite um número.')

def sair_gerenciador():
    os.system('cls')
    print('Saindo do gerenciador de tarefas. Até mais!')

def gerenciador_tarefas():
    opcoes = '''
1. Adicionar tarefa 
2. Visualizar tarefas 
3. Remover tarefa 
4. Sair '''

    while True:

        print(opcoes)

        try:
            escolha = int(input('Escolha uma opção: '))

            match escolha:

                case 1:
                    adicionar_tarefa()

                case 2:
                    visualizar_tarefas()

                case 3:
                    remover_tarefa()

                case 4:
                    return sair_gerenciador()
                
                case _:
                    print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')

        except ValueError:
            print('Erro: Opção inválida! Escolha uma opção entre 1 e 4.')

tarefas = []
gerenciador_tarefas()