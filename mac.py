import sha1

def HMAC(k, m):
    blockSize = 64 #for SHA-1
    outerPad = '0101110001011100010111000101110001011100010111000101110001011100'
    innerPad = '0011011000110110001101100011011000110110001101100011011000110110'

    if(len(k) > blockSize):
        sha1.sha(k)
    while outerPad < blockSize and innerPad < blockSize
    
    outerPadKey = k ^ outerPad
    innerPadKey = k ^ innerPad

    hMAC = sha1.sha(outerPadKey + sha1.sh(innerPadKey + m))
    return hMAC