import hashlib
lines = [line.rstrip('\n') for line in open('your password file path')]
hashout  = open("your output file path", "w")
for line in lines:            
    m = hashlib.md5()
    m.update(line)
    hashout.write(m.hexdigest())
    hashout.write("\n")