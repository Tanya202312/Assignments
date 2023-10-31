my_list= []
while True:
    try:
        integers = input("Please enter an integer ")
        if integers != "done":
            sum = 0
            integers = int(integers)
            my_list.append(integers)
            for i in my_list:
                sum += i
            average = sum / len(my_list)
            print(my_list,"average = ", " %.2f" % average)
        else:
            print("Bye!")
            break
    except ValueError:
        continue