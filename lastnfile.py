file=open("text.txt","r")
lines=file.readlines()
num=int(input("Enter the limit:"))
last_lines=lines[-num:]
print(last_lines.strip())