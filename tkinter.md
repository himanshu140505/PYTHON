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



#options include -> text, font, background, foreground, etc
