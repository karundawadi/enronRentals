import tkinter as tk
window = tk.Tk() # Window is the main tkinter 
window.title("Enrol Rental System")

# Buttons
add = tk.Button(
    text="Add",
    width=20,
)
display = tk.Button(
    text="Display",
    width=20,
)
perform = tk.Button(
    text="Perform",
    width=20,
)

add.grid(row = 0, column = 0, pady = 2)
display.grid(row = 1, column = 0, pady = 2)
perform.grid(row = 2, column=0, pady = 2 )
window.mainloop()

# For new window 
def openNewWindow(nameOfWindow:String):
    newWindow = Toplevel(window)
    newWindow.title("New Window")
    newWindow.geometry("200x200")
    Label(newWindow, text ="This is a new window").pack()