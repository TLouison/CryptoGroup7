import secrets
import utility as util
import sha1

def i2osp(integer, size=4):
  return ''.join([chr((integer >> (8 * i)) & 0xFF) for i in reversed(range(size))])

def mgf1(msg, length):
    output = ''
    counter = 0
    while(len(output) < length):
        C = i2osp(counter, 4)
        output += sha1.sha(msg+C)
        count += 1
    return output[:lengh]

def staticDiffieHellman(g, p, socket):
    secretNum = 24704502257117
    print(secretNum)
    publicKeyHalf = pow(g, secretNum, p)
    print(publicKeyHalf)
    socket.send(publicKeyHalf)
    otherPublicKeyHalf = socket.recv(1024)
    publicSecret = pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def EphemeralDiffieHellman(g, p, socket):
    secretNum = secrets.randbits(256)
    print(secretNum)
    publicKeyHalf = pow(g, secretNum, p)
    print(publicKeyHalf)
    socket.send(publicKeyHalf)
    otherPublicKeyHalf = socket.recv(1024)
    publicSecret = pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def RSAKeyGeneration(socket):
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
    e = 0
    while(True):
        e = secrets.randbelow(carmichael)
        if(e != 1 and math.gcd(e,carmichael)==1):
            break   
    d = util.modinv(e, carmichael)
    socket.send(e)
    e = socket.recv(1024)
    socket.send(N)
    n = socket.recv(1024)
    return n, d, e

def semanticRSAEncrypt(m, socket):
    n = 12
    k0 = 10
    k1 = 11
    r = secrets.randbits(k0)
    appendedM = m
    while(len(appendedM) < n-k0):
        appendedM += '0'
    G = sha1.sha(r)
    X = m^G
    H = sha1.sha(X)
    Y = r^H
    mFinal = X+Y
    return textBookRSA(mFinal)

def semanticRSADecrypt(Y, X):
    n = 12
    k0 = 10
    k1 = 11
    H = sha1.sha(X)
    r = Y ^ H
    G = sha1.sha(r)
    appendedM = X ^ G
    m = appendedM[0:len(n)]

def main(socket, algorithm, option):
    if algorithm == 'ephemeraldiffiehellman':
        if option == 0:
            g = secrets.randint(80)
            p = secrets.randint(80)
            socket.send(g)
            socket.send(p)
        else:
            g = socket.recv(10)
            p = socket.recv(10)
        return g, p, EphemeralDiffieHellman(g, p, socket)

    if algorithm == 'staticdiffiehellman':
        if option == 0:
            g = secrets.randint(80)
            p = secrets.randint(80)
            socket.send(g)
            socket.send(p)
        else:
            g = socket.recv(10)
            p = socket.recv(10)
        return g, p, staticDiffieHellman(g, p, socket)
    
    if algorithm == 'textbookrsa':

if __name__ == "__main__":
    _known_primes = []
    diffieHellman(5, 23)