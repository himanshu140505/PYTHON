import os
import sys
import time

def clearscreen():
    os.system('cls')

def exitfn():
    os._exit(0)

def sleepfn(n):
    time.sleep(n)


def typing(text):
    for character in text:
      sys.stdout.write(character)
      sys.stdout.flush()
      time.sleep(0.009)

def default():
    print("Under Development....")




















































def owner_txt():
    return("||                     ~ BY PyWebCircuit      ||")

def owner():
    print("||                     ~ BY PyWebCircuit      ||")
