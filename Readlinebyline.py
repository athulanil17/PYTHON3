f= open("text.txt")
content_list = f.readlines()
content_list = [x.strip() for x in content_list]
print(content_list)
print(type(content_list))
