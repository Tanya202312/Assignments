def num_divide3(mylist):
    for k in range(len(mylist)):
        mylist[k] =mylist[k] / 3
        
        

if __name__ == '__main__':
    while True:
        number = input("enter a number ")
        if number == "done":
            break
        
        try:
            number = int(number)
            if number < 0:
                print("Error! Enter a positive number")
                continue
        except:
            if number := str(number):
                print("Error! Enter a numerical value ")
            continue
            
        scorelist = range(1, number + 1)
        scorelist = list(scorelist)
        num_divide3(scorelist)
        scorelist = len(scorelist)
        scorelist = int(scorelist / 3)
        print("numbers divisible by 3 among numbers from 1 to ",number, "= " , scorelist)
    print("bye!")
