phrase= str(input("Please enter string: "))
upper, lower, numbers, other = 0, 0, 0, 0
for i in phrase:
    if i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        numbers += 1
    else:
        other += 1
print("uppercase letters", upper, "\nlowercase letters",lower, "\nnumbers", numbers,"\nother characters", other)        
    