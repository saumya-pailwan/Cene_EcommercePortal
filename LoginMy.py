from tkinter import *
import tkinter.messagebox
import sqlite3
import Admin
import mini
import Addprodct
import functools
global A
global B
t = Tk()
t.geometry("900x450")
t.title("Account Login")


def register():
    connection = sqlite3.connect("projE_DB.db")
    cursor = connection.cursor()

    register_screen = Toplevel(t, bg="light grey")
    register_screen.title("Register")
    register_screen.geometry("900x650")

    username = StringVar()
    password = StringVar()
    mail = StringVar()
    contact = StringVar()
    address = StringVar()
    first = StringVar()
    last = StringVar()

    font0 = "Berlin Sans FB"
    # Set label for user's instruction
    Label(register_screen, text="Please enter your details", bg="#1A1A1D", fg="#66FCF1", relief=RIDGE, bd=5, padx=30,
          font=("calibri", 30)).pack(ipadx=500, ipady=10)

    fname = Label(register_screen, text="First Name * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    fname.pack(padx=20, pady=10)

    fname_entry = Entry(register_screen, textvariable=first, bd=3)
    fname_entry.pack(ipadx=4)

    lname = Label(register_screen, text="Last name * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    lname.pack(padx=20,pady=10)

    lname_entry = Entry(register_screen, textvariable=last, bd=3)
    lname_entry.pack(ipadx=4)

    mail_lable = Label(register_screen, text="Email-id * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    mail_lable.pack(padx=20,pady=10)

    mail_entry = Entry(register_screen, textvariable=mail, bd=3)
    mail_entry.pack(ipadx=4)

    username_lable = Label(register_screen, text="Username * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    username_lable.pack(padx=20,pady=10)

    username_entry = Entry(register_screen, textvariable=username, bd=3)
    username_entry.pack(ipadx=6)

    # Set password label
    password_lable = Label(register_screen, text="Password * ", fg="black", padx=20, font=("arial", 15), bg="light grey")
    password_lable.pack(padx=20,pady=10)

    # Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*', bd=3)
    password_entry.pack(ipadx=6)

    cont_lable = Label(register_screen, text="Contact No * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    cont_lable.pack(padx=20,pady=10)

    cont_entry = Entry(register_screen, textvariable=contact, bd=3)
    cont_entry.pack(ipadx=6)

    add_lable = Label(register_screen, text="Address * ", fg="black", padx=50, font=("arial", 15), bg="light grey")
    add_lable.pack(padx=20,pady=10)

    add_entry = Entry(register_screen, textvariable=address, bd=3)
    add_entry.pack(padx=5, ipadx=6, pady=5, ipady=10)

    def create_table():
        """cursor.execute("create table if not exists CUSTOMER(Username text,EmailId text,Password text,ContactNo "
                       "number, Address text)")"""
        cursor.execute('select count(customer_id)from CUSTOMER')
        A = cursor.fetchone()[0]
        B = A+1
        un = cursor.execute("select count(username) from CUSTOMER where username=(?)", (username_entry.get(),))
        va = un.fetchone()[0]
        if va == 1:
            tkinter.messagebox.showinfo("Login", "Username already exist!")
        elif (
                username_entry.get() or password_entry.get() or cont_entry.get() or add_entry.get() or mail_entry.get() or fname_entry.get() or lname_entry.get()) == "":
            tkinter.messagebox.showinfo("Login", "Enter all values pls!")
        elif len(cont_entry.get()) != 10:
            tkinter.messagebox.showinfo("Login", "Incorrect contact number!")
        else:
            cursor.execute("insert into CUSTOMER values(?,?,?,?,?,?,?,?)", (B, fname_entry.get(), lname_entry.get(), mail_entry.get(), password_entry.get(),add_entry.get(), cont_entry.get(), username_entry.get()))
            connection.commit()
            tkinter.messagebox.showinfo("Register", "Registration Successful! ")
            register_screen.destroy()

    Button(register_screen, text="Register", width=10, height=1, command=create_table, padx=20).pack()


def confirm():
    connection = sqlite3.connect("projE_DB.db")
    cursor = connection.cursor()
    un = cursor.execute("select count(username) from CUSTOMER where username=(?)", (e1.get(),))
    var = un.fetchone()[0]

    if var == 0:
        tkinter.messagebox.showinfo("Login", "Username doesn't exist!")

    pwd = cursor.execute("select password from CUSTOMER where username = (?)", (e1.get(),))
    pwd = cursor.fetchone()[0]
    if pwd == e2.get():
        tkinter.messagebox.showinfo("Login", "Login Successful")
        cursor.execute("select customer_id from customer where username=(?)", (e1.get(),))
        c_id = cursor.fetchone()[0]
        print(c_id)
        t.destroy()
        mini.create(c_id)
    else:
        tkinter.messagebox.showinfo("Login", "Login Failed..Incorrect username or password")


left = Frame(t, bd=5, relief=SUNKEN, width=300, height=450, bg="#1A1A1D").grid(row=0, column=0, columnspan=2, rowspan=7)
right = Frame(t, width=500, height=450).grid(row=0, column=2, columnspan=3, rowspan=7)

text = Label(left, text="LOGIN", bg="#1A1A1D", fg="#66FCF1", font=("calibri", 30)).grid(row=0, column=0)
text2 = Label(left, text="Get access to your\n orders, Wishlist,\n Recommendations", bg="#1A1A1D", fg="#CB2D6F",
              font=("arial", 15)).grid(row=1, column=0)

img = PhotoImage(left, file='logo png.png').subsample(8, 8)
L = Label(left, image=img).grid(row=4, column=0)

text3 = Label(right, text="Enter Username ", font=("calibri", 20)).grid(row=0, column=2)
text4 = Label(right, text="Enter Password ", font=("calibri", 20)).grid(row=1, column=2)

e1 = Entry(right)
e1.grid(row=0, column=3,ipadx=40)
e2 = Entry(right, show='*')
e2.grid(row=1, column=3,ipadx=40)
a = e1.get()
b = e2.get()
# print(b)
b1 = Button(right, text="Login", fg="Black", height=1, width=20, command=confirm).grid(row=2, column=2, columnspan=2)
text5 = Label(right, text="New to Cene? Create a new account ", fg="grey", font=("calibri", 10)).grid(row=3, column=2,
                                                                                                      columnspan=2)
b2 = Button(right, text="Register", fg="Black", height=1, width=20, command=register).grid(row=4, column=2,
                                                                                           columnspan=2)
b3 = Button(right, text="ADMIN", fg="Black", height=1, width=20, command=Admin.adminlogin).grid(row=6, column=2, columnspan=2)

t.mainloop()
