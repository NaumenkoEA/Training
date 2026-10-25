file = open("user.txt","w")


file.write("Имя: Evgenii\n")
file.write("Возраст: 23\n")
file.write("Город: Solihorsk")
file.close()

file = open("user.txt","r")
text = file.read()

print(text)

file.close()