while True:
    str1=str(input("Please enter  string: "))
    if str1 == "done":
        break
    else:
        str1 = str1.upper().replace(".", "").replace(",","").replace(":","").replace("!","").replace("?", "")
        print(str1)
print("Bye!")  