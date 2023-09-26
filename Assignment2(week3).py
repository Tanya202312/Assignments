try:
  score = int(input("Enter the test score ==> "))  
except:
    print("Error, please enter numeric input between 0 and 100")
else:
   if score > 100:
    print("Error, please enter numeric input between 0 and 100")
   else:
    if score >= 90:
      print("your grade is A")
    else:
      if score >= 80:
        print("your grade is B")
      else:
        if score >= 70:
          print("your grade is C")
        else:
          if score >= 60:
            print("your score is D")
          else:
            if score >= 0:
              print("your grade is F")
            else:
              if score < 0:
                print("Error, please enter numeric input between 0 and 100")  
           


  
       



  
      