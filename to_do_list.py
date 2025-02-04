'''This is a function made by 
                            PyWebCurcit
                                        A intermediate level to-do-list with Python'''

#imported os and time modules for clearing the screen (clearscreen) and sleep functions respectively 

from systemcommands import *
import time

# The todolist() contains various functions like :
# 1.todoicon 2.invalidfunc 3.exit 4.clearscreen 
# 5.space(for space generation in the concat input of the new tasks) 
# 6.display and the main func which contains the match case for the todolist 

def todolist():

    def todoicon():
        print("================================================")
        print("||                 TO DO LIST                 ||")
        print("================================================")


    def invalidfunc():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("          Invalid Choice. TRY AGAIN!!!          ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")


    def exit():
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("             Exiting the program...             ")
        print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

    
    def space(b):
        return((20-len(b))*" ")
    

    def display(a):
        print("================================================")
        print("S_NO.          TASK                   STATUS    ")
        print("------------------------------------------------")
        if a:
            for item in a:
                print(item)
        else:
            print("No tasks to show")
        print("================================================")


    c=1
    tasks = []
    while(c!=0):
        clearscreen()
        todoicon()
        print("||     OPTIONS :                              ||")
        print("||              1. Enter Task(s)              ||")
        print("||              2. Show Task(s)               ||")
        print("||              3. Mark Task(s) as done       ||")
        print("||      PRESS       0       TO       EXIT     ||")
        print("================================================")
        c = int(input("Enter your choice based on the above options : "))
        
        clearscreen()
    
        match(c):
            case 0:
                exit()
                time.sleep(10)
                clearscreen()


            case 1:
                n = int(input("Enter the number of tasks you wish to enter : "))
                for i in range(len(tasks), len(tasks) + n):
                    task = input("Enter the task : ")
                    tasks.append(f"{i + 1}.          {task}{space(task)}     Not Done")
                clearscreen()
            

            case 2:
                display(tasks)
                print("WAIT...")
                time.sleep(10)
                clearscreen()


            case 3:
                display(tasks)
                td = input("Enter the task you wish to mark as done: ")
                for i in range(len(tasks)):
                    ts = tasks[i].split(".")[0]
                    if ts == td:
                        tasks[i] = tasks[i].replace("Not Done","    Done")
                print("================================================")
                display(tasks)


            case _:
                invalidfunc()

    
todolist()