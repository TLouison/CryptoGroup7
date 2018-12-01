import hash

'''
Message Authentication Code

HMAC
'''


def HMAC(k, m):
    blockSize = 64 #for SHA-1
    outerPad = '01011100'
    innerPad = '00110110'

    if(len(k) > blockSize):
        hash.sha(k)
    
    while(len(k) < blockSize):
        k += '0'
    
    while(len(outerPad) < blockSize and len(innerPad) < blockSize):
        outerPad += outerPad
        innerPad += innerPad
    
    outerPadKey = k ^ outerPad
    innerPadKey = k ^ innerPad

    hMAC = hash.sha(outerPadKey + hash.sha(innerPadKey + m))
    return hMAC