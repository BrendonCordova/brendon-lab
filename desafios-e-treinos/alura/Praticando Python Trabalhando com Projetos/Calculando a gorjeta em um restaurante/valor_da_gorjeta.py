
def valor_gorjeta( valor_conta, porcentagem=10):

    valor_da_gorjeta = (porcentagem / 100) * valor_conta

    return valor_da_gorjeta

def valor_total_da_conta(gorjeta, valor_conta):
    
    return valor_conta + gorjeta