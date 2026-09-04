print("=============================")
print('Welcome here')
print('My first post!')
print('=============================')

username =  "cool creator"
bio = "Fun Blogger"
followers = "100"

print('Username:', username)
print("Bio:", bio)
print("Followers:", followers)

username = "lame creator"

print('Username:', username)

followers = 100 

followers += 50
print("Day 1:", followers)

followers += 20
print("Day 2:", followers)

followers += 10
print("Day 3:", followers)


followers -= 5
print("Day 4:", followers)

username = input("Enter Username: ")
age = input("Enter age: ")
category = input("Enter Content Category: ")

print("\nInstagram Profile")
print("======================")
print("Username:", username)
print("Age:", age)
print("Category: ", category)
print("======================")

username = input("Enter Username: ")
age = int(input("Enter Age:"))
category =input("Enter content category: ")

print("\nInstagram Profile")
print("======================")
print("Username:", username)
print("Age:", age)
print("Category: ", category)
print("======================")

if age>40 and category == "fun":
    print("You are old what is fun for you?")