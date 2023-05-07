email = input("email: ").strip()

#slice user name
user = email[:email.index("@")]

#slice domain name
domain = email[email.index("@") + 1 :]

#format message
output = "Your username is {} and your domain name is {}".format(user,domain)

print(output)