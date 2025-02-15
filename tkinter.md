Tkinter is a standard GUI library for Python which provides a fast adn easy way to create desktop applications.

root = tk.Tk(screenName = None, baseName = None, className = 'Tk', useTk=1)
mainloop()

import tkinter
m = tkinter.Tk()
'widgets are added here'
m.mainloop()

LABLES : w = Label(master, option = value)
-> the display box where we display text or image

BUTTON : w = Button(master, option = value)
->clickable button that can trigger an action

ENTRY : w = Entry(master, option = value)
-> to input the single line text entry from the user
-> for multiline text input Text widget is user

CHECKBUTTON : w = CheckButton(master, option = value)
-> can be toggled on and off 
-> can be lined to a variable to store its state

RADIOBUTTON : RadioButton(master, option = value)
-> allows the user to select one option from a set of choices 
-> They are grouped by sharing the same variable

LISTBOX : w = Listbox(master, option = value)
-> display a list of items from which a user can select one or more

SCROLLBAR : w = Scrollbar(master, option = value)
-> the side controller which can be used to impliment listed widgets

MENU : window.w = Menu(master, option = value)
-> to create all kinds of menus used by the application

COMBOBOX : 
-> created using ttk.Combobox
-> values are specified using the values parameter
-> default value is set using the set method 
-> an event handler function on_select is bound to the Combobox using the bind method which updates a lable with the selected item whenever an item is selected

        def select(event):
            selected_item = combo_box.get()
            label.config(text="Selected Item: " + selected_item)

        root = tk.Tk()
        root.title("Combobox Example")

        # Create a label
        label = tk.Label(root, text="Selected Item: ")
        label.pack(pady=10)

        # Create a Combobox widget
        combo_box = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
        combo_box.pack(pady=5)

        # Set default value
        combo_box.set("Option 1")

        # Bind event to selection
        combo_box.bind("<<ComboboxSelected>>", select)

        root.mainloop()

SCALE : w = Scale(master, option = value)
-> used to provide a graphical slider that allows to select any value from that scale

TOPLEVEL : w = TopLevel(master, option = value)
-> is directly controlled by the window manager
-> don't need any parent window to work on 

MESSAGE : w = Message(master, option = value)
-> to display text messages with wrapping

MENU BUTTON : w = MenuButton(master, option = value)
-> is a part of top-down menu which stays on the window all the time

PROGRESSBAR : 
-> indicates the process of a long time task
-> the progressbar fills up to 100% over a short period stimulating a task that takes time to complete

        def start_progress():
            progress.start()

            # Simulate a task that takes time to complete
            for i in range(101):
            # Simulate some work
                time.sleep(0.05)  
                progress['value'] = i
                # Update the GUI
                root.update_idletasks()  
            progress.stop()

        root = tk.Tk()
        root.title("Progressbar Example")

        # Create a progressbar widget
        progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        progress.pack(pady=20)

        # Button to start progress
        start_button = tk.Button(root, text="Start Progress", command=start_progress)
        start_button.pack(pady=10)

        root.mainloop()


SPINBOX : w = SpinBox(master, option = value)
-> is an entryof 'Entry' widget

TEXT : w = Text(master, option = value)
->to edit a multi line text and format the way it has to be displayed

CANVAS : w = Canvas(master, option = value)
-> used to draw pictures and other complex layout like graphics text and widgets

PANNEDWINDOW : w = PannedWindow(master, optio = value)
-> used to handle numer of panes arranged in it

COLOR OPTION ;
-> Code ::
            import tkinter as tk
            root = tk.Tk()
            root.title("Color Options in Tkinter")

            # Create a button with active background and foreground colors
            button = tk.Button(root, text="Click Me", activebackground="blue", activeforeground="white")
            button.pack()

            # Create a label with background and foreground colors
            label = tk.Label(root, text="Hello, Tkinter!", bg="lightgray", fg="black")
            label.pack()

            # Create an Entry widget with selection colors
            entry = tk.Entry(root, selectbackground="lightblue", selectforeground="black")
            entry.pack()

            root.mainloop()


TKINTER GEOMETRY MANAGERS : 
-> offers access to the geometric configuration of the widgets which can organise the widgets in the parent windows
-> Three geometry manager classes class :
    1. pack() method 
       -> organises the widgets in block s before placing in the parent widget
       -> can be packed from the top, bootom, left or right
       -> can widgets to fill the available space o place them in a fixed size
       -> Code ::
                import tkinter as tk

                root = tk.Tk()
                root.title("Pack Example")

                # Create three buttons
                button1 = tk.Button(root, text="Button 1")
                button2 = tk.Button(root, text="Button 2")
                button3 = tk.Button(root, text="Button 3")

                # Pack the buttons vertically
                button1.pack()
                button2.pack()
                button3.pack()

                root.mainloop()

    2. grid() method :
       -> organizes the widgets in grid (table-like structure) before placing in the parent widget
       -> each widget is assigned a row and column
       -> can span multiple rows or columns using rowspan and columnspan
       -> Code ::
                import tkinter as tk

                root = tk.Tk()
                root.title("Grid Example")

                # Create three labels
                label1 = tk.Label(root, text="Label 1")
                label2 = tk.Label(root, text="Label 2")
                label3 = tk.Label(root, text="Label 3")

                # Grid the labels in a 2x2 grid
                label1.grid(row=0, column=0)
                label2.grid(row=0, column=1)
                label3.grid(row=1, column=0, columnspan=2)

                root.mainloop()

    3. place() method :
        -> organises the widgets y placing them in specifi positions directly by the programmer
        -> widgets are placed at specific x and y coordinates
        ->




# options include -> text, font, background, foreground, etc
