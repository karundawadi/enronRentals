import tkinter as tk
import mysql.connector 
import tkinter.messagebox as MessageBox
from datetime import date

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
                password="Qwerty12345!" # A fake password :|>
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
                        password="Qwerty12345!" # A fake password :|>
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
        def end_return_a_car_view:
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
    
    rent_a_car_button = tk.Button(newwin,
    text="Rent a car",
    width=20,
    command= rentACar
    )
    
    return_a_car_button = tk.Button(newwin,
    text="Return a car",
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
