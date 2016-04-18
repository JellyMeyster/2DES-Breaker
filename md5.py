import hashlib
lines = [line.rstrip('\n') for line in open('C:\Users\U53r\Desktop\Crypto\password.txt')]
hashout  = open("C:\Users\U53r\Desktop\Crypto\md5.txt", "w")
for line in lines:            
    m = hashlib.md5()
    m.update(line)
    hashout.write(m.hexdigest())
    hashout.write("\n")