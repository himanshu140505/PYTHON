import random 
from systemcommands import *

def pass_gen_icon():
    print("================================================")
    print("||             PASSWORD GENERATOR             ||")
    owner()
    print("================================================")

def password_gnerator():
    pass_gen_icon()

    print("|| USE ANY ONE OF THE FOLLOWING PASSWORDS:    ||")
    print("================================================")

    for i in range(1,6):
        password = ''
        for j in range(12):
            password += chr(random.randint(33, 126))
        print(f"||    {i}->  {password}                       ||")
    print("================================================")

password_gnerator()