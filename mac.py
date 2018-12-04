import sha1

def HMAC(k, m):
    blockSize = 64 #for SHA-1
    outerPad = '0101110001011100010111000101110001011100010111000101110001011100'
    innerPad = '0011011000110110001101100011011000110110001101100011011000110110'

    if(len(k) > blockSize):
        sha1.sha(k)
    
    outerPadKey = int(k,2) ^ int(outerPad,2)
    innerPadKey = int(k,2) ^ int(innerPad,2)

    hMAC = sha1.sha( bin(outerPadKey + sha1.sha( bin(innerPadKey + int(m,2))[2:]) )[2:])
    return hMAC

if __name__ == "__main__":
    ans = hex(HMAC("0", "0"))[2:]
    print(ans)
    print(len(ans))