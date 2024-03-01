def cifrado_de_sustitucion(texto_plano, clave):
    texto_cifrado = ""
    for caracter in texto_plano:
        if caracter in clave:
            texto_cifrado += clave[caracter]
        else:
            texto_cifrado += caracter
    return texto_cifrado

texto_plano1 = "HELLO"
clave1 = {'H': 'X', 'E': 'Y', 'L': 'Z', 'O': 'A'}
texto_cifrado1 = cifrado_de_sustitucion(texto_plano1, clave1)
print(f"Texto cifrado para {texto_plano1} es: {texto_cifrado1}")

texto_plano2 = "WORLD"
clave2 = {'W': 'Q', 'O': 'P', 'R': 'S', 'L': 'T', 'D': 'U'}
texto_cifrado2 = cifrado_de_sustitucion(texto_plano2, clave2)
print(f"Texto cifrado para {texto_plano2} es: {texto_cifrado2}")