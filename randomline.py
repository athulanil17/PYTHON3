import random
with open("text.txt","r") as file:
    content=file.read().splitlines()
print(random.choice(content))
    