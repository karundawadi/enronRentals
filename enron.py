import tkinter as tk
import tkinter.messagebox as MessageBox
import mysql.connector
import re

window = tk.Tk() # Window is the main tkinter 
window.title("Enrol Rental System")

def insertCustomer():
    name = e_name.get()
    phone = e_phone.get()

    if len(phone) != 10 or not phone.isdigit():
        MessageBox.showinfo("Number", "Number needs to be valid.")
    elif (name == "" or phone == ""):
        MessageBox.showinfo("Insert", "Needs all fields.")
    else:
        tempPhone = "("
        x = 0
        for token in phone:
            if x == 3:
                tempPhone += ") "
            if x == 6:
                tempPhone += "-"
            tempPhone += token
            x += 1

        phone = tempPhone

        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="project2")
        cursor = con.cursor()
        cursor.execute("SELECT MAX(custID) FROM Customer")
        num = cursor.fetchall()
        num = [i[0] for i in num]
        num = str(int(num[0]) + 1)
        try:
            cursor.execute("INSERT INTO Customer VALUES('" + num + "','" + name + "','" + phone +"')")
            cursor.execute("commit")
        except:
            pass

        con.close()

def insertVehicle():
    v_id = vehicle_id.get()
    v_desc = vehicle_desc.get()
    v_year = vehicle_year.get()
    v_type = vehicle_type.get()
    v_cat = vehicle_cat.get()

    if not v_year.isdigit() or not v_type.isdigit() or not v_type.isdigit():
        MessageBox.showinfo("Value Type", "Please make sure year, type, and category are numbers.")
    elif len(v_id) != 17:
        MessageBox.showinfo("Vehicle Id", "Vehicle ID is invalid.")
    elif int(v_type) < 1 or int(v_type) > 6:
        MessageBox.showinfo("Type", "Type needs to be 1 to 6.")
    elif int(v_cat) != 0 and int(v_cat) != 1:
        MessageBox.showinfo("Category Value", "Category must be 0 or 1.")
    elif v_id == "" or v_desc == "" or v_year == "" or v_type == "" or v_cat == "":
        MessageBox.showinfo("Insert", "Needs all fields.")
    else:
        con = mysql.connector.connect(host="localhost", user="root", password="1234", database="project2")
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO Vehicle VALUES('" + v_id + "','" + v_desc + "','" + v_year + "','" + v_type + "','" + v_cat +"')")
            cursor.execute("commit")
        except:
            pass

        con.close()


def openCustomer():
    newwin = tk.Toplevel(window)
    name = tk.Label(newwin, text='Enter Name:')
    name.place(x=20, y=30)
    phone = tk.Label(newwin, text='Enter Phone Number:')
    phone.place(x=20, y=60)

    global e_name
    e_name = tk.Entry(newwin)
    e_name.place(x=150, y=30)
    global e_phone
    e_phone = tk.Entry(newwin)
    e_phone.place(x=150, y=60)

    insert = tk.Button(newwin, text="Insert", command=insertCustomer)
    insert.place(x=20, y=140)


def openVehicle():
    newwin = tk.Toplevel(window)
    v_id = tk.Label(newwin, text='Enter Vehicle ID:')
    v_id.place(x=20, y=30)
    v_desc = tk.Label(newwin, text='Enter Vehicle Description:')
    v_desc.place(x=20, y=60)
    v_year = tk.Label(newwin, text='Enter Vehicle Year:')
    v_year.place(x=20, y=90)
    v_type = tk.Label(newwin, text='Enter Vehicle Type:')
    v_type.place(x=20, y=120)
    v_cat = tk.Label(newwin, text='Enter Vehicle Category:')
    v_cat.place(x=20, y=150)

    global vehicle_id
    global vehicle_desc
    global vehicle_year
    global vehicle_type
    global vehicle_cat

    vehicle_id = tk.Entry(newwin)
    vehicle_id.place(x=150, y=30)
    vehicle_desc = tk.Entry(newwin)
    vehicle_desc.place(x=150, y=60)
    vehicle_year = tk.Entry(newwin)
    vehicle_year.place(x=150, y=90)
    vehicle_type = tk.Entry(newwin)
    vehicle_type.place(x=150, y=120)
    vehicle_cat = tk.Entry(newwin)
    vehicle_cat.place(x=150, y=150)

    insert = tk.Button(newwin, text="Insert", command=insertVehicle)
    insert.place(x=20, y=180)


def openAddWindow():
    newwin = tk.Toplevel(window)
    customer = tk.Button(
        newwin,
        text="Add Customer",
        width = 20,
        command=openCustomer
    )
    vehicle = tk.Button(
        newwin,
        text="Add Vehicle",
        width=20,
        command=openVehicle
    )
    customer.pack()
    vehicle.pack()

def openDisplayWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
    display.pack()  

def openPerformWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
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

add.grid(row=0, column=0, pady=2)
display.grid(row=1, column=0, pady=2)
perform.grid(row=2, column=0, pady=2)
window.mainloop()
