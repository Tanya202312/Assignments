fhand = open("mbox.txt", "r")
count = 0
mail = 0
for line in fhand:
    if line.startswith("From "):
        line = line.rstrip()
        count = count + 1
        atpos = line.find(" ")
        sppos = line.find(" ",10,)   
        mail = line[atpos+1:sppos]      
        print(mail)
print('Total %d mails printed' % count)    
fhand.close()