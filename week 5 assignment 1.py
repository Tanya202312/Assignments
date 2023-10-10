while True:
    try:
        words = str(input("Enter two words: "))
        if words == "done" or not words:
            break
        word1, word2 = words.split()
        list= [word1, word2]
        list.sort()
        print(list[0], "comes first")
    except ValueError:     
        continue 
     
print("bye!") 