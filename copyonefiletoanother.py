with open("text.txt","r") as f:
    with open("TEXT2.txt","w") as f2:
        data=f.read()
        f2.write(data)
    print("file copied successfully")