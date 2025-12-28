import os

def exercicio1():
    print('''
Ana está desenvolvendo um programa que precisa processar uma lista de 5 nomes de clientes para gerar relatórios mensais. Para isso, ela precisa escrever um programa que percorra a lista de nomes e exiba cada cliente.
''')
    
    clientes = ["João", "Maria", "Carlos", "Ana", "Beatriz"]

    for nome in clientes:
        print(f'- {nome}')

    '''Usado a estrutura for, pois sabemos a quantidade de operações que será feita, que será a quantidade de elementos que a lista terá'''

def exercicio2():
    print('''
André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
''')
    
    contador = 0
    while contador < 10:
        print('Processando dados...')
        contador += 1

def exercicio3():
    print('''
Marcos está desenvolvendo um programa para exibir uma mensagem de boas-vindas repetidamente no console, como parte de uma campanha de marketing de sua plataforma chamada Buscante. Ele quer garantir que a mensagem seja exibida 5 vezes.

Ajude Marcos a escrever um programa que exiba a mensagem: "Bem-vindo ao Buscante!" o número exato de vezes que ele precisa.
''')
    
    for i in range(5):
        print('Bem vindo ao Buscante!')

def exercicio4():
    print('''
Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
''')
    
    valores = [10, 20, 30, 40, 50]
    total = 0

    for i in valores:
        total += i
    print(f'A soma total das receitas é: {total}')

def exercicio5():
    print('''
Ana está desenvolvendo seu portfólio para exibir os projetos de Python que concluiu. Ela organizou uma lista com o nome de cada projeto, mas percebeu que alguns itens podem estar ausentes, aparecendo como None:
''')
    
    projetos = ["website", "jogo", "análise de dados", None, "aplicativo móvel"]
    for projeto in projetos:
        if projeto == None:
            print('Projeto ausente')
        else:
            print(projeto)

def exercicio6():
    print('''
José está desenvolvendo uma funcionalidade no sistema do Buscante para interromper a busca assim que um livro específico é encontrado. A lista de livros já cadastrados no sistema é a seguinte:
''')
    
    livros = ["1984", "Dom Casmurro", "O Pequeno Príncipe", "O Hobbit", "Orgulho e Preconceito"]
    for livro in livros:
        if livro == "O Hobbit":
            print(f'Livro encontrado: {livro}') 
            break

def exercicio7():
    print('''
Você está desenvolvendo um sistema de controle de estoque para o Buscante. Um dos requisitos é verificar a quantidade de exemplares de um livro em estoque e continuar vendendo até que o estoque se esgote. Sempre que uma venda é realizada, o sistema deve informar o usuário e atualizar a quantidade disponível.

Crie um programa que simule as vendas de um livro com o estoque inicial de 5 exemplares. O programa deve exibir a mensagem "Venda realizada! Estoque restante: <quantidade>" a cada venda e, ao final, exibir a mensagem "Estoque esgotado".
''')
    
    # estoque = 5
    # for i in range(5):
    #     estoque -= 1
    #     print(f'Venda realizada! Estoque restante: {estoque}')

    #     if estoque == 0:
    #         print('Estoque esgotado')

    estoque = 5
    while estoque > 0:
        estoque -= 1
        print(f'Venda realizada! Estoque restante: {estoque}')
    print('Estoque esgotado')

def exercicio8():
    print('''
Aline está implementando uma funcionalidade que exibe mensagens personalizadas para os clientes durante uma promoção especial da sua nova loja de livros. O sistema deve exibir uma mensagem de contagem regressiva personalizada para cada número de 10 até 1, e ao final exibir a mensagem: "Aproveite a promoção agora!".

Crie um programa que utilize um laço for para exibir as seguintes mensagens:

Para números pares, exiba: "Faltam apenas <número> segundos - Não perca essa oportunidade!".
Para números ímpares, exiba: "A contagem continua: <número> segundos restantes.".
Ao final da contagem, exiba a mensagem: "Aproveite a promoção agora!".
''')
    
    for i in range(10,0,-1):
        if i % 2 == 0:
            print(f'Faltam apenas {i} segundos - Não perca essa oportunidade!')
        else:
            print(f'A contagem continua: {i} segundos restantes')
    print('Aproveite a promoção agora!')

def exercicio9():
    print('''
Ana está implementando um sistema de filtragem de livros no Buscante. A funcionalidade deve percorrer uma lista de livros e exibir o nome de cada livro disponível em estoque. No entanto, se o livro estiver esgotado, ele deve ser ignorado durante a iteração.
''')
    
    livros = [
    {"nome": "1984", "estoque": 5},
    {"nome": "Dom Casmurro", "estoque": 0},
    {"nome": "O Pequeno Príncipe", "estoque": 3},
    {"nome": "O Hobbit", "estoque": 0},
    {"nome": "Orgulho e Preconceito", "estoque": 2}
]
    
    for livro in livros:

        if livro['estoque'] <= 0:
            continue
        print(f'Livro disponível: {livro['nome']}')

def exercicio10():
    print('''
João está desenvolvendo um sistema de cadastro para um site de leitura. Ele precisa garantir que os usuários insiram um nome de usuário e uma senha válidos. As regras são as seguintes:

O nome de usuário deve ter pelo menos 5 caracteres.
A senha deve ter pelo menos 8 caracteres.
João quer que o sistema continue solicitando as informações até que ambas as condições sejam atendidas. Quando o usuário insere dados válidos, o programa deve exibir a mensagem: "Cadastro realizado com sucesso!".

Crie um programa que implemente essa lógica usando um laço while.
''')
    
    while True:
    
        nome_usuario = input('Digite seu nome de usuário:')
        if len(nome_usuario) < 5:
            print('O nome do usuário deve ter pelo menos 5 caracteres')
            continue

        senha = input('Digite seu senha de usuário:')
        if len(senha) < 8:
            print('A senha deve ter pelo menos 8 caracteres')
            continue

        print('Cadastro realizado com sucesso!')
        break

# Concluído com sucesso!

def main():
    os.system('cls')
    exercicio10()

if __name__ == '__main__':
    main()