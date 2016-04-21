import subprocess
import sys
import itertools

KEYstart = 0x0000000000000000  # hex literal, gives us a regular integer
KEYend = 0xFFFFFFFFFFFFFFFF

if len(sys.argv) !=2:
  print "Please give the plaintext"
else:
	PT = sys.argv[1]	
	proc=subprocess.Popen('python gDES.py ' + PT + ' encrypt 1', shell=True, stdout=subprocess.PIPE, )
	CT=proc.communicate()[0].strip('\n')
	print CT
	print KEYend

	'''for x in range(len(KEYstart)):
		for i in xrange(0x0, 0xF + 1):
	    print hex(i)[2:]'''
	keyChars = '0123456789abcdef'
	keyLen = 16
	gen = itertools.product(keyChars, repeat=keyLen)
	for keyvals in gen:
		key = ''.join(keyvals)
		print key
		'''res=subprocess.Popen('python gDES.py ' + PT + ' encrypt 1 ' + key, shell=True, stdout=subprocess.PIPE, )
		print res.coomunicate()[0].strip('\n')'''
		'''res=subprocess.Popen('python gDES.py ' + CT + ' decrypt 1 ' + key, shell=True, stdout=subprocess.PIPE, )
		print res.coomunicate()[0].strip('\n')'''
