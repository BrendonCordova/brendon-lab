
def identificar_palavras_longas(texto):
    palavras_longas = []
    for palavra in texto:
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    
    if not palavras_longas:
        return 'Nenhuma palavra longa foi encontrada no texto.'
    else:
        print('Palavras longas encontradas:')
        for palavra in palavras_longas:
            print(palavra)

texto = input('Digite um texto: ').split()
identificar_palavras_longas(texto)
