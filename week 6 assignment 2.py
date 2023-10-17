fhand = open("mbox.txt", "r")
count = 0
host = 0
for line in fhand:
    if line.startswith("From:"):
        line = line.rstrip()
        count = count + 1
        atpos = line.find("@")
        sppos = line.find("\n", atpos)      
        host = line[atpos+1:sppos]      
        print(host)
print('Total %d hosts printed' % count)    
fhand.close()