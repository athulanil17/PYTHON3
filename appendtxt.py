file=open("text.txt","a")
txt=str(input("Enter text to be added: "))
file.write(txt)
file.close()
file=open("text.txt","r")
print(file.read())
