sum=0
count=0
while True:
    value=input("Enter a number: ")
    if value == "done" :
        break
    try:
        x=int(value)
    except:
        if value :=str(value):
            print("Error! Enter a numerical value ")
        continue
    count=count + 1
    sum= sum + x
    average=sum / count
print("DONE")
print("sum of input numb: ", sum )
print("number of input: ", count  )
print("average of input numbers: ", average )

