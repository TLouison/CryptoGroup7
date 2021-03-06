#Implementation of SHA-1
#Written by Todd Louison
import utility as util
import secrets

#Left rotates the given bitstring by n
def leftRotate(msg, n):
    return ((msg << n) | (msg >> (32 - n))) & 0xffffffff

#Left shifts the bits
def leftShift(bits, n):
    return bits << n

#real sha1 without string garbage
def sha(msg):
    #Defining required constants
    h0 = 0x67452301
    h1 = 0xEFCDAB89
    h2 = 0x98BADCFE
    h3 = 0x10325476
    h4 = 0xC3D2E1F0

    #Gathering len of original message and append a 1 to the new msg
    m_length = len(msg)
    msg += '1'

    #Filling out the 512 bit msg with the 64-bit length
    for i in range(512):
        if ((len(msg)+len(bin(m_length)[2:])) % 512 == 0):
            break
        msg += "0"

    msg += bin(m_length)[2:]
    #Chunking message into usable portions
    chunkedMessage = util.chunkMessage(msg, 512)

    #Getting hash values for each 512 bit chunk
    for chunk in chunkedMessage:
        w = list(map(lambda x: int(x, 2), util.chunkMessage(chunk, 32)))
        while len(w) < 80:
            w.append(0)

        for i in range(16, 80):
            w[i] = leftRotate( w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i - 16], 1)

        #Defaulting a-e to the running totals h0-h4
        a = h0
        b = h1
        c = h2
        d = h3
        e = h4

        #Perfoming the SHA logical operations
        for i in range(80):
            #Determining which f and k to use
            if 0 <= i <= 19:
                f = (d ^ (b & (c ^ d)))
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

            #Updating values
            temp = leftRotate(a, 5) + f + e + k + w[i] & 0xffffffff
            e = d
            d = c
            c = leftRotate(b, 30)
            b = a
            a = temp

        #Adding the values to the current running total
        h0 += a
        h1 += b
        h2 += c
        h3 += d
        h4 += e

    #Performing bitwise operations to create a 160-bit digest
    return leftShift(h0, 128) | leftShift(h1, 96) | leftShift(h2, 64) | leftShift(h3, 32) | h4


if __name__ == "__main__":
    print(len('01110100011001010111001101110100'))
    ans = sha('01110100011001010111001101110100')
    print(bin(ans))