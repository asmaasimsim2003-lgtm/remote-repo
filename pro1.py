import random
import string
print("welcom the password generated")
password=int(input("enter the total num of charters in the password:"))
letter=int(input("enter the num of letters in the password:"))
num=int(input("enter the num of the password:"))
sympol=int(input("enter num of symbol in the password:"))
if password!=(letter + num + sympol):
    print("invalid num .the sum of letters , number, and symbol does not  match the password")
else:
    password_char=(random.choices(string.ascii_letters,k=letter)+random.choices(string.digits,k=num) +random.choices(string.punctuation,k=sympol))
    random.shuffle(password_char)
    pas="".join(password_char)
    print("generated password " ,pas)