# Branch added 
import tkinter as tk
import mysql.connector 

window = tk.Tk() # Window is the main tkinter 
window.title("Enrol Rental System")
window.geometry("500x300") # Setting the size of the application window 

# connecting to db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Qwerty12345!" # A fake password :|>
)

def openAddWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
    display.pack()    

def openDisplayWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
    display.pack()  

def openPerformWindow():
    newwin = tk.Toplevel(window)
    newwin.geometry("500x300") # Sets the size of window to 500 by 300 
    
    # Opens rent a car window 
    def rentACar():
        rent_a_car_window = tk.Toplevel(window)
        display = tk.Label(rent_a_car_window, text="Rent a car")
        display.pack()    
    
    # Opens return a car window 
    def returnACar():
        return_a_car = tk.Toplevel(window)
        display = tk.Label(return_a_car, text="Return a car !")
        display.pack()  
    
    rent_a_car_button = tk.Button(newwin,
    text="Rent a car",
    width=20,
    command= rentACar
    )
    
    return_a_car_button = tk.Button(newwin,
    text="Rent a car",
    width=20,
    command= returnACar
    )
    rent_a_car_button.grid(row=0, column=0, columnspan =2, padx=180 , pady = 25)
    return_a_car_button.grid(row=1, column=0, columnspan =2, padx=180 , pady = 25)
    

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
    bg = 'blue',
    command=openPerformWindow
)

add.grid(row=0, column=0, columnspan =2, padx=180 , pady = 25)
display.grid(row=1, column=0,columnspan =2, padx=180, pady=25)
perform.grid(row=2, column=0, columnspan =2, padx=180, pady=25)

window.mainloop() # Listens for various changes 
