import os

def exercicio1():
    print('''Bruno gerencia um pequeno comércio e quer saber qual produto teve o melhor desempenho de vendas no mês passado. Ele registrou a quantidade vendida de dois produtos: maçãs e bananas. Agora, ele precisa escrever um programa que identifique e exiba qual deles teve maior venda.

    Crie um programa que receba o número de vendas dos dois produtos e exiba uma mensagem indicando qual deles vendeu mais. Se as quantidades forem iguais, exiba uma mensagem dizendo que houve empate.''')

    quant_maca_vendidas = int(input('Quantas maças foram vendidas: '))
    quant_bananas_vendidas = int(input('Quantas bananas foram vendidas: '))

    if quant_maca_vendidas > quant_bananas_vendidas:
        print('As maças tiveram mais vendas')
    elif quant_bananas_vendidas > quant_maca_vendidas:
        print('As bananas tiveram mais vendas')
    else:
        print('Houve empate de vendas')

def exercicio2():
    print('''Camila está organizando um projeto e precisa calcular o tempo total necessário para concluir três atividades: A, B e C. No entanto, se alguma atividade tiver um número de dias negativo, o código deve avisar que os valores inseridos são inválidos e não calcular o total.

Escreva um programa que receba o número de dias de três atividades e exiba o tempo total do projeto. Se algum valor for negativo, mostre uma mensagem informando o erro.''')

    dias_a = int(input('Informe os dias para a atividade A: '))
    dias_b = int(input('Informe os dias para a atividade B: '))
    dias_c = int(input('Informe os dias para a atividade C: '))

    if dias_a < 0 or dias_b < 0 or dias_c < 0:
         print('Erro: Os dias não podem ser negativos')
    else:
         total_dias = dias_a + dias_b + dias_c
         print(f'O total de dias para a atividade é: {total_dias}')


def exercicio3():
    print('''Lucas trabalha em TI e precisa garantir que a temperatura de uma sala de servidores não ultrapasse 25°C. Ele quer um programa que receba a temperatura atual como entrada e, se necessário, exiba uma mensagem de alerta.''')
    
    temperatura_atual = int(input('Digite a temperatura atual: '))

    if temperatura_atual > 25:
         print('Alerta! Temperatura acima do limite permitido.')
    else:
         print("Temperatura dentro do limite seguro.")

def exercicio4():
    print('''
Anna Júlia está criando um sistema para calcular o Índice de Massa Corporal (IMC) e fornecer recomendações básicas. O programa deve receber o peso e a altura de uma pessoa e exibir o valor do IMC, além de indicar se está abaixo do peso, com peso normal ou acima do peso. Crie um programa que receba o peso (em kg) e a altura (em metros) e calcule o IMC usando a fórmula: IMC = peso / (altura ** 2) Depois, exiba o valor do IMC e uma mensagem indicando se está abaixo do peso (IMC < 18.5), peso normal (18.5 <= IMC < 25) ou acima do peso (IMC >= 25).
''')
    
    peso = int(input('Digite seu peso (kg): '))
    altura = float(input('Digite sua altura (m): '))

    imc = peso / (altura ** 2)
    print(f'Seu IMC é: {imc:.2f}')

    if imc < 18.5:
         print('Você está abaixo do peso')
    elif imc < 25:
         print('Você está com peso normal')
    else:
         print('Você está acima do peso')

def exercicio5():
    print('''
Carlos quer monitorar seu orçamento mensal para evitar gastos excessivos. Ele estabeleceu um limite de R$ 3.000,00 para seus gastos e precisa de um programa que ajude a controlar suas despesas. O programa deve receber o total de despesas realizadas e informar se ele ultrapassou o limite ou ainda está dentro do orçamento.
''')
    
    total_gastos = float(input('Digite o total de despesas do Mês (R$): '))

    if total_gastos > 3000.00:
         print('Atenção! Você ultrapassou o limite do orçamento.')
    else:
         print('Você tem orçamento ainda.')

def exercicio6():
    print('''
Mariana é responsável por liberar o acesso ao escritório e precisa de um programa que verifique se os funcionários podem entrar. Para isso, ela usará o horário atual. O escritório só permite acesso entre 8h e 18h. Crie um programa que receba a hora atual como entrada (em formato de 24 horas) e exiba uma mensagem informando se o acesso é permitido ou negado.
''')
    
    horario_atual = int(input('Digite a hora atual (formato 24 horas): '))

    if 8 <= horario_atual < 18:
         print('Acesso permitido!')
    else:
         print('Acesso negado!')

def exercicio7():
    print('''
Uma professora precisa de um programa que ajude a calcular a média final dos alunos e informe se foram aprovados, ficaram de recuperação ou reprovados. As regras são:

Média >= 7: Aprovado
5 <= Média < 7: Recuperação
Média < 5: Reprovado
Escreva um programa que receba três notas como entrada e calcule a média final. Com base na média, exiba a situação do aluno.
''')
    
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    n3 = float(input('Digite a terceira nota: '))

    media = (n1 + n2 + n3) / 3
    print(f'Média: {media:.2f}')

    if media >= 7:
         print('Aprovado')
    elif media >= 5:
         print('Recuperação')
    else:
         print('Reprovado!')

def exercicio8():
    print('''
Fernanda está planejando uma viagem e quer calcular quanto pagará de pedágio. O valor do pedágio depende da distância percorrida:

Até 100 km: R$ 10,00
Entre 100 km e 200 km: R$ 20,00
Acima de 200 km: R$ 30,00
Crie um programa que receba a distância percorrida e informe o valor do pedágio correspondente.
''')
    
    distancia_percorrida = int(input('Digite a distância percorrida (em km): '))

    if distancia_percorrida <= 100:
         print('Valor do pedágio: R$ 10,00')
    elif distancia_percorrida <= 200:
         print('Valor do pedágio: R$ 20,00')
    else:
         print('Valor do pedágio: R$ 30,00')

def exercicio9():
    print('''
Lucas está desenvolvendo um jogo e precisa de uma funcionalidade que verifique se um número é par ou ímpar. Essa verificação será usada para definir ações diferentes dentro do jogo. Escreva um programa que receba um número inteiro e exiba uma mensagem informando se ele é par ou ímpar.
''')
    
    numero_inteiro = int(input('Digite um número inteiro: '))
    if numero_inteiro % 2 == 0:
         print('O número é par')
    else:
         print('O número é ímpar')

def exercicio10():
    print('''
Pedro quer solicitar um empréstimo, mas a aprovação depende de duas condições:

O valor da renda mensal precisa ser maior que R$ 2.000,00.
O valor da parcela não pode ultrapassar 30% da renda.
Crie um programa que receba como entrada a renda mensal de Pedro e o valor da parcela desejada. O programa deve informar se o empréstimo foi aprovado ou negado com base nas condições acima.
''')
    
    renda_mensal = float(input('Digite o valor da sua renda mensal: '))
    parcela = float(input('Digite o valor da parcela desejada: '))

    if renda_mensal > 2000 and parcela <= 0.3 * renda_mensal:
        print('Empréstimo aceito!')
    elif renda_mensal <= 2000:    
        print('Empréstimo negado: renda mensal mínima não atingida')
    else:
        print('Empréstimo negado: parcela acima de 30% da renda')       

# Para não poluir de execuções

def main():
      os.system('cls')
      exercicio10()

if __name__ == '__main__':
      main()