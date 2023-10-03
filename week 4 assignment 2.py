def computePay (Hours,Rate):
    Pay=Hours*Rate
    if Hours <= 40:
        Pay = Hours * Rate
        print("Your pay is ", Pay)
    elif Hours > 40:
        Rate1 = Rate * 1.5
        Salary= 40 * Rate + (Hours - 40) * Rate1
        print("Your salary is ", Salary)  
    

try:
    Hours = int(input("Enter hours "))
    Rate = float(input("Enter rate "))
    computePay(Hours,Rate)
    print(" ")
except:
    print("Error! Please enter numeric input")    