import secrets

def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True # n  is definitely composite
 
def is_prime(n, _precision_for_huge_n=16):
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751: 
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def lcm(x, y):
    return abs(x*y) // math.gcd(x,y)

def extended_gcd(a ,b):
    lastR, R = abs(a), abs(b)
    x, lastX, y, lastY = 0, 1, 1, 0
    while(R):
        lastR, (quotient, R) = R, divmod(lastR, R)
        x, lastX = lastX - quotient*x, x
        y, lastY = lastY - quotient*y, y
    return lastR, lastX*(-1 if a < 0 else 1), lastY * (-1 if b < 0 else 1)
             
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x%m

def diffieHellman(g, p, socket):
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
        if(is_prime(p)):
            break
    while(True):
        q = secrets.randbits(256)
        if(is_prime(q) and p!=q):
            break
    N = p*q
    carmichael = lcm(p-1,q-1)
    e = 0
    while(True):
        e = secrets.randbelow(carmichael)
        if(e != 1 and math.gcd(e,carmichael)==1):
            break   
    d = modinv(e, carmichael)
    return n, e, d

def semanticRSA(socket):


def main():
    _known_primes = []
    return "value"

if __name__ == "__main__":
    _known_primes = []
    diffieHellman(5, 23)