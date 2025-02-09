from systemcommands import *

def temp_conv_logo():
    print("================================================")
    print("||            TEMPERATURE CONVERTOR           ||")
    owner()
    print("================================================")

def choices():
    print("================================================")
    print("|| Enter your choice:                         ||")
    print("||    1. Celcius to Farhenheit                ||")
    print("||    2. Celcius to Kelvin                    ||")
    print("||    3. Farhenheit to Celcius                ||")
    print("||    4. Farhenheit to Kelvin                 ||")
    print("||    5. Kelvin to Celcius                    ||")
    print("||    6. Kelvin to Farhenheit                 ||")
    print("================================================")

def temp_convertor():
    user_choice = 1

    while user_choice != 0:
        clearscreen()

        temp_conv_logo()
        choices()

        user_choice = int(input("Enter your choice : "))
        clearscreen()

        print("================================================")

        match (user_choice):
            case 0:
                clearscreen()
                break

            case 1:
                celcius = float(input("|| Enter the temperature in celcius : "))
                farhenheit = (celcius * 9/5) + 32
                print("================================================")
                print(f"||The temperature in farhenheit is : {farhenheit}  ")

            case 2:
                celcius = float(input("|| Enter the temperature in celcius : "))
                kelvin = celcius + 273.15
                print("================================================")
                print(f"|| The temperature in Kelvin is : {kelvin}    ")

            case 3:
                farhenheit = float(input("|| Enter the temperature in farhenheit : "))
                celcius = farhenheit - 32 * 5/9
                print("================================================")
                print(f"|| The temperature in Celcius is : {celcius}")

            case 4:
                farhenheit = float(input("|| Enter the temperature in farhenheit : "))
                kelvin = farhenheit - 32 * 5/9
                print("================================================")
                print(f"|| The temperature in Kelvin is : {kelvin}")

            case 5:
                kelvin = float(input("|| Enter the temperature in Kelvin : "))
                celcius = farhenheit - 32 * 5/9
                print("================================================")
                print(f"|| The temperature in Celcius is : {celcius}")

            case 6:
                kelvin = float(input("|| Enter the temperature in Kelvin : "))
                farhenheit = farhenheit - 32 * 5/9
                print("================================================")
                print(f"|| The temperature in Farhenheit is : {farhenheit}")

            case _:
                print("|| Invalid Choice !!!!!!!!")
            
        print("================================================")
        sleepfn()

temp_convertor()

