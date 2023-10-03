def grade(yourscore):
    if yourscore > 100:
        print("Error, please enter numeric input between 0 and 100")
    elif yourscore >= 90 and yourscore <= 100:
        print("your grade is A")
    elif yourscore >= 80 and yourscore < 90:
        print("your grade is B")
    elif yourscore >= 70 and yourscore <= 79:
        print("your grade is C")
    elif yourscore >= 60 and yourscore <= 69:
        print("your grade is D")
    elif yourscore >= 0 and yourscore <= 59:
        print("your grade is F")
    elif yourscore < 0:
        print("Error, please enter numeric input between 0 and 100 ")
    
try:
    yourscore=int(input("Enter score: "))
    grade(yourscore)
    print(" ")
except:
    print("Error, please enter numeric input between 0 and 100")