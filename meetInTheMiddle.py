import subprocess
import sys
import itertools

if len(sys.argv) !=2:
  print "Please give the plaintext"
else:
	PT = sys.argv[1]	
	proc=subprocess.Popen('python gDES.py ' + PT + ' encrypt 2', shell=True, stdout=subprocess.PIPE, )
	CT=proc.communicate()[0].strip('\n')
	print CT

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
