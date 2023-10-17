try:
    fname = input("Enter the file name: ")
    fhand = open(fname)
    line = fhand.read()
    line = line.upper()
    print(line)  
    fhand.close()
except FileNotFoundError:
    print("Error! File does not exist")    
    



