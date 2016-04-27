import hashlib
import sys
from os import urandom

salt = ""
salt_length = 0
pass_length = 0
diff = 0

if len(sys.argv) != 5:
	print "Provide the filename containing each string, an output filename and a salt if applicable."
else:
	go_salt = sys.argv[3].rstrip('\n')
	pass_length = int(sys.argv[4].rstrip('\n'))
	lines = [line.rstrip('\n') for line in open(sys.argv[1])]
	hashout  = open(sys.argv[2], "w")
	for line in lines:
		if go_salt == "y":
			if len(line) < pass_length:
				diff = pass_length - len(line)
				salt_length =  diff/2     
			salt = urandom(salt_length).encode('hex')
		m = hashlib.md5() 
		m.update(line + salt)
		hashout.write(m.hexdigest())
		hashout.write("\n")
