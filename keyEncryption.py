import sha1

def encryptDES():
    return 

# def decryptDES():

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

def textBookRSA(m, k, n):
    return pow(m, k, n)

def main(socket, cipherSuite, info, msg, encrypt):
    if(cipherSuite == '3des'): #Need to see DES implementation first
        return tripleDES(info['sessionKey'], msg)
    elif(cipherSuite == 'des'): #Need to see DES implementation first
        return DES(info['sessionKey'], msg)
    elif(cipherSuite == 'textbookrsa'):
        print(msg)
        if(encrypt):
            print('Encrypt')
            msg = ''.join(format(ord(x), 'b') for x in msg)
            msg = int(msg,2)
            ans = textBookRSA(msg, info['publicKey'], info['n'])
            print(ans)
            return textBookRSA(msg, info['publicKey'], info['n'])
        else:
            print('Decrypt')
            msg = int(msg)
            ans = textBookRSA(msg, info['sessionKey'], info['N'])
            ans = bin(ans)[2:]
            print(ans.decode('ascii'))
            return ans.decode('ascii')
    elif(cipherSuite == 'semanticrsa'):
        return 'sadf'