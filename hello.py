print("Hello")

name = input("Name: ")

age = input("Age: ")

city = input("City: ")

string = "Your name is {} and you are {} years old. You live in{}"

output = string.format(name,age,city)

print(output)               