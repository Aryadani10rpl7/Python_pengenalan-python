# Koding Casting data types
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is",
type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is",
type(str_numbers_to_int))

integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is",
type(integer_to_str))

num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0

num_bool = bool(num_int)
print(num_bool, type(num_bool))

#Koding Input Output
name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

#if-else
try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print("Damn you've got a magna cumlaude with your ",your_GPA,
            " GPA")
        elif 3.50 <= your_GPA < 3.80:
            print("Cool!! You've got a cumlaude with your ",your_GPA," GPA")
        elif 3.00 <= your_GPA < 3.50:
            print("You've got a stable GPA tho")
        elif your_GPA < 3.0:
            print("You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")

#Using match case
try:
    status_code = int(input("Enter your status code: "))
    print("Your code means")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
except :
    print("Please enter a valid status code")

#Using Loops
for i in range(5):
    print(i)
    0
    1
    2
    3
    4

for i in range(5):
    print("Data science is easy!")
print(50*"=")
for i in range(1, 5, 2):
    print("Data science is easy!")

##Keyword control
for i in range(5):
    if i == 2:
        continue
    if i == 4:
        break
    print(i)