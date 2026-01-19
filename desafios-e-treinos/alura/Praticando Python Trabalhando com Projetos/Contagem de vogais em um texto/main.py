
def contagem_vogais(texto):
    vogais = 'aeiouáàéèíìóòúù'
    quant_vogal = 0
    for caractere in texto.lower():
        if caractere in vogais:
            quant_vogal += 1

    return quant_vogal

texto = input('Digite um texto: ').strip()
print(f'O texto contém {contagem_vogais(texto)} vogais.')