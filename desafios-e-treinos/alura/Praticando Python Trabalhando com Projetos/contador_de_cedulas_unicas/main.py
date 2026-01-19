

def contador_cedulas():
    cedulas = [100, 50, 20, 10, 5, 2]

    try:
        valor_saque_solicitado = int(input('Digite o valor do saque: ').strip())


        if valor_saque_solicitado % 2 != 0:
            print('Erro: O valor deve ser múltiplo de 2.')
            
        elif valor_saque_solicitado <= 0:
            print('Erro: O valor deve ser positivo.')
        
        else:
            print('\nCédulas entregues:')

            for cedula in cedulas:
                quantidade = valor_saque_solicitado // cedula
                if quantidade > 0:
                    print(f'{quantidade} cédulas de R$ {cedula}')
                    valor_saque_solicitado = valor_saque_solicitado % cedula

    except ValueError:
        print('Erro: A entrada não é um valor válido, por favor, escreva o saque em valor númerico')
    
    
contador_cedulas()