file = open("user.txt","a")

file.write("\nLike language : Python")

file.close()

file = open("user.txt","r")

text = file.read()

print(text)

file.close()