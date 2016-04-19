import hashlib
import sys
if len(sys.argv) != 3:
	print "Provide the filename containing each string and an output filename"
else:
	lines = [line.rstrip('\n') for line in open(sys.argv[1])]
	hashout  = open(sys.argv[2], "w")
	for line in lines:            
	    m = hashlib.md5()
	    m.update(line)
	    hashout.write(m.hexdigest())
	    hashout.write("\n")