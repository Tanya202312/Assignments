try:
    Hours=int(input("Enter hours "))
    Rate=float(input("Enter rate "))
except:
    print("Enter a number")   
else:
    if Hours > 40:
        Rate1 = Rate * 1.5
        Salary= 40 * Rate + (Hours - 40) * Rate1
        print("Your salary is ", Salary)  
    else:
        if Hours <= 40:
            Salary= Hours * Rate
            print("Your salary is ", Salary) 

 