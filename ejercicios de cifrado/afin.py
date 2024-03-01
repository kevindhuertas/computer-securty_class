def cifrado_afin(texto_plano, a, b):
    texto_cifrado = ""
    for caracter in texto_plano:
        if caracter.isalpha():
            # Desplaza el alfabeto para empezar con 'A' = 0
            desplazamiento = ord('A') if caracter.isupper() else ord('a')
            # Aplica la transformación afin y convierte de nuevo a carácter
            caracter_cifrado = chr(((a * (ord(caracter) - desplazamiento) + b) % 26) + desplazamiento)
            texto_cifrado += caracter_cifrado
        else:
            texto_cifrado += caracter
    return texto_cifrado


texto_plano1 = "HELLO"
a1 = 5
b1 = 8
texto_cifrado1 = cifrado_afin(texto_plano1, a1, b1)
print(f"Texto cifrado para {texto_plano1} es: {texto_cifrado1}")

texto_plano2 = "WORLD"
a2 = 3
b2 = 7
texto_cifrado2 = cifrado_afin(texto_plano2, a2, b2)
print(f"Texto cifrado para {texto_plano2} es: {texto_cifrado2}")