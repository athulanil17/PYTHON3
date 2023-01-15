file=open('text.txt','r')
n=int(input("Enter the lines to be read:"))
for i in range(n):
    print(file.readline())