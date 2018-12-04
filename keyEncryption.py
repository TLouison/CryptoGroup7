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

def perm32(P):
    s = ""
    s = P[32: 1] + P[ 2: 5] + P[ 4: 5] + P[ 6: 9] + P[ 8: 9] + P[10:13] + P[12:13] + P[14:17] + P[16:17] + P[18:21] + P[20:21] + P[22:25] + P[24:25] + P[26:29] + P[28:29] + P[30: 1]
    return s

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
def s0(initial32bit):
	# grab the letters at respective indices and concatenate and convert to base 2 int
	row = int((initial32bit[1]+initial32bit[-1]),2)
	col = int((initial32bit[2:-1]),2)

	s0_box = [ [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]  \
                [ 0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8]\
                [ 4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0]\
                [ 15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

   
	# get the value from s box of calculated row and col
	s_val = s0_box[row][col]
	# convert to binary
	bin_sval = bin(s_val)

	# return 4 bit val
	return bin_sval[2:].zfill(2)


def s1(initial32bit):
	# grab the letters at respective indices and concatenate and convert to base 2 int
	row = int((initial32bit[1]+initial32bit[-1]),2)
	col = int((initial32bit[2:-1]),2)

	s1_box = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10]    \
                [ 3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5] \
                [ 0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15]
                [ 13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

	# get the value from s box of calculated row and col
	s_val = s1_box[row][col]
	# convert to binary
	bin_sval = bin(s_val)

	# return 4 bit val
	return bin_sval[2:].zfill(2)


def f_func(x, k):

	# concatenate and xor new value with key after converting to int base 2
	total_p = perm32(x)
	xor_ed = int(total_p,2) ^ int(k,2) 
	xor_ed = "{:b}".format(xor_ed) # convert to binary

	# make sure its still 4 digits
	first = xor_ed[:32].zfill(32)
	last = xor_ed[32:].zfill(32)

	# pass to respective s boxes
	s0_val = s0(first)
	s1_val = s1(last)

	# concatenate
	sol = s0_val + s1_val

	# last permutation
	p = inverseInitialP(sol)

	return p


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
	permutation = initPermute(bits64)

	# split
	first32 = permutation[:32]
	last32 = permutation[32:]

	# send the latter to the f function with first key
	f_last32 = f_func(last32, k1)

	# xor new value with key after converting to int base 2
	xor1 = int(first,2) ^ int(f_last32,2) 
	xor1 = "{:b}".format(xor1).zfill(32)

	# send to f function with second key
	f_xor1 = f_func(xor1, k2)

	# xor the returned value with the original latter half
	xor2 = int(f_xor1,2) ^ int(last32,2) 
	xor2 = "{:b}".format(xor2).zfill(32)

	# concatenate
	final = str(xor2) + str(xor1) 

	#final permutation
	cipher_text = initPermute(final)


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
    # implement initial permutation
	permutation = initPermute(bits64)

	# split
	first32 = permutation[:32]
	last32 = permutation[32:]

	# send the latter to the f function with second key
	f_last32 = f_func(last32, k2)

	# xor new value with key after converting to int base 2
	xor1 = int(first4,2) ^ int(f_last32,2) 
	xor1 = "{:b}".format(xor1).zfill(32)

	# send to f function with first key
	f_xor1 = f_func(xor1, k1)

	# xor the returned value with the original latter half
	xor2 = int(f_xor1,2) ^ int(last32,2) 
	xor2 = "{:b}".format(xor2).zfill(32)

	# concatenate
	final = str(xor2) + str(xor1) 

	# final permutation
	plain_text = initPermute(final)
	print("Here is the decrypted plain text: "+plain_text)
	return plain_text
