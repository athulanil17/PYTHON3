with open("text.txt", 'r') as f:
    words = f.read().split()

max_len = len(max(words,key=len))

for word in words:
    if len(word) == max_len:
        print("The largest word is:", word)
        break