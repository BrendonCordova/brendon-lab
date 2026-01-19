from valor_da_gorjeta import valor_gorjeta, valor_total_da_conta

# Entrada

try:
    valor_da_conta = float(input('Digite o valor da conta: '))
    porcentagem_gorjeta = int(input('Digite a porcentagem da gorjeta: '))
except ValueError:
    print('Erro: o valor digitado não é um valor válido')

# Processamento

gorjeta = valor_gorjeta(valor_da_conta, porcentagem_gorjeta)

total = valor_total_da_conta(gorjeta, valor_da_conta)

# Saída

print(f'Valor da gorjeta: R$ {gorjeta:.2f}')
print(f'Total a pagar: R$ {total:.2f}')