print("Capítulo 4 - Quicksort\nPágina 83\nPrática:")

def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivo = array[0]
        menores = [i for i in array[1:] if i <= pivo]
        maiores = [i for i in array[1:] if i > pivo]

        return quicksort(menores) + [pivo] + quicksort(maiores)
    # errei na colocação do pivo no return, pois esqueci que o pivo é um array, por isso, há necessidade de por []

resultado = quicksort([10, 5, 2, 3])
print(resultado)