name = input("Введите имя: ")
age = input("Input age: ")
city = input("Input city: ")

file = open("user.txt", "w")

file.write("Name :"+ name+"\n")
file.write("Age :"+ age+"\n")
file.write("City :"+ city)

file.close()