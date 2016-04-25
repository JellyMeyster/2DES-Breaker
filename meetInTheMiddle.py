import itertools
import gDES

Khexs = ['0000000000001255', '000000000000125c'] # keys for both DES iterations
PT = '6100000000000000'
enc = {} # Dictionary for the encrypting table
dec = {} # Dictionary for the decrypting table
r = gDES.DESstuff(PT, Khexs[0], 'encrypt') + ' ' # first round of 2DES
CT = gDES.DESstuff(r, Khexs[1], 'encrypt') + ' ' # second round of 2DES
CT = CT.zfill(17) # padding

keyChars = '0123456789abcdef' # all hex values for itertools
keyLen = 16 # length of the keys to bruteforce
gen = itertools.product(keyChars, repeat=keyLen) # generate all keys
i =0
for keyvals in gen: # for each of the keys, lets do stuff
	if i > 4700: # for testing purposes, only care about the first 4700 keys
		break
	key = ''.join(keyvals) # key in string format
	res = gDES.DESstuff(PT, key, 'encrypt') # encrypt the plaintext with each key
	enc[res] = key # add encrypted value to dictionary with the key
	res = gDES.DESstuff(CT, key, 'decrypt') # decrypt the ciphertext with each key
	dec[res] = key # add decrypted value to dictionary with the key
	i += 1

print "\nRESULTS:"
for data, key in dec.items(): # go through each encrypted value and its key of the decrypted dictionary
	if enc.get(data) != None: # if it exists
		print "THE FIRST KEY IS:\t" + enc.get(data) # the corresponding key from the decrypted dictionary
		print "THE SECOND KEY IS:\t" + key # the key from the decrypted dictionary
