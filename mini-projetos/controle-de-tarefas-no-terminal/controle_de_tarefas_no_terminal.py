import os
import json

def exibir_nome():
    print('''
█▀▀ █▀█ █▄ █ ▀█▀ █▀█ █▀█ █   █▀▀   █▀▄ █▀▀   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█ █▀
█▄▄ █▄█ █ ▀█  █  █▀▄ █▄█ █▄▄ ██▄   █▄▀ ██▄    █  █▀█ █▀▄ ██▄ █▀  █▀█ ▄█
''')
    
def exibir_subtitulo(subtitulo):
    print(subtitulo)

def redirecionar_menu():
    print('Para voltar ao menu principal, aperte uma tecla')
    input()
    main()

def opcoes():
    print('1 - Criar Tarefas')
    print('2 - Listar Tarefas')
    print('3 - Alterar Título da Tarefa')
    print('4 - Alterar Status da Tarefa')
    print('5 - Sair')

def criar_tarefa():
    titulo = input('Digite o título da sua tarefa: ')
    status = input('Digite o status da sua tarefa (pendente / concluída): ')
    nova_tarefa = {'titulo':titulo, 'status':status}
    tarefas.append(nova_tarefa)
    salvar_json()

    redirecionar_menu()

def listar_tarefas():

    final_opcoes()
    print(f'{'Título da Tarefa'.ljust(23)} | {'Status'.ljust(20)}')

    for tarefa in tarefas:
        titulo = tarefa['titulo']
        status = tarefa['status']

        print(f' - {titulo.ljust(20)} | {status.ljust(20)}')

    redirecionar_menu()  

def alterar_titulo_tarefa():

    nome_tarefa = input('Digite o titulo da tarefa: ')
    tarefa_encontrada = False

    for tarefa in tarefas:
        if tarefa['titulo'] == nome_tarefa:
            tarefa_encontrada = True
            novo_titulo = input('Digite o novo título a tarefa: ')
            tarefa['titulo'] = novo_titulo
            salvar_json()
            print('Tarefa renomeada com sucesso!')
    if not tarefa_encontrada:
        print('Não foi encontrado a sua tarefa, por favor, tente novamente.')
    
    redirecionar_menu()

def alterar_status_tarefa():
    nome_tarefa = input('Digite o nome da tarefa que deseja alterar: ')
    tarefa_encontrada = False

    for tarefa in tarefas:

        if tarefa['titulo'] == nome_tarefa:
            tarefa_encontrada = True 
            tarefa['status'] = 'concluída' if tarefa['status'] == 'pendente' else 'pendente'
            salvar_json()
            print('Tarefa alterada com sucesso!')

    if not tarefa_encontrada:
        print('Não foi encontrado a sua tarefa, por favor, tente novamente.')

    redirecionar_menu()

def sair():
    final_opcoes()
    exibir_subtitulo('''
▄▀█ █▀█ █▀█   █▀▀ █▄ █ █▀▀ █▀▀ █▀█ █▀█ ▄▀█ █▀▄ █▀█ 
█▀█ █▀▀ █▀▀   ██▄ █ ▀█ █▄▄ ██▄ █▀▄ █▀▄ █▀█ █▄▀ █▄█ ▄
''')

def escolha_opcao():
    escolha = int(input('Digite um número que corresponda as opções: '))
    match escolha:

        case 1:
            return criar_tarefa()
        
        case 2:
            return listar_tarefas()
        
        case 3:
            return alterar_titulo_tarefa()
        
        case 4:
            return alterar_status_tarefa()
        
        case 5:
            return sair()

def final_opcoes():
    os.system('cls')

def salvar_json():
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_json():
    global tarefas
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []
def main():
   carregar_json()
   final_opcoes()
   exibir_nome()
   opcoes()
   escolha_opcao()

if __name__ == '__main__':
    main()
