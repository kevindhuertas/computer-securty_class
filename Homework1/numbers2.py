def numeros_a_letras(numeros):
    letras = ""
    for numero in numeros:
        numero = int(numero)
        if 1 <= numero <= 26:
            letras += chr(numero + 96).upper()
        else:
            letras += " " 
    return letras

numeros = "16 9 3 15 3 20 6".split()
print(numeros_a_letras(numeros))

numeros = "20 8 5 14 21 13 2 5 18 19 13 1 19 15 14".split()
print(numeros_a_letras(numeros))