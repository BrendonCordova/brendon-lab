import os

def exercicio1():
    print('''
Julia é professora e precisa de um programa para ajudar seus alunos a calcularem suas idades com base no ano de nascimento. Sua tarefa é criar uma função que receba o ano de nascimento e o ano atual e retorne à idade correspondente.
''')
    
    def quantidade_de_anos(ano_atual, ano_nascimento):
        return ano_atual - ano_nascimento

    ano_nascimento = int(input('Digite o ano de nascimento: '))
    ano_atual = int(input('Digite o ano atual: '))
    print(f'A idade é {quantidade_de_anos(ano_atual, ano_nascimento)} anos.')

def exercicio2():
    print('''
Sara está participando de um concurso de escrita, e uma das regras exige que cada palavra de seu texto tenha um limite máximo de caracteres.

Ajude Sara criando uma função que receba uma palavra e exiba a quantidade de caracteres.
''')
    
    def quantidade_palavra(palavra):
        return len(palavra)
    
    palavra = input('Digite uma palavra: ')
    print(f'Essa palavra tem {quantidade_palavra(palavra)} caracteres.')
    

def exercicio3():
    print('''
Beatriz está desenvolvendo um sistema de atendimento para um site de serviços. Ela deseja criar um programa que exiba uma saudação personalizada dependendo da hora do dia que o usuário acessa a plataforma. O sistema deverá ter a seguinte regra:

Se for antes das 12h, exibir "Bom dia";

Entre 12h e 18h, exibir "Boa tarde";

Após 18h, exibir "Boa noite".
''')
    
    def saudacao_pelo_horario(hora):
        if hora < 12:
            return 'Bom dia'
        elif hora < 18:
            return 'Boa tarde'
        else:
            return 'Boa noite'
        
    hora = int(input('Digite a hora atual (0-23): '))
    print(saudacao_pelo_horario(hora))
    
def exercicio4():
    print('''
Pedro está criando um sistema de cadastro de produtos para sua loja e percebeu que todos os números de telefone dos clientes estão armazenados como strings. No entanto, para facilitar buscas e validações, ele precisa que esses números sejam tratados como inteiros.

Dado o seguinte código com uma lista de números de telefone armazenados incorretamente como str, faça duas funções, uma que converte os tipos para inteiro e outra que verifica se a conversão foi feita corretamente e todos os números de telefone são inteiros:
''')

    def conversao(lista):

        return [int(telefone) for telefone in lista]
    
    def verificar_conversao(lista):

        for numero in lista:
            if not isinstance(numero, int):
                return f'erro na conversão, este número {numero} não está convertido'
        return 'Todos os números foram convertidos corretamente'

    telefones = ["11987654321", "21912345678", "31987654321", "11911223344"]
    novos_telefones = conversao(telefones)
    # novos_telefones.append('45488888888') --> teste de erro
    print(verificar_conversao(novos_telefones))
    # print(novos_telefones) --> apenas visualização

def exercicio5():
    print('''
Carlos trabalha em um comércio e precisa saber o valor total de vendas realizadas no dia. As vendas são informadas em uma única linha separadas por espaços.

Sua tarefa é criar um programa que receba essa linha, converta os valores para números e exiba o total.
''')
    
    vendas = input('Digite os valores das vendas: ').split()
    print(vendas)
    total_vendas = sum(map(float,vendas))
    print(f'O total de vendas foi: {total_vendas}')
            
def exercicio6():
    print('''
Lucas está desenvolvendo um sistema para gerar relatórios financeiros e precisa filtrar apenas os valores pares de uma lista de números informada pelo usuário.

Crie um programa que receba uma lista de números e exiba apenas os pares usando a função filter().
''')
    
    numeros = input('Digite os números separados por espaço: ').split()
    pares = filter(lambda n: int(n) % 2 == 0, numeros)
    print(f'Números pares:', ' '.join(pares))

def exercicio7():
    print('''
Clara está gerenciando o estoque de sua loja e recebeu duas listas separadas: uma contendo os nomes dos produtos e outras com seus respectivos preços. Para facilitar a organização, ela precisa combinar essas listas de forma que cada produto seja associado ao seu preço.

Crie um programa que junte as listas e exiba o resultado no formato produto: preço
''')
    
    produtos = input('Digite os produtos separdos por vírgula: ').split(',')
    precos = input('Digite os produtos separdos por vírgula: ').split(',')

    for produto, preco in zip(produtos, precos):
        print(f'{produto.strip()}: {preco.strip()}')

def exercicio8():
    print('''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
''')
    
    soma = lambda num1, num2 : num1 + num2
    subtracao = lambda num1, num2 : num1 - num2
    multiplicacao = lambda num1, num2 : num1 * num2
    divisao = lambda num1, num2 : num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'

    num1 = int(input('Digite o primeiro número: '))    
    num2 = int(input('Digite o segundo número: '))
    operacao = input('Escolha a operação (| + | - | * | / |): ')

    match operacao:
        case '+':
            resultado = soma(num1, num2)
        case '-':
            resultado = subtracao(num1, num2)
        case '*':
            resultado = multiplicacao(num1, num2)
        case '/':
            resultado = divisao(num1, num2)
        case _:
            print('Operação Inválida')
        
    print(f'O resultado é {resultado:.0f}')

def exercicio8_2():
    print('''
Joana está participando de um processo seletivo para uma vaga de desenvolvedora e recebeu um desafio técnico de criar uma calculadora para somar, subtrair, multiplicar e dividir dois números.

Sua tarefa é criar um programa usando funções lambda que receba dois números e um operador matemático escolhido pelo usuário (+, -, * ou /) e exiba o resultado correspondente.
''')
    
    soma = lambda num1, num2 : num1 + num2
    subtracao = lambda num1, num2 : num1 - num2
    multiplicacao = lambda num1, num2 : num1 * num2
    divisao = lambda num1, num2 : num1 / num2 if num2 != 0 else 'Erro: Divisão por zero'

    num1 = int(input('Digite o primeiro número: '))    
    num2 = int(input('Digite o segundo número: '))
    operacao = input('Escolha a operação (| + | - | * | / |): ')

    operacoes = {
        '+': soma,
        '-': subtracao,
        '*': multiplicacao,
        '/': divisao
    }

    if operacao in operacoes:

        resultado = operacoes[operacao](num1, num2)

        print(f'O resultado é: {resultado}')

    else:
        print('Operação Inválida')

def exercicio9():
    print('''
Miguel está desenvolvendo um sistema de cupons de desconto e precisa de uma forma para aplicar diferentes taxas de desconto sobre os valores das compras.

Diante deste problema, crie uma closure que gere uma função capaz de calcular o preço final com um desconto fixo definido pelo usuário.
''')

    def desconto(x):

        def calcular_desconto(preco):
            return preco - ((preco * x) / 100)
        return calcular_desconto
    
    x = float(input('Digite a porcentagem de desconto: '))
    preco_produto = float(input('Digite o valor da compra: '))

    desconto_usuario = desconto(x)
    
    print(f'{desconto_usuario(preco_produto)}')

def exercicio10():
    print('''
Paulo está desenvolvendo um programa para calcular valores acumulados em um sistema financeiro. Ele precisa somar os todos os números inteiros de 1 até n, onde n é um valor escolhido pelo usuário.

Ajude Paulo criando uma função recursiva que receba um número n e retorne a soma de todos os números inteiros de 1 até N.
''')

    def soma_acumulada(n):
        if n == 1:
            return 1
        return n + soma_acumulada(n - 1)

    n = int(input('Digite um número: '))

    print(f'A soma de 1 a {n} é: {soma_acumulada(n)}')

def main():
    os.system('cls')
    exercicio10()

if __name__ == '__main__':
    main()