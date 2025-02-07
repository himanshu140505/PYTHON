from systemcommands import *
def calicon():
    print("================================================")
    print("||                 CALCULATOR                 ||")
    owner()
    print("================================================")

def calculator():
    while True:
        expression = input("Enter an expression: ")
        try:
            print("----------------------------------------")
            print("             Result = ", eval(expression))
            print("----------------------------------------")
        except:
            print("XXXXXX Invalid expression XXXXXX")
        print()
        choice = input("Do you want to continue? (Y/N)")
        if choice == 'N' or choice == 'n':
            print("EXITING.........")
            break



calculator()