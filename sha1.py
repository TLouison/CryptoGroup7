#Implementation of SHA-1
#Written by Todd Louison
import secrets
import utility as util

#Left rotates the given bitstring by n
def leftRotate(msg, n):
    return ((msg << n) | (msg >> (32 - n))) & 0xffffffff

def leftShift(bits, n):
    return bits << n

#real sha1 without string garbage
def sha1Ints(msg):
    #Defining required constants
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    #Gathering len of original message and append a 1 to the new msg
    m_length = bin(len(bin(msg)[2:]))[2:]
    msg += 0x80

    #Padding to be congruent with -64 = 448 % 512
    msg = bin(msg)[2:]
    for i in range(512):
        if ((len(msg)+64) % 512 == 0):
            break
        msg += "0"

    #Filling out the 512 bit msg with the 64-bit length
    msg = int(msg + "{:}".format(m_length).rjust(64, "0"), 2)

    #Chunking message into usable portions
    chunkedMessage = util.chunkMessage(bin(msg)[2:], 512)

    for chunk in chunkedMessage:
        w = list(map(lambda x: int(x, 2), util.chunkMessage(chunk, 32)))
        while len(w) < 80:
            w.append(0)

        for i in range(16, 80):
            w[i] = leftRotate( w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i - 16], 1)

        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #Perfoming the SHA logical operations
        for i in range(80):
            if 0 <= i <= 19:
                f = (b & c) | (~b & d)
                k = 0x5A827999
            elif 20 <= i <= 39:
                f = b ^ c ^ d
                k = 0x6ED9EBA1
            elif 40 <= i <= 59:
                f = (b & c) | (b & d) | (c & d)
                k = 0x8F1BBCDC
            elif 60 <= i <= 79:
                f = b ^ c ^ d
                k = 0xCA62C1D6

            temp = leftRotate(a, 5) + f + e + k + w[i]
            e = d
            d = c
            c = leftRotate(b, 30)
            b = a
            a = temp
        
        h0 += a
        h1 += b
        h2 += c
        h3 += d
        h4 += e

    return leftShift(h0, 128) | leftShift(h1, 96) | leftShift(h2, 64) | leftShift(h3, 32) | h4


if __name__ == "__main__":
    ans = sha1Ints(0b00000000010101010101101001010100001010101010101010101010101100101010001010101011101110101111111110100010010000101010000101000000)
    print(bin(ans))