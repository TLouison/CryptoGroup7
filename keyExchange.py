import secrets
import utility as util

def staticDiffieHellman(g, p, socket):
    secretNum = 24704502257117
    print(secretNum)
    publicKeyHalf = pow(g, secretNum, p)
    print(publicKeyHalf)
    socket.send(publicKeyHalf)
    otherPublicKeyHalf = socket.recv(1024)
    publicSecret pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def EphemeralDiffieHellman(g, p, socket):
    secretNum = secrets.randbits(256)
    print(secretNum)
    publicKeyHalf = pow(g, secretNum, p)
    print(publicKeyHalf)
    socket.send(publicKeyHalf)
    otherPublicKeyHalf = socket.recv(1024)
    publicSecret pow(otherPublicKeyHalf, secretNum, p)
    return publicSecret

def textBookRSA(socket):
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
    return n, e, d

def semanticRSAEncrypt(m, socket):
    n = 12
    k0 = 10
    k1 = 11
    r = secrets.randbits(k0)
    appendedM = m
    while(len(appendedM) < n-k0):
        appendedM += '0'
    G = hash.sha(r)
    X = m^G
    H = hash.sha(X)
    Y = r^H
    mFinal = X+Y
    return textBookRSA(mFinal)

def semanticRSADecrypt(Y, X):
    n = 12
    k0 = 10
    k1 = 11
    H = hash.sha(X)
    r = Y ^ H
    G = hash.sha(r)
    appendedM = X ^ G
    m = appendedM[0:len(n)]


if __name__ == "__main__":
    _known_primes = []
    diffieHellman(5, 23)