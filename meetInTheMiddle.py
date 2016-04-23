import subprocess
import sys
import itertools
import gDES

Khex = ['FEDCBA9876543210', 'FEDCBA9876543211'] # keys for both DES iterations
PT = '6100000000000000'

print PT
r = gDES.DESstuff(PT, Khex[0], 'encrypt') + ' '
CT = gDES.DESstuff(r, Khex[1], 'encrypt') + ' '
print CT


keyChars = '0123456789abcdef'
keyLen = 16
gen = itertools.product(keyChars, repeat=keyLen)
for keyvals in gen:
	key = ''.join(keyvals)
	#print key
	print "ENCRYPT: " + gDES.DESstuff(PT, key, 'encrypt') + "  :  " + key
	print "DECRYPT: " + gDES.DESstuff(CT, key, 'decrypt') + "  :  " + key