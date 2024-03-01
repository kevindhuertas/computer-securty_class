
n: 100269649132846895943031765309154462680663778448438433353555801172324096096067343064990500266175176645208771348901368426984678416621986848939445719834305538173819093512064092128145191019612908696253852702240758957796475764747836297169461927197538694272833215960444811966073494952729629441183203630445241681617
e: 65537
ciphertext: 72264588332335364261914902468159957421256187297797847336573781072962284309078615365100346219449341728451813401487097184912328357075168001831187040243190270266199642778602169028856520096427544072788835924493367346440734264044961021796109850132326083259540423909033795502464042613323402654575210966400854735810


# Hago una llamada al mercury.picoctf.net, y en consola paso el calculo para que haga el decrypt
import socket
import binascii

def recv_until(sock, delimiter):
    data = b""
    while not data.endswith(delimiter):
        data += sock.recv(1)
    return data

# Establecer conexión
host = "mercury.picoctf.net"
port = 10333
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host, port))

# Recibir datos hasta los prompts y extraer los números
print(recv_until(sock, b"n:"))
n = int(recv_until(sock, b"\n").strip())
print(n)

print(recv_until(sock, b"e:"))
e = int(recv_until(sock, b"\n").strip())
print(e)

print(recv_until(sock, b"ciphertext:"))
c = int(recv_until(sock, b"\n").strip())
print(c)

print(recv_until(sock, b"to decrypt:"))

# Realizar cálculo
msg = str((pow(2, e, n) * c) % n).encode() + b"\n"
sock.send(msg)

print(recv_until(sock, b"you go: "))
p2 = int(recv_until(sock, b"\n").strip())
print(p2)

# resultado final
result = p2 // 2
print(result)

# Convertir el resultado a hexadecimal y luego a bytes legibles
st = "{:x}".format(result)
print(binascii.unhexlify(st))

sock.close()