import secrets
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
    p = secrets.randbits(256)
    q = secrets.randbits(256)
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
    return "value"

if __name__ == "__main__":
    diffieHellman(5, 23)