import tkinter as tk
import tkinter.messagebox as MessageBox
from datetime import date
import mysql.connector
import re

window = tk.Tk() # Window is the main tkinter 
window.title("Enron Rental System")
window.geometry("500x300") # Setting the size of the application window 
password_database = "Qwerty12345!" #change this to database password 

# connecting to db
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="project2",
    password=password_database # A fake password :|>
)

def get_vehicle():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="Print Data")
    newwin.geometry("500x300")
    con = mysql.connector.connect(host="localhost", user="root", password=password_database, database="project2")
    c = con.cursor()

    if len(veh_id.get()) == 0 and len(vehicle_description.get()) == 0:
        c.execute('SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, RATE.Daily  from vRentalInfo, VEHICLE, RATE WHERE RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VechicleID = vRentalInfo.VIN ;')
        answer = c.fetchall()
        data = ''
        for a in answer:
            data += "\n" + " ".join(str(a[0]).split()) + "\t" + " ".join(str(a[1]).split()) + "\t" + " ".join(str(a[2]).split())  
        newwin.geometry("1000x1000")
        layout_t = "\n"+"VIN"+"\t"+"Vehicle"+"\t" +"Daily Rate"+"\n"
        
        # prints query output
        resultw = tk.Label(newwin, text=layout_t)
        resultw.grid(row=0, column=0, columnspan=2)
        
        result = tk.Label(newwin, text=data)
        result.grid(row=1, column=0, columnspan=2)

        # destroy tbe current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(veh_id.get())!= 0 and len(vehicle_description.get()) == 0:
        c.execute("SELECT DISTINCT vRentalInfo.VIN, vRentalInfo.Vehicle, RATE.Daily  from vRentalInfo, VEHICLE, RATE WHERE RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VechicleID = vRentalInfo.VIN AND vRentalInfo.VIN = '"+veh_id.get()+"';")
        answer = c.fetchall()
        data = ''
        for a in answer:
            data += "\n" + " ".join(str(a[0]).split()) + "\t" + " ".join(str(a[1]).split()) + "\t" + " ".join(str(a[2]).split())  
        
        # if the input is invalid
        if len(data) == 0:
            message = "Invalid input. Please try again "

            # print the query answer
            result = tk.Label(newwin, text=message)
            result.grid(row=0, column=0, columnspan=2)

        # if the input is valid
        else:
            layout_t = "\n"+"VIN"+"\t"+"Vehicle"+"\t" +"Daily Rate"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(veh_id.get()) == 0 and len(vehicle_description.get()) != 0:
        c.execute("SELECT DISTINCT vRentalInfo.VIN, vRentalInfo.Vehicle, RATE.Daily  from vRentalInfo, VEHICLE, RATE WHERE RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VechicleID = vRentalInfo.VIN AND vRentalInfo.Vehicle LIKE '"+('%' + vehicle_description.get() + '%') + "';")
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
            layout_t = "\n"+"VIN"+"\t"+"Vehicle"+"\t" +"Daily Rate"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(veh_id.get()) != 0 and len(vehicle_description.get()) != 0:
        c.execute("SELECT vRentalInfo.VIN, vRentalInfo.Vehicle, RATE.Daily  from vRentalInfo, VEHICLE, RATE WHERE RATE.Type = VEHICLE.Type AND RATE.Category = VEHICLE.Category AND VEHICLE.VechicleID = vRentalInfo.VIN AND vRentalInfo.Vehicle='"+vehicle_description.get()+"' AND vRentalInfo.VIN = '"+veh_id.get()+"';")
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
            layout_t = "\n"+"VIN"+"\t"+"Vehicle"+"\t" +"Daily Rate"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()

        # clear the input boxes NOT WORKING
        # cust_id.delete(1.0, END)
        # cust_name.delete(1.0, END)

    # display.pack()

def get_data():
    newwin = tk.Toplevel(window)
    display = tk.Label(newwin, text="Print Data")
    newwin.geometry("500x300")
    con = mysql.connector.connect(host="localhost", user="root", password=password_database, database="project2")
    c = con.cursor()

    if len(cust_id.get()) == 0 and len(cust_name.get()) == 0:
        c.execute('SELECT * FROM vRentalInfo ORDER BY vRentalInfo.RentalBalance')
        answer = c.fetchall()
        data = ''
        for a in answer:
            data += "\n" + " ".join(str(a[0]).split()) + "\t" + " ".join(str(a[1]).split()) + "\t" + " ".join(str(a[2]).split()) + "\t" + " ".join(str(a[3]).split()) + "\t" + " ".join(str(a[4]).split()) + "\t" + " ".join(str(a[5]).split()) + "\t" + " ".join(str(a[6]).split()) + "\t" + " ".join(str(a[7]).split()) + "\t" + " ".join(str(a[8]).split()) + "\t" + " ".join(str(a[9]).split()) + "\t" + " ".join(str(a[10]).split()) + "\t" + ('$' + str("%.2f" % a[11])) 
        newwin.geometry("1000x1000")
        layout_t = "\n"+"OrderDate"+"\t"+"StartDate"+"\t" +"Return Date"+"\t"+"TotalDays"+"\t"+"VIN"+"\t"+"Vehicle"+"\t"+"Type"+"\t"+"Category"+"\t"+"CustomerID"+"\t"+"CustomerName"+"\t"+"OrderAmount"+"\t"+"RentalBalance"+"\n"
        # prints query output
        resultw = tk.Label(newwin, text=layout_t)
        resultw.grid(row=0, column=0, columnspan=2)
        
        result = tk.Label(newwin, text=data)
        result.grid(row=1, column=0, columnspan=2)

        # destroy tbe current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get())!= 0 and len(cust_name.get()) == 0:
        c.execute("SELECT CusomterID ,CustomerName,CONCAT('$',CAST(RentalBalance AS DECIMAL(10,2))) FROM "
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
            layout_t = "\n"+"CustID"+"\t"+"Name"+"\t" +"Balance Due"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get()) == 0 and len(cust_name.get()) != 0:
        c.execute( "SELECT CusomterID, CustomerName, CONCAT('$', CAST(RentalBalance AS DECIMAL(10,2))) FROM "
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
            layout_t = "\n"+"CustID"+"\t"+"Name"+"\t" +"Balance Due"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()


    elif len(cust_id.get()) != 0 and len(cust_name.get()) != 0:
        c.execute("SELECT CusomterID, CustomerName, CONCAT('$', CAST(RentalBalance AS DECIMAL(10,2))) FROM "
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
            layout_t = "\n"+"CustID"+"\t"+"Name"+"\t" +"Balance Due"+"\n"
            # prints query output
            resultw = tk.Label(newwin, text=layout_t)
            resultw.grid(row=0, column=0, columnspan=2)
            result = tk.Label(newwin, text=data)
            result.grid(row=1, column=0, columnspan=1)

        # destroy the current window
        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=3, column=0, columnspan=2)

        con.commit()
        con.close()

        # clear the input boxes NOT WORKING
        # cust_id.delete(1.0, END)
        # cust_name.delete(1.0, END)

    # display.pack()

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

        con = mysql.connector.connect(host="localhost", user="root", password=password_database, database="project2")
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
        con = mysql.connector.connect(host="localhost", user="root", password=password_database, database="project2")
        cursor = con.cursor()
        try:
            cursor.execute("INSERT INTO Vehicle VALUES('" + v_id + "','" + v_desc + "','" + v_year + "','" + v_type + "','" + v_cat +"')")
            cursor.execute("commit")
        except:
            pass

        con.close()

def openCustomer():
    newwin = tk.Toplevel(window)
    newwin.geometry("500x300")
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
    insert.place(x=20, y=100)

def openVehicle():
    newwin = tk.Toplevel(window)
    newwin.geometry("500x300")
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
    vehicle_id.place(x=180, y=30)
    vehicle_desc = tk.Entry(newwin)
    vehicle_desc.place(x=180, y=60)
    vehicle_year = tk.Entry(newwin)
    vehicle_year.place(x=180, y=90)
    vehicle_type = tk.Entry(newwin)
    vehicle_type.place(x=180, y=120)
    vehicle_cat = tk.Entry(newwin)
    vehicle_cat.place(x=180, y=150)

    insert = tk.Button(newwin, text="Insert", command=insertVehicle)
    insert.place(x=20, y=180)

def openAddWindow():
    newwin = tk.Toplevel(window)
    customer = tk.Button(
        newwin,
        text="Add Customer",
        width=20,
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
    newwin.geometry("500x300") # Sets the size of window to 500 by 300 
    
    def open_customer():
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
    
    def open_vehicle():
        newwin = tk.Toplevel(window)
        display = tk.Label(newwin, text="Enter values below")

        global veh_id
        global vehicle_description

        veh_id = tk.Entry(newwin, width=30)
        veh_id.grid(row=0, column=1)

        vehicle_description = tk.Entry(newwin, width=30)
        vehicle_description.grid(row=1, column=1)

        cust_id_label = tk.Label(newwin, text="VIN")
        cust_id_label.grid(row=0, column=0)

        cust_name_label = tk.Label(newwin, text="Vehicle Description")
        cust_name_label.grid(row=1, column=0)

        submit_button = tk.Button(newwin, text="Submit", command=get_vehicle)
        submit_button.grid(row=3, column=1, columnspan=1)

        cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
        cancel_button.grid(row=4, column=1, columnspan=1)
    
    customer_button = tk.Button(newwin, text="Customer", command=open_customer)
    customer_button.grid(row=1, column=1, columnspan=1,padx=180 , pady = 25)
    
    vehicle_button = tk.Button(newwin, text="Vehicle", command=open_vehicle)
    vehicle_button.grid(row=2, column=1, columnspan=1,padx=180 , pady = 25)

    cancel_button = tk.Button(newwin, text="Cancel", command=newwin.destroy)
    cancel_button.grid(row=3, column=1, columnspan=1,padx=180 , pady = 25)
    
def openPerformWindow():
    newwin = tk.Toplevel(window)
    newwin.geometry("500x300") # Sets the size of window to 500 by 300 
    
    # Opens rent a car window 
    def retriveARental():
        customername = tk.StringVar() # Basically Null value
        vehicle_number = tk.StringVar()
        return_date_rental = tk.StringVar()
        # View elements 
        retrive_a_car_window = tk.Toplevel(window)
        retrive_a_car_window.geometry("500x300")
        name_customer = tk.Label(retrive_a_car_window, text="Name :")
        vehicle_id = tk.Label(retrive_a_car_window, text="Vehicle Id:")
        return_date_field = tk.Label(retrive_a_car_window,text="Enter Return Date:")
        
        name_of_customer = tk.Entry(retrive_a_car_window,textvariable = customername)
        vehicle_id_customer = tk.Entry(retrive_a_car_window,textvariable = vehicle_number)
        return_date_field_second = tk.Entry(retrive_a_car_window, textvariable = return_date_rental)
        
        def findRental():
            retrive_a_car_window_find_rental = tk.Toplevel(window)
            retrive_a_car_window_find_rental.geometry("500x500")
            # connecting to db
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="project2",
                password=password_database # A fake password :|>
            )
            custname = customername.get().strip()
            vehicleno = vehicle_number.get()
            returndate = return_date_rental.get()
            cursor = mydb.cursor()
            sql = "SELECT RENTAL.CustID, RENTAL.StartDate, RENTAL.RentalType, RENTAL.Qty, RENTAL.TotalAmount, RENTAL.PaymentDate FROM RENTAL,CUSTOMER WHERE CUSTOMER.CustID = RENTAL.CustID AND CUSTOMER.Name ='"+custname+"'AND RENTAL.VechicleID ='"+vehicleno+"'AND RENTAL.ReturnDate='"+returndate+"';"
            print(sql)
            cursor.execute(sql) 
            results = cursor.fetchall()
            print(results)
            data = ''
            for a in results:
                data += "\n"+str(a[0])+"\t"+str(a[1])+"\t" +str(a[2])+"\t"+str(a[3])+"\t"+str(a[4])+"\t"+str(a[5])
            layout_t = "\n"+"CustID"+"\t"+"StartDate"+"\t" +"Rental Type"+"\t"+"Qty"+"\t"+"Total Amount"+"\t"+"Payment Date"
            result_obtained_findrental = tk.Label(retrive_a_car_window_find_rental,text=data)
            layout_text =  tk.Label(retrive_a_car_window_find_rental,text=layout_t)
            def destroyRetrive():
                retrive_a_car_window_find_rental.destroy() # Destroys the view 
            cancel_button_retrieve = tk.Button(retrive_a_car_window_find_rental,
                text="Return",
                width=20,
                command = destroyRetrive
            )
            layout_text.grid(row=0,column=0)
            result_obtained_findrental.grid(row=1,column=0)
            cancel_button_retrieve.grid(row=2,column=0)
            cursor.close()
        
        sumbit_info_button = tk.Button(retrive_a_car_window,
            text="Sumbit",
            width=20,
            command = findRental
        )
        
        def destroyRetrive():
            retrive_a_car_window.destroy() # Destroys the view 
        cancel_button_retrieve = tk.Button(retrive_a_car_window,
            text="Cancel",
            width=20,
            command = destroyRetrive
        )
        
        name_customer.grid(row=0,column=0)
        name_of_customer.grid(row=0,column=1)
        vehicle_id.grid(row=1,column=0)
        vehicle_id_customer.grid(row=1,column=1)
        return_date_field.grid(row=2,column=0)
        return_date_field_second.grid(row=2,column=1)
        sumbit_info_button.grid(row=3,column=0)
        cancel_button_retrieve.grid(row=4,column=0)
        
    # Opens return a car window 
    def returnACar():
        customername = tk.StringVar() # Basically Null value
        vehicle_number = tk.StringVar()
        return_a_car = tk.Toplevel(window)
        return_a_car.geometry("500x300")
        
        def processReturnACar():
            show_pay_button = True
            name_provided = customername.get()
            id_provided = vehicle_number.get()
            # Connecting database again here 
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                database="project2",
                password=password_database # A fake password :|>
            )
            cursor = mydb.cursor()
            sql = "SELECT CUSTOMER.Name, SUM(RENTAL.TotalAmount) as CurrentBalance FROM CUSTOMER, RENTAL WHERE CUSTOMER.CustID = RENTAL.CustID AND CUSTOMER.Name ='"+ name_provided+"'AND RENTAL.VechicleID ='"+id_provided+"'AND RENTAL.PaymentDate is NULL;"
            cursor.execute(sql) 
            results = cursor.fetchall()
            if len(results) == 0: # To check if the results are returned or not 
                MessageBox.showerror(title="No records found",message="Try again")
            else:
                cursor.close() # Closes the connection 
                print(name_provided)
                print(id_provided)
                print(results)
                user_name_obtained = results[0][0] 
                amount_due = results[0][1]
                payment_window = tk.Toplevel(window)
                payment_window.geometry("500x300")
                amount_due_text_shown = tk.Label(payment_window, text="No payment due")
                if amount_due is None:
                    amount_due_text_shown = tk.Label(payment_window, text="No payments due !")
                    show_pay_button = False
                else:
                    amount_due_text_shown = tk.Label(payment_window, text="$ "+str(amount_due)+" Due")
                
                def destroy_all_views():
                    payment_window.destroy()
                
                def complete_payment_for_user():
                    mydb = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        database="project2",
                        password=password_database # A fake password :|>
                    )
                    cursor = mydb.cursor()
                    # To get customer id 
                    sql_cust_id = "SELECT CUSTOMER.CustID FROM CUSTOMER WHERE CUSTOMER.Name ='"+ name_provided+"';"
                    cursor.execute(sql_cust_id) 
                    sql_cust_id_results = cursor.fetchall()
                    cust_id_found = sql_cust_id_results[0][0]
                    print("The customer ID found is "+str(cust_id_found))
                    today = date.today()
                    d4 = today.strftime("%Y-%m-%d") # Converting to format required 
                    print("d4 =", d4)
                    sql = "UPDATE RENTAL SET RENTAL.PaymentDate ='"+d4+"' WHERE RENTAL.VechicleID ='"+id_provided+"' AND RENTAl.CustID ='"+str(cust_id_found)+"';"
                    print(sql) # To verify is complete or not 
                    cursor.execute(sql) 
                    cursor.close()
                    payment_window.destroy()
                pay_amount_button = tk.Button(payment_window, 
                                            text="Pay due amount",
                                            width=20,
                                            command = complete_payment_for_user)
                cancel_button = tk.Button(payment_window, 
                                            text="Cancel Button",
                                            width=20,
                                            command = destroy_all_views)
                amount_due_text_shown.grid(row=0,column=1)
                if(show_pay_button):
                    pay_amount_button.grid(row=1,column=0)
                cancel_button.grid(row=2,column=0)
        
        # UI elements
        generic_ui_1 = tk.Label(return_a_car, text="Enter your name and VIN of the car")
        name_customer = tk.Label(return_a_car, text="Name :")
        vehicle_id = tk.Label(return_a_car, text="Vehicle Id:")
        name_of_customer = tk.Entry(return_a_car,textvariable = customername)
        vehicle_id_customer = tk.Entry(return_a_car,textvariable = vehicle_number)
        sumbit_info_button = tk.Button(return_a_car,
            text="Sumbit",
            width=20,
            command = processReturnACar
        )
        def end_return_a_car_view():
            return_a_car.destroy() # Destroys the view 
            
        cancel_info_button = tk.Button(return_a_car,
            text="Cancel",
            width=20,
            command = end_return_a_car_view
        )
        
        # Grid options
        generic_ui_1.grid(row=0, column=0)
        name_customer.grid(row=1, column=0)
        vehicle_id.grid(row=2, column=0)
        name_of_customer.grid(row=1, column=1)
        vehicle_id_customer.grid(row=2, column=1)
        sumbit_info_button.grid(row=4, column=0)
        cancel_info_button.grid(row=5,column=0)
    
    def destroy_perform_window():
        newwin.destroy()
    
    cancel_button = tk.Button(newwin,
    text="Cancel",
    width=20,
    command= destroy_perform_window
    )
    
    retrive_a_rental_button = tk.Button(newwin,
    text="Retrieve a rental",
    width=20,
    command= retriveARental
    )
    
    return_a_car_button = tk.Button(newwin,
    text="Return a car",
    width=20,
    command= returnACar
    )
    
    retrive_a_rental_button.grid(row=0, column=0, columnspan =2, padx=180 , pady = 25)
    return_a_car_button.grid(row=1, column=0, columnspan =2, padx=180 , pady = 25)
    cancel_button.grid(row=2, column=0, columnspan =2, padx=180 , pady = 25)

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

add.grid(row=0, column=0, columnspan =2, padx=180 , pady = 25)
display.grid(row=1, column=0,columnspan =2, padx=180, pady=25)
perform.grid(row=2, column=0, columnspan =2, padx=180, pady=25)

window.mainloop() # Listens for various changes 
