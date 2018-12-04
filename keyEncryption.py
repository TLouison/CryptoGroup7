<<<<<<< HEAD
def initPermute(S):
    P = [0]*64

    P[57] = S[0]
    P[59] = S[8]
    P[61] = S[16]
    P[63] = S[24]
    P[56] = S[32]
    P[58] = S[40]
    P[60] = S[48]
    P[62] = S[56]
    P[49] = S[1]
    P[51] = S[9]
    P[53] = S[17]
    P[55] = S[25]
    P[48] = S[33]
    P[50] = S[41]
    P[52] = S[49]
    P[54] = S[57]
    P[41] = S[2]
    P[43] = S[10]
    P[45] = S[18]
    P[47] = S[26]
    P[40] = S[34]
    P[42] = S[42]
    P[44] = S[50]
    P[46] = S[58]
    P[33] = S[3]
    P[35] = S[11]
    P[37] = S[19]
    P[39] = S[27]
    P[32] = S[35]
    P[34] = S[43]
    P[36] = S[51]
    P[38] = S[59]
    P[25] = S[4]
    P[27] = S[12]
    P[29] = S[20]
    P[31] = S[28]
    P[24] = S[36]
    P[26] = S[44]
    P[28] = S[52]
    P[30] = S[60]
    P[17] = S[5]
    P[19] = S[13]
    P[21] = S[21]
    P[23] = S[29]
    P[16] = S[37]
    P[18] = S[45]
    P[20] = S[53]
    P[22] = S[61]
    P[9] = S[6]
    P[11] = S[14]
    P[13] = S[22]
    P[15] = S[30]
    P[8] = S[38]
    P[10] = S[46]
    P[12] = S[54]
    P[14] = S[62]
    P[1] = S[7]
    P[3] = S[15]
    P[5] = S[23]
    P[7] = S[31]
    P[0] = S[39]
    P[2] = S[47]
    P[4] = S[55]
    P[6] = S[63]

    return ''.join(P)

def encryptDES():
    return 

# def decryptDES():

if __name__ == "__main__":
    print(initPermute("0001000010110111011001111100001110010101101110000100010000001011"))
=======
# this function returns the input left shifted once
def left_shift(to_shift):
	tmp = to_shift[0]
	to_shift = to_shift[1:]
	to_shift = to_shift+(tmp)
	return to_shift

# the following permutation functions take in a string as the argument and handles the permutation via concatenation

# the following 2 permutation functions are for the key generation
def p10(initial_p): # permutation for 10 bit keys
	# 3 5 2 7 4 10 1 9 8 6
	final_p = initial_p[2] + initial_p[4] + initial_p[1] + initial_p[6] + initial_p[3] + initial_p[9] + initial_p[0] + initial_p[8] + initial_p[7] + initial_p[5]
	return final_p

def p8(initial_p): 
	# 6 3 7 4 8 5 10 9
	final_p = initial_p[5] + initial_p[2] + initial_p[6] + initial_p[3] + initial_p[7] + initial_p[4] + initial_p[9] + initial_p[8]
	return final_p

# these permutations are used in the actual encryption/decryption
def initial_p(initial_p): # initial permutation
	# 2 6 3 1 4  8 5 7
	final_p = initial_p[1] + initial_p[5] + initial_p[2] + initial_p[0] + initial_p[3] + initial_p[7] + initial_p[4] + initial_p[6]
	return final_p

def inverseInitialP(initial_p):
	# 2 4 3 1
	final_p = initial_p[1] + initial_p[3] + initial_p[2] + initial_p[0]
	return final_p

# the following 2 functions act as the s boxes
def s0(initial4bit):
	# grab the letters at respective indices and concatenate and convert to base 2 int
	row = int((initial4bit[1]+initial4bit[2]),2)
	col = int((initial4bit[0]+initial4bit[3]),2)

	s0_box = [[1, 0, 3, 2],\
			  [3, 2, 1, 0],\
			  [0, 2, 1, 3],\
			  [3, 1, 3, 2]]

	# get the value from s box of calculated row and col
	s_val = s0_box[row][col]
	# convert to binary
	bin_sval = bin(s_val)

	# return 4 bit val
	return bin_sval[2:].zfill(2)


def s1(initial4bit):
	# grab the letters at respective indices and concatenate and convert to base 2 int
	row = int((initial4bit[1]+initial4bit[2]),2)
	col = int((initial4bit[0]+initial4bit[3]),2)

	s1_box = [[0, 1, 2, 3],\
			  [2, 0, 1, 3],\
			  [3, 0, 1, 0],\
			  [2, 1, 0, 3]]

	# get the value from s box of calculated row and col
	s_val = s1_box[row][col]
	# convert to binary
	bin_sval = bin(s_val)

	# return 4 bit val
	return bin_sval[2:].zfill(2)


def f_func(x, k):
	# first expand/permutate x
	# 4 1 2 3
	first_x = x[3] + x[0] + x[1] + x[2]

	# 2 3 4 1
	last_x = x[1] + x[2] + x[3] + x[0]

	# concatenate and xor new value with key after converting to int base 2
	total_p = first_x + last_x
	xor_ed = int(total_p,2) ^ int(k,2) 
	xor_ed = "{:b}".format(xor_ed) # convert to binary

	# make sure its still 4 digits
	first4 = xor_ed[:4].zfill(4)
	last4 = xor_ed[4:].zfill(4)

	# pass to respective s boxes
	s0_val = s0(first4)
	s1_val = s1(last4)

	# concatenate
	sol = s0_val + s1_val

	# last permutation
	p4 = inverseInitialP(sol)

	return p4


def generateKeys(key10bit):
	# generate K1, K2 

	# permutate
	perm10 = p10(key10bit)

	first5 = perm10[:5]
	last5 = perm10[5:]

	# shift left and find k1
	shifted_first = left_shift(first5)
	shifted_last = left_shift(last5)

	k1 = p8(shifted_first + shifted_last)

	# shift left again and find k2
	shifted_first = left_shift(shifted_first)
	shifted_last = left_shift(shifted_last)

	k2 = p8(shifted_first + shifted_last)

	return k1, k2



def encrypt(plaintext, k1, k2):
    listobits = []
    tmp = ""
    for i in plaintext:
        tmp+=i
        if len(tmp) == 64:
            listobits.append(tmp)
            tmp = ""

    if len(tmp)>0:
        tmp = "{:b}".format(tmp).zfill(64)
        listobits.append(tmp)

    cipher = ""
    for i in listobits:
        cipher += encrypt64(i, k1, k2)

    print("Here is the encrypted cipher text: "+cipher)
    return cipher


def encrypt64(bits64, k1, k2):
    # implement initial permutation
	permutation = initial_p(bits64)

	# split
	first = permutation[:32]
	last = permutation[32:]

	# send the latter to the f function with first key
	f_last4 = f_func(last, k1)

	# xor new value with key after converting to int base 2
	xor1 = int(first,2) ^ int(f_last4,2) 
	xor1 = "{:b}".format(xor1).zfill(4)

	# send to f function with second key
	f_xor1 = f_func(xor1, k2)

	# xor the returned value with the original latter half
	xor2 = int(f_xor1,2) ^ int(last4,2) 
	xor2 = "{:b}".format(xor2).zfill(4)

	# concatenate
	final = str(xor2) + str(xor1) 

	#final permutation
	# 4 1 3 5 7 2 8 6
	cipher_text = final[3] + final[0] + final[2] + final[4] + final[6] + final[1] + final[7] + final[5]


def decrypt(cipher, k1, k2):
	listobits = []
    tmp = ""
    for i in cipher:
        tmp+=i
        if len(tmp) == 64:
            listobits.append(tmp)
            tmp = ""

    plaintext = ""
    for i in listobits:
        plaintext += decrypt64(i, k1, k2)

    print("Here is the decrypted plain text: "+plaintext)
    return plaintext

def decrypt64(i, k1, k2):
>>>>>>> a0a4c5cd3008acb12ab7a994585f882265eb5895
