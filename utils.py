import random
import string

def check_password(p):
    l = any(i.islower() for i in p)
    u = any(i.isupper() for i in p)
    d = any(i.isdigit() for i in p)
    s = any(not i.isalnum() for i in p)

    if len(p) < 6 or p.isalpha() or p.isdigit():
        return "Weak Password"
    elif len(p) >= 8 and l and u and d and s:
        return "Strong Password"
    else:
        return "Medium Password"


def generate_password(n):
    chars = string.ascii_letters + string.digits + string.punctuation
    pwd = ""
    for _ in range(n):
        pwd += random.choice(chars)
    return pwd
