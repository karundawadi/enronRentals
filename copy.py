import tkinter as tk
import mysql.connector

window = tk.Tk()  # Window is the main tkinter
window.title("Enrol Rental System")

def get_data():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="Print Data")
    con = mysql.connector.connect(host="localhost", user="root", password="Birgha@1", database="Part_ten")
    c = con.cursor()

    if len(cust_id.get()) == 0 and len(cust_name.get()) == 0:
        c.execute('SELECT * FROM vRentalInfo ORDER BY vRentalInfo.BalanceDue')
        answer = c.fetchall()
        data = ''
        for a in answer:
            data += "\n" + str(a[0]) + "\t" + str(a[1]) + "\t" + str(a[2]) + "\t" + str(a[3]) + "\t" + str(a[4]) + \
                    "\t" + str(a[5]) + "\t" + str(a[6]) + "\t" + str(a[7]) + "\t" + str(a[8]) + "\t" \
                    + str(a[9]) + "\t" + str(a[10]) + "\t" + ('$' + str("%.2f" % a[11])) + "\n"

        # prints query output
        result = tk.Label(newwin, text=data)
        result.grid(row=0, column=0, columnspan=2)

        # destroy tbe current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=1, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get())!= 0 and len(cust_name.get()) == 0:
        c.execute("SELECT DISTINCT CusomterID ,CustomerName,CONCAT('$',CAST(BalanceDue AS DECIMAL(10,2))) FROM "
                  "vRentalInfo WHERE CusomterID ='" + (cust_id.get()) + "';")
        answer = c.fetchall()
        data = ''
        for a in answer:
            data += "\n" + str(a[0]) + "\t" + str(a[1]) + "\t" + str(a[2]) + "\n"

        # if the input is invalid
        if len(data) == 0:
            message = "Invalid input. Please try again "

            # print the query answer
            result = tk.Label(newwin, text=message)
            result.grid(row=0, column=0, columnspan=2)

        # if the input is valid
        else:
            result = tk.Label(newwin, text=data)
            result.grid(row=0, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=1, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get()) == 0 and len(cust_name.get()) != 0:
        c.execute( "SELECT DISTINCT CusomterID, CustomerName, CONCAT('$', CAST(BalanceDue AS DECIMAL(10,2))) FROM "
                   "vRentalInfo WHERE CustomerName LIKE '" + ('%'+cust_name.get()+'%') + "';")

        answer = c.fetchall()
        print(answer)
        data = ''
        for a in answer:
            data += "\n" + str(a[0]) + "\t" + str(a[1]) + "\t" + str(a[2]) + "\n"

        if len(data) == 0:
            message = "Invalid input. Please try again "

            # print the query answer
            result = tk.Label(newwin, text=message)
            result.grid(row=0, column=0, columnspan=2)

        # if the input is valid
        else:
            result = tk.Label(newwin, text=data)
            result.grid(row=0, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=1, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get()) != 0 and len(cust_name.get()) != 0:
        c.execute("SELECT DISTINCT CusomterID, CustomerName, CONCAT('$', CAST(BalanceDue AS DECIMAL(10,2))) FROM "
                  "vRentalInfo WHERE CustomerName LIKE '" +('%'+ cust_name.get()+'%') + "'AND CusomterID ='" +
                  (cust_id.get()) + "';")
        answer = c.fetchall()
        print(answer)
        data = ''
        for a in answer:
            data += "\n" + str(a[0]) + "\t" + str(a[1]) + "\t" + str(a[2]) + "\n"

        # if the input is invalid
        if len(data)==0:
            message = "Invalid input. Please try again "

            # print the query answer
            result = tk.Label(newwin, text=message)
            result.grid(row=0, column=0, columnspan=2)

        # if the input is valid
        else:
            result = tk.Label(newwin, text=data)
            result.grid(row=0, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=1, columnspan=2)

        con.commit()
        con.close()

        # clear the input boxes NOT WORKING
        # cust_id.delete(1.0, END)
        # cust_name.delete(1.0, END)

    # display.pack()


def openDisplayWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="Enter values below")

    global cust_id
    global cust_name

    cust_id = tk.Entry(newwin, width=30)
    cust_id.grid(row=0, column=1)

    cust_name = tk.Entry(newwin, width=30)
    cust_name.grid(row=1, column=1)

    cust_id_label = tk.Label(newwin, text="CustID")
    cust_id_label.grid(row=0, column=0)

    cust_name_label = tk.Label(newwin, text="Name")
    cust_name_label.grid(row=1, column=0)

    submit_button = tk.Button(newwin, text="Submit", command=get_data)
    submit_button.grid(row=3, column=1, columnspan=1)

    cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
    cancel_button.grid(row=4, column=1, columnspan=1)

def openAddWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
    display.pack()


def openPerformWindow():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="A new window !")
    display.pack()


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