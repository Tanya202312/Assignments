word = str(input("Enter string: "))
print("Input string: ", word)
for letter in word:
    index = len(word) -1
while index >= 0:
    print(word[index])
    index= index - 1    
   