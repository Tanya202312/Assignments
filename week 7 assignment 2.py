file = open("romeo.txt", "r")
unique_words = []
for line in file:
    words = line.split()
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
unique_words.sort()
print(list(unique_words))