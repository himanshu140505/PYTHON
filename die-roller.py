import cv2
import random
from systemcommands import *

def nggicon():
    print("================================================")
    print("||                 DIE ROLLER                 ||")
    owner()
    print("================================================")

    
def getval():
    die_roll_no = int(input("Enter the nmber of times you want the die(s) to roll : "))
    return(die_roll_no)



def die_roller():
    nggicon()
    die_roll_no = getval()

    while (die_roll_no != 0):    
        c = 1
        
        die_random_list = []
        for i in range(0,die_roll_no):
            die_random_list.append(random.randint(1,6))
            
        for i in die_random_list:
            cv2.imshow(f"DIE ROLL {c}", cv2.imread(f'DIE-IMAGES/die-{i}.png'))
            c=c+1

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        clearscreen()
        nggicon()
        die_roll_no = getval()

    clearscreen()
    exitfn()

die_roller()
