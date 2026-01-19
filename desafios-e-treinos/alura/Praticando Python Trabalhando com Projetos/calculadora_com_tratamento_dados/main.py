def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    return a / b

def calculadora():

    try:
        val1 = float(input('Digite o primeiro valor: '))

        opcoes = '+-*/'

        operacao = input('Digite a operação desejada (+, -, *, /): ')

        if operacao not in opcoes: 
            return 'Opção inválida!'

        val2 = float(input('Digite o segundo valor: '))

        # if val1 == 0 and operacao == '/':  # para caso algum deles fosse zero
        #     val2 = 0

        if operacao == '+':
            resultado = somar(val1, val2)
        elif operacao == '-':
            resultado = subtrair(val1, val2)
        elif operacao == '*':
            resultado = multiplicar(val1, val2)
        else:
            resultado = dividir(val1, val2)
        
        print(f'Resultado: {resultado}')

    except ValueError:
        return 'Erro: Entrada inválida. Digite apenas números.'

    except ZeroDivisionError:
        return 'Erro: Divisão por zero não é permitida.'
    
calculadora()
