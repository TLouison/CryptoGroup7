import secrets
import utility as util
import math

def staticDiffieHellman(g, p, socket): #Predefined public values
    secretNum = 24704502257117
    publicKeyHalf = pow(g, secretNum, p)
    socket.send(str(publicKeyHalf).encode())
    otherPublicKeyHalf = int(socket.recv(1024).decode())
    publicSecret = pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def EphemeralDiffieHellman(g, p, socket): #New public values everytime to protect message
    secretNum = secrets.randbits(256)
    publicKeyHalf = pow(g, secretNum, p)
    socket.send(str(publicKeyHalf).encode())
    otherPublicKeyHalf = int(socket.recv(1024).decode())
    publicSecret = pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def RSAKeyGeneration(socket, option): 
    while(True):
        p = secrets.randbits(256)
        if(util.is_prime(p)):
            break
    while(True):
        q = secrets.randbits(256)
        if(util.is_prime(q) and p!=q):
            break
    N = p*q
    carmichael = util.lcm(p-1,q-1)
    e = 65537
    d = float(1+carmichael)/e
    k = 1
    while(not d.is_integer()):
        d = float(1+k*carmichael)/e
        k += 1
    d = int(d)
    socket.send(str(e).encode())
    e = int(socket.recv(1024).decode())
    socket.send(str(N).encode())
    n = int(socket.recv(1024).decode())
    return d, n, e, N

def main(socket, algorithm, option):
    info = dict()
    if algorithm == 'ephemeraldiffiehellman':
        if option == 0:
            g = secrets.randbits(80)
            p = secrets.randbits(80)
            socket.send(str(g).encode())
            socket.send(str(p).encode())
        else:
            g = int(socket.recv(2000).decode())
            p = int(socket.recv(2000).decode())
        info['sessionKey'], info['n'] = EphemeralDiffieHellman(g, p, socket), p    
        return info

    if algorithm == 'staticdiffiehellman':
        if option == 0:
            g = 642201221879453301923991
            p = 20038108183259
            socket.send(str(g).encode())
            socket.send(str(p).encode())
        else:
            g = int(socket.recv(2000).decode())
            p = int(socket.recv(2000).decode())
        info['sessionKey'], info['n'] = staticDiffieHellman(g, p, socket), p
        return info
    
    if algorithm == 'rsakeygeneration':
        info['sessionKey'], info['n'], info['publicKey'], info['N'] = RSAKeyGeneration(socket, option)
        return info

if __name__ == "__main__":
    _known_primes = []
    diffieHellman(5, 23)