import tkinter as tk

window = tk.Tk() # Window is the main tkinter 
window.title("Enrol Rental System")

def openAddWindow():
    newwin = Toplevel(window)
    display = Label(newwin, text="A new window !")
    display.pack()    

def openDisplayWindow():
    newwin = Toplevel(window)
    display = Label(newwin, text="A new window !")
    display.pack()  

def openPerformWindow():
    newwin = Toplevel(window)
    display = Label(newwin, text="A new window !")
    display.pack()  

# Buttons
add = tk.Button(
    text="Add",
    width=20,
    command=openAddWindow
)
display = tk.Button(
    text="Display",
    width=20,
    command=openDisplayWindow
)
perform = tk.Button(
    text="Perform",
    width=20,
    command=openPerformWindow
)

add.grid(row = 0, column = 0, pady = 2)
display.grid(row = 1, column = 0, pady = 2)
perform.grid(row = 2, column=0, pady = 2 )
window.mainloop()
