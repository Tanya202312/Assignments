try:
    fname = input("Enter the file name : ")
    fhand = open(fname)
    count = 0
    sum = 0
    average = 0
    for line in fhand:
        if line.startswith("X-DSPAM-Confidence:"):
            line = float(line.split(':')[-1])      
            try:
                sum = sum + line
                count += 1
                average = sum / count      
            except ValueError:
                pass     
    print("The average is: %.4f" % average)       
    fhand.close()
except FileNotFoundError:
    print("Error! File does not exist")   