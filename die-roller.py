import cv2
import random
from systemcommands import *
from tkinter_app import insert_text, main as tkinter_main

def nggicon(text_widget):
    insert_text(text_widget, "================================================")
    insert_text(text_widget, "||                 DIE ROLLER                 ||")
    owner_text = owner_txt()
    insert_text(text_widget, owner_text)
    insert_text(text_widget, "================================================")

def getval(text_widget):
    die_roll_no = int(input("Enter the number of times you want the die(s) to roll: "))
    insert_text(text_widget, f"Number of rolls: {die_roll_no}")
    return die_roll_no

def die_roller(text_widget):
    nggicon(text_widget)
    die_roll_no = getval(text_widget)

    while die_roll_no != 0:    
        c = 1
        
        die_random_list = []
        for i in range(die_roll_no):
            die_random_list.append(random.randint(1, 6))
            
        for i in die_random_list:
            img = cv2.imread(f'DIE-IMAGES/die-{i}.png')
            if img is not None:
                cv2.imshow(f"DIE ROLL {c}", img)
                c += 1
            else:
                insert_text(text_widget, f"Error: Could not load image DIE-IMAGES/die-{i}.png")

        cv2.waitKey(0)
        cv2.destroyAllWindows()

        nggicon(text_widget)
        die_roll_no = getval(text_widget)

    clearscreen()
    exitfn()

if __name__ == "__main__":
    root, text_widget = tkinter_main('Die Roller App')
    die_roller(text_widget)
    root.mainloop()
