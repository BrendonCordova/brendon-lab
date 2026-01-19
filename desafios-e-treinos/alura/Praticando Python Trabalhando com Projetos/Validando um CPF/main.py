
# def validar_cpf(cpf):
#     numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] # simplificar usando o isdigit()
#     for caractere in cpf:
#         if caractere not in numeros:
#             print('Erro: O CPF deve conter apenas números')
#             return
#     if len(cpf) != 11:
#         print('Erro: O CPF deve ter exatamente 11 dígitos. ')
#     else:
#         return 'CPF válido'

def validar_cpf(cpf):
    if not cpf.isdigit():
        return 'Erro: O CPF deve conter apenas números.'
    if len(cpf) != 11:
        return 'Erro: O CPF deve conter exatamente 11 dígitos.'
    return 'CPF válido.'


cpf = input('Digite seu CPF(apenas números): ').strip()
print(validar_cpf(cpf))
