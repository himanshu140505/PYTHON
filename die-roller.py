import cv2
import random
from systemcommands import *
from tkinter_app import TkinterApp

owner_text = owner_txt()

def nggicon(app):
    app.insert_text("================================================")
    app.insert_text("||                 DIE ROLLER                 ||")
    app.insert_text(f"{owner_text}")
    app.insert_text("================================================")

def getval(app):
    app.insert_text("||Enter the number of die you want to roll:   ||")
    app.insert_text("================================================")
    input_box = app.create_box(validate="key", validatecommand=(app.root.register(app.validate_input), '%P'),width=5, bd=10, relief="groove")
    input_box.bind('<Return>', lambda event: app.root.quit())
    app.root.mainloop()
    try:
        return int(input_box.get())
    except ValueError:
        app.insert_text("Invalid input. Please enter a valid number.")
        app.clear_text()
        nggicon(app)
        return getval(app)

def die_roller(app):
    nggicon(app)
    die_roll_no = getval(app)
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
                app.insert_text(f"Error: Could not load image DIE-IMAGES/die-{i}.png")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
        app.clear_text()
        nggicon(app)
        die_roll_no = getval(app)

    app.clear_text()
    exitfn()

if __name__ == "__main__":
    app = TkinterApp('DIE ROLLER')
    die_roller(app)
    app.run()
