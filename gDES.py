import sys
#TODO get user message input
#TODO convert said user message input into hex (base 16)
#	s = user message input
#	hex_chars = map(hex,map(ord,s))
#	or
#	s.encode('hex_codec')

#m = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0A\x0B\x0C\x0D\x0E\x0F'
Khex = ['FEDCBA9876543210', 'FEDCBA9876543211'] # keys for both DES iterations

'''Initial key permutation'''
PC1 = [[57, 49, 41, 33, 25, 17, 9],
      [1, 58, 50, 42, 34, 26, 18],
      [10, 2, 59, 51, 43, 35, 27],
      [19, 11, 3, 60, 52, 44, 36],
      [63, 55, 47, 39, 31, 23, 15],
      [7, 62, 54, 46, 38, 30, 22],
      [14, 6, 61, 53, 45, 37, 29],
      [21, 13, 5, 28, 20, 12, 4]]

'''number of left shifts to make to create the 16 sets of left and right key halves'''
LSHIFTS = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]

'''permutation to get the 16 keys'''
PC2 = [[14, 17, 11, 24, 1, 5],
       [3, 28, 15, 6, 21, 10],
       [23, 19, 12, 4, 26, 8],
       [16, 7, 27, 20, 13, 2],
       [41, 52, 31, 37, 47, 55],
       [30, 40, 51, 45, 33, 48],
       [44, 49, 39, 56, 34, 53],
       [46, 42, 50, 36, 29, 32]]

'''Initial permutation for M'''
IP = [[58, 50, 42, 34, 26, 18, 10, 2],
      [60, 52, 44, 36, 28, 20, 12, 4],
      [62, 54, 46, 38, 30, 22, 14, 6],
      [64, 56, 48, 40, 32, 24, 16, 8],
      [57, 49, 41, 33, 25, 17, 9, 1],
      [59, 51, 43, 35, 27, 19, 11, 3],
      [61, 53, 45, 37, 29, 21, 13, 5],
      [63, 55, 47, 39, 31, 23, 15, 7]]

'''part of the process for developing the right half of the encoded message'''
EBIT = [[32, 1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8, 9],
        [8, 9, 10, 11, 12, 13],
        [12, 13, 14, 15, 16, 17],
        [16, 17, 18, 19, 20, 21],
        [20, 21, 22, 23, 24, 25],
        [24, 25, 26, 27, 28, 29],
        [28, 29, 30, 31, 32, 1]]

'''part of the process for devloping the right half of the encoded message'''
S1 = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
      [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
      [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
      [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]

S2 = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
      [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
      [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
      [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]

S3 = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13 ,12, 7, 11, 4, 2, 8],
      [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
      [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
      [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]

S4 = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
      [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
      [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
      [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]

S5 = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
      [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
      [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
      [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]

S6 = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
      [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
      [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
      [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]

S7 = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
      [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
      [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
      [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]

S8 = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
      [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
      [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15 ,3, 5, 8],
      [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]


'''the final permutation used to calculate the right side of the encoded message'''
P = [[16, 7, 20, 21],
     [29, 12, 28, 17],
     [1, 15, 23, 26],
     [5, 18, 31, 10],
     [2, 8, 24, 14],
     [32, 27, 3, 9],
     [19, 13, 30, 6],
     [22, 11, 4, 25]]

'''The final permutation after switching the left and right sides of the 16th permutation of the encoded message'''
IP1 = [[40, 8, 48, 16, 56, 24, 64, 32],
       [39, 7, 47, 15, 55, 23, 63, 31],
       [38, 6, 46, 14, 54, 22, 62, 30],
       [37, 5, 45, 13, 53, 21, 61, 29],
       [36, 4, 44, 12, 52, 20, 60, 28],
       [35, 3, 43, 11, 51, 19, 59, 27],
       [34, 2, 42, 10, 50, 18, 58, 26],
       [33, 1, 41, 9, 49, 17, 57, 25]]



'''Takes in a message in hex format and returns it as a binary string'''
def getBinFromHex(message):
	m = ''
	for char in message:
		m = m + bin(int('1'+char, 16))[3:]
	return m

'''Returns the left half of a given string'''
def getLeftHalf(message):
	return message[:len(message)/2]

'''Returns the right half of a given string'''
def getRightHalf(message):
	return message[len(message)/2:]

'''takes in a string and a 2D list (table). The given string at the index of the table's first index is the first value of the return string. 
The given string at the index of the table's second index is the second value of the return string. etc...'''
def doPerm(message, perm):
	res = ''
	for row in perm:
		for ele in row:
			res = res + message[ele-1]
	return res

'''Takes in a string and a number where it shifts the first n number of characters from the string and puts them on the end'''
def doShifts(message, shiftVal):
	popped = message[:shiftVal]
	message = message[shiftVal:] + popped
	return message

'''performs xor on two given strings of the same length'''
def xorVals(message1, message2):
	res = ''
	if len(message1) != len(message2):
		return "ERROR"
	for i in range(len(message1)):
		if message1[i] == message2[i]:
			res = res + '0'
		else:
			res = res + '1'
	return res

'''Takes a string and a number where the string is split on every nth character and returned as a list'''
def splitInput(message, val):
	return [message[i:i+val] for i in range(0, len(message), val)]

'''Takes the first and last binary to create the row number and the middle four binaries to create the column number. 
This is done eight times and the value at the cooresponding table is appended (in binary) to the returned result'''
def doRCperm(message):
	res = ''
	i = 0
	for val in message:
		x = val[0] + val[5]
		xdec = int(x, 2)
		y = val[1] + val[2] + val[3] + val[4]
		ydec = int(y, 2)
		
		if i == 0:
			res = res + str(bin(S1[xdec][ydec])[2:].zfill(4))
		elif i == 1:
			res = res + str(bin(S2[xdec][ydec])[2:].zfill(4))
		elif i == 2:
			res = res + str(bin(S3[xdec][ydec])[2:].zfill(4))
		elif i == 3:
			res = res + str(bin(S4[xdec][ydec])[2:].zfill(4))
		elif i == 4:
			res = res + str(bin(S5[xdec][ydec])[2:].zfill(4))
		elif i == 5:
			res = res + str(bin(S6[xdec][ydec])[2:].zfill(4))
		elif i == 6:
			res = res + str(bin(S7[xdec][ydec])[2:].zfill(4))
		elif i == 7:
			res = res + str(bin(S8[xdec][ydec])[2:].zfill(4))
		i+=1
	return res


def DESstuff(MESSAGE, Khex, crypt):
  K = ''  #key in binary
  M = ''  #message in binary form
  L = ''  #left half of message
  R = ''  #right half of message

  KP = '' #permutated key
  C =[] #left half of permutated keys
  D = []  #right half of permutated keys
  KN = [] #the 16 subkeys

  MIP = ''  #message after IP
  LN = []   #left halves of the message
  RN = []   #right halves of the message
  E = []    #holds part of the value for the right sides of the encoded message
  KaE = []  #xor results of KN and E
  SBOX = [] #holds the sbox output values for the right sides of the encoded message
  PN = []   #holds the results of the P permutation
  RL = ''   #holds the message where right and left sides are switched
  CBIN = '' #holds the encrypted message in binary format
  CHEX = '' #holds the encrypted message in hex format


  '''Assign the initial message to M in binary form'''
  M = getBinFromHex(MESSAGE)
  #print 'M: ' + M


  '''==================================================== START Key Development ===================================================='''
  '''Assign the initial key to K in binary form'''
  K = getBinFromHex(Khex)
  #print 'K: ' + K
  #print 'K: 0001001100110100010101110111100110011011101111001101111111110001'

  '''Assign L and R to their respective halves of the message'''
  L = getLeftHalf(M)
  R = getRightHalf(M)
  #print 'L + R: ' + L + R
  #print 'L: ' + L
  #print 'R: ' + R

  '''Do an initial permuation on the key with the given table'''
  KP = doPerm(K, PC1)
  #print 'KP: ' + KP

  '''Assign the halves of the permutated key to C (left) and D (right)'''
  C.append(getLeftHalf(KP))
  D.append(getRightHalf(KP))

  '''Shift the halves based off the given table and assign the halves to the C and D lists'''
  i=0
  for val in LSHIFTS:
  	C.append(doShifts(C[i], val))
  	D.append(doShifts(D[i], val))
  	i+=1

  #for i in range(len(C)):
  	#print "C" + str(i) + ": " + C[i]
  	#print "D" + str(i) + ": " + D[i]

  '''Combine each of the two halves (from C and D) and do a permutation with the given table and assign each as a unique subkey in KN'''
  for i in range(16):
  	KN.append(doPerm(C[i+1] + D[i+1], PC2))
  if crypt == 'decrypt':
    tempKN = []
    x = 15
    while x >= 0:
      tempKN.append(KN[x])
      x-=1
    KN = tempKN

  #for i in range(len(KN)):
  	#print "KN" + str(i) + ": " + KN[i]


  '''==================================================== END Key Development ===================================================='''

  '''==================================================== START Block Encoding ===================================================='''

  '''Assign MIP to the result of M and the Initial Permutation'''
  MIP = doPerm(M, IP)
  #print 'MIP: ' + MIP

  LN.append(getLeftHalf(MIP))
  RN.append(getRightHalf(MIP))

  #print 'LN + RN: ' + LN[0] + RN[0]
  #print 'LN: ' + LN[0]
  #print 'RN: ' + RN[0]


  for i in range(1,17):
  	LN.append(RN[i-1])						# the left half is equal to the previous right half
  	E.append(doPerm(RN[i-1], EBIT))			# part of the right half where the permutation is performed on the previous right half
  	KaE.append(xorVals(KN[i-1], E[i-1]))	# part of the right half where the key and E are xor together
  	KaEsplit = splitInput(KaE[i-1], 6)		# splits the values by every 6th character
  	SBOX.append(doRCperm(KaEsplit))			# gets the sbox output
  	PN.append(doPerm(SBOX[i-1], P))			# performs the last permutation needed for the right half
  	RN.append(xorVals(LN[i-1], PN[i-1]))	# adds the result of the xor of the previous left side and the permutation to the right side

  RL = RN[16] + LN[16]	# combines the last right side with the last left side, but in reverse (right then left)
  #print "RL: " + RL

  CBIN = doPerm(RL, IP1)	# the last permutation to create the ciphertext in binary
  CHEX = hex(int(CBIN, 2))[2:]	# Converts the ciphertext into hex
  x = 0
  for val in CHEX:
    if val == 'L':
      CHEX = CHEX[:i] + CHEX[i+1:]
    x+=1
  #print CBIN
  #print CHEX
  return CHEX


  '''==================================================== END Block Encoding ===================================================='''



'''print 'Number of arguments:', len(sys.argv), 'arguments.'
print 'Argument List:', str(sys.argv)'''
if len(sys.argv) !=3:
  print "Please give the message to be used then encrypt/decrypt"
elif sys.argv[2] != 'encrypt' and sys.argv[2] != 'decrypt':
  print "Please give the message to be used then e/d"
else:
  MESSAGE = sys.argv[1]
  crypt = sys.argv[2]
  if crypt == 'encrypt':
    MESSAGE = MESSAGE.encode("hex")
  elif crypt == 'decrypt':  # already in hex
    MESSAGE = MESSAGE.replace(" ", "") # in case it comes sparated with spaces
  MESSAGES = splitInput(MESSAGE, 16)
  if len(MESSAGES[len(MESSAGES) - 1]) != 16:  # add padding if not at full 16 length
    for i in range(len(MESSAGES[len(MESSAGES) - 1]), 16):
	    MESSAGES[len(MESSAGES)-1] = MESSAGES[len(MESSAGES)-1] + '0'  # pad with 0's
  fullDES = ''
  for mess in MESSAGES:
    r = DESstuff(mess, Khex[0], crypt) + ' '
    r = DESstuff(r, Khex[1], crypt) + ' '
    if crypt == 'decrypt':
      r = r.strip() #get rid of trailing spaces 
      r = ''.join(chr(int(r[i:i+2], 16)) for i in range(0, len(r), 2))  # converts from hex to ASCII
    fullDES = fullDES + r
  print fullDES





