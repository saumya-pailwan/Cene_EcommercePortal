from tkinter import *
import tkinter as tk


def inspro():
    font1 = ("BahnSchrift Light SemiCondensed", 50)
    font2 = ("Berlin Sans FB", 15)
    inspro = Tk()
    inspro.geometry("1920x1080")
    inspro.config(bg="black")
    Label(inspro, text="MODIFY SUPPLIER", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                          column=0,
                                                                                                          columnspan=10,
                                                                                                          padx=200,
                                                                                                          ipadx=50,
                                                                                                          ipady=50)


    a = Frame(inspro, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Supplier Id", font=font2, background="#F25278", foreground="white")
    l1.grid(row=3, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_id = Entry(a, background="#F25278", font=font2)
    pro_id.grid(row=3, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Company Name", font=font2, background="#F25278", foreground="white")
    l2.grid(row=4, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_name = Entry(a, background="#F25278", font=font2)
    pro_name.grid(row=4, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Supplier Name", font=font2, background="#F25278", foreground="white")
    l3.grid(row=5, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_price = Entry(a, background="#F25278", font=font2)
    pro_price.grid(row=5, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Contact No", font=font2, background="#F25278", foreground="white")
    l4.grid(row=6, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_stock = Entry(a, background="#F25278", font=font2)
    pro_stock.grid(row=6, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    font2 = ("Berlin Sans FB", 15)

    b1 = Button(inspro, text="Add Supplier", fg="Black", font=font2, background="dark turquoise", height=1, width=20,
                command=addpro).grid(row=8, column=0, ipadx=15, ipady=10,
                                     columnspan=2)
    inspro.mainloop()


inspro()
