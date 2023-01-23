file=open("text.txt","r")
content=file.readlines()
for s in content:
    print(s.strip())
