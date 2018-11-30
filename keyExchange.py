import secrets
import utility as util

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

def semanticRSA(socket):
    return "Yener"

def main():
    _known_primes = []
    return "value"

if __name__ == "__main__":
    _known_primes = []
    diffieHellman(5, 23)