import itertools
import gDES

Khexs = ['0000000000001255', '000000000000125c'] # keys for both DES iterations
PT = '6100000000000000'
enc = {}
dec = {}
r = gDES.DESstuff(PT, Khexs[0], 'encrypt') + ' '
CT = gDES.DESstuff(r, Khexs[1], 'encrypt') + ' '
CT = CT.zfill(17)

keyChars = '0123456789abcdef'
keyLen = 16
gen = itertools.product(keyChars, repeat=keyLen)
i =0
for keyvals in gen:
	if i > 4700:
		break
	key = ''.join(keyvals)
	res = gDES.DESstuff(PT, key, 'encrypt')
	enc[res] = key
	res = gDES.DESstuff(CT, key, 'decrypt')
	dec[res] = key
	i += 1

print "\nRESULTS:"
for data, key in dec.items():
	if enc.get(data) != None:
		print "THE FIRST KEY IS:\t" + enc.get(data)
		print "THE SECOND KEY IS:\t" + key

