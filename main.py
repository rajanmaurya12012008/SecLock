from utils import check_password, generate_password

print("Welcome to Password Checker & Generator")
print("S - Check Password")
print("G - Generate Password")

ch = input("Enter choice: ")

if ch == "S" or ch == "s":
    p = input("Enter password: ")
    print(check_password(p))

elif ch == "G" or ch == "g":
    n = int(input("Enter length: "))
    print("Password:", generate_password(n))

else:
    print("wrong choice")
