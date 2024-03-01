import numpy as np

def cifrar_con_cifrado_hill(texto_plano, clave):
    dim_matriz = len(clave)
    longitud_relleno = dim_matriz - (len(texto_plano) % dim_matriz)
    texto_plano_rellenado = texto_plano + 'X' * longitud_relleno

    texto_cifrado = ""
    for i in range(0, len(texto_plano_rellenado), dim_matriz):
        bloque = texto_plano_rellenado[i:i + dim_matriz]
        vector_bloque = [ord(caracter) - ord('A') for caracter in bloque]
        vector_cifrado = np.dot(clave, vector_bloque) % 26
        bloque_cifrado = ''.join(chr(num + ord('A')) for num in vector_cifrado)
        texto_cifrado += bloque_cifrado

    return texto_cifrado

texto_plano = "HELLOWORLD"
clave = [[2, 3], [1, 4]]
texto_cifrado = cifrar_con_cifrado_hill(texto_plano, clave)
print(f"Texto cifrado para {texto_plano} es: {texto_cifrado}")