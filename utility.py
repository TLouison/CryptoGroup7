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

#Chunks a string into chunks of length n
def chunkMessage(msg, n):
    binary_list = []
    buffer = ""

    #Splitting the binary string into 8 bit sections
    for i in range(len(msg)):
        buffer += msg[i]

        if len(buffer) == n:
            binary_list.append(buffer)
            buffer = ""

    if len(buffer) < n and len(buffer) > 0:
        while len(buffer) < n:
            buffer += "0"
        binary_list.append(buffer)

    return binary_list