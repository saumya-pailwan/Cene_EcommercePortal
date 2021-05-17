"""from tkinter import *


def addpro():
    font1 = ("BahnSchrift Light SemiCondensed", 50)
    font2 = ("Berlin Sans FB", 15)
    addpro = Tk()
    addpro.geometry("1920x1080")
    addpro.config(bg="black")
    Label(addpro, text="ADD PRODUCT PAGE", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                             column=0,
                                                                                                             columnspan=10,
                                                                                                             padx=200,
                                                                                                             ipadx=50,
                                                                                                             ipady=50)
    a = Frame(addpro, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Product Id", font=font2, background="#F25278", foreground="white")
    l1.grid(row=3, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_id = Entry(a, background="#F25278", font=font2)
    pro_id.grid(row=3, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Product Name", font=font2, background="#F25278", foreground="white")
    l2.grid(row=4, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_name = Entry(a, background="#F25278", font=font2)
    pro_name.grid(row=4, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Product Price", font=font2, background="#F25278", foreground="white")
    l3.grid(row=5, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_price = Entry(a, background="#F25278", font=font2)
    pro_price.grid(row=5, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Product Stock", font=font2, background="#F25278", foreground="white")
    l4.grid(row=6, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_stock = Entry(a, background="#F25278", font=font2)
    pro_stock.grid(row=6, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    font2 = ("Berlin Sans FB", 15)

    addpro.mainloop()"""
# addpro()
from tkinter import *
from tkinter import messagebox
import sqlite3


def inspro():
    def get_insgui():
        idp = pro_id.get()
        name = pro_name.get()
        desc = pro_desc.get()
        price = pro_price.get()
        stock = pro_stock.get()
        ids = pro_shop.get()
        disc = pro_disc.get()
        category = category_box.curselection()[0]
        b.add_product(idp, name, desc, price, stock, ids, disc, category)

    font2 = ("Berlin Sans FB", 15)
    font1 = ("Berlin Sans FB", 50)
    inspro = Tk()
    scroll = Scrollbar(inspro)
    scroll.grid(row=0, column=20, ipady=20)
    inspro.geometry("1920x1080")
    inspro.config(bg="black")
    inspro.title("Insert Product Page")
    Label(inspro, text="ADD PRODUCT PAGE", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                             column=0,
                                                                                                             columnspan=10,
                                                                                                             padx=200,
                                                                                                             ipadx=50,
                                                                                                             ipady=50)
    a = Frame(inspro, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Product Id", font=font2, background="#F25278")
    l1.grid(row=3, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_id = Entry(a, background="#F25278", font=font2)
    pro_id.grid(row=3, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Product Name", font=font2, background="#F25278")
    l2.grid(row=4, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_name = Entry(a, background="#F25278", font=font2)
    pro_name.grid(row=4, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    ld = Label(a, text="Enter Product Description", font=font2, background="#F25278")
    ld.grid(row=5, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_desc = Entry(a, background="#F25278", font=font2)
    pro_desc.grid(row=5, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Product Price", font=font2, background="#F25278")
    l3.grid(row=6, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_price = Entry(a, background="#F25278", font=font2)
    pro_price.grid(row=6, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Product Stock", font=font2, background="#F25278")
    l4.grid(row=7, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_stock = Entry(a, background="#F25278", font=font2)
    pro_stock.grid(row=7, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l6 = Label(a, text="Enter Shop Id", font=font2, background="#F25278")
    l6.grid(row=8, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_shop = Entry(a, background="#F25278", font=font2)
    pro_shop.grid(row=8, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l5 = Label(a, text="Enter Discount", font=font2, background="#F25278")
    l5.grid(row=9, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_disc = Spinbox(a, background="#F25278", from_=0, to=100)
    pro_disc.grid(row=9, column=6, columnspan=1, padx=10, ipadx=60, ipady=10, sticky=W)

    l5 = Label(a, text="Select Category ", font=font2, background="#F25278")
    l5.grid(row=10, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    cat = StringVar()
    list_items = ["Tops", "Dresses", "Kurtas and Suits", "Sarees", "Accessories", "Jewellery", "Shirts", "Trousers",
                  "Informals", "Indian Wear", "Grains and Pulses", "Spices and Condiments", "Snacks", \
                  "Cook Essentials", "Cleaners", "Stationary", "Skin and Hair care", "makeup", "cloth decors",
                  "serving items", "Decorative pieces", "Kitchen storage", "Paintings", \
                  "Wall Hangings", "Craft Section", "Gift Items"]
    category_box = Listbox(a, listvariable=cat)
    category_box.grid(row=10, column=6, columnspan=5, rowspan=2, ipadx=70, ipady=10, sticky=W)

    for category in list_items:
        category_box.insert('end', category)

    scrollbar = Scrollbar(a)
    scrollbar.grid(row=10, column=11, rowspan=2, ipady=50, sticky=W)
    category_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=category_box.yview)

    addbutton = Button(a, text="ADD PRODUCT", bg="dark turquoise", command=get_insgui)
    addbutton.grid(row=14, column=6, pady=10, ipadx=20, ipady=10)

    font2 = ("Berlin Sans FB", 15)

    inspro.mainloop()


def editpro():
    def get_insgui():
        idp = pro_id.get()
        name = pro_name.get()
        desc = pro_desc.get()
        price = pro_price.get()
        stock = pro_stock.get()
        ids = pro_shop.get()
        disc = pro_disc.get()
        cat = category_box.curselection()[0]
        b.modify_product(idp, name, desc, price, stock, ids, disc, cat)

    font1 = ("BahnSchrift Light SemiCondensed", 50)
    font2 = ("Berlin Sans FB", 15)
    editpro = Tk()
    editpro.geometry("1920x1080")
    editpro.title("Modify product page")
    editpro.config(bg="black")
    Label(editpro, text="MODIFY PRODUCT PAGE", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                                 column=0,
                                                                                                                 columnspan=10,
                                                                                                                 padx=200,
                                                                                                                 ipadx=50,
                                                                                                                 ipady=50)
    a = Frame(editpro, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Product Id", font=font2, background="#F25278")
    l1.grid(row=3, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_id = Entry(a, background="#F25278", font=font2)
    pro_id.grid(row=3, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Product Name", font=font2, background="#F25278")
    l2.grid(row=4, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_name = Entry(a, background="#F25278", font=font2)
    pro_name.grid(row=4, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    ld = Label(a, text="Enter Product Description", font=font2, background="#F25278")
    ld.grid(row=5, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_desc = Entry(a, background="#F25278", font=font2)
    pro_desc.grid(row=5, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Product Price", font=font2, background="#F25278")
    l3.grid(row=6, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_price = Entry(a, background="#F25278", font=font2)
    pro_price.grid(row=6, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Product Stock", font=font2, background="#F25278")
    l4.grid(row=7, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_stock = Entry(a, background="#F25278", font=font2)
    pro_stock.grid(row=7, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l6 = Label(a, text="Enter Shop Id", font=font2, background="#F25278")
    l6.grid(row=8, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_shop = Entry(a, background="#F25278", font=font2)
    pro_shop.grid(row=8, column=6, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l5 = Label(a, text="Enter Discount", font=font2, background="#F25278")
    l5.grid(row=9, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    pro_disc = Spinbox(a, background="#F25278", from_=0, to=100)
    pro_disc.grid(row=9, column=6, columnspan=1, padx=10, ipadx=60, ipady=10, sticky=W)

    l5 = Label(a, text="Select Category ", font=font2, background="#F25278")
    l5.grid(row=10, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    cat = StringVar()
    list_items = ["Tops", "Dresses", "Kurtas and Suits", "Sarees", "Accessories", "Jewellery", "Shirts", "Trousers",
                  "Informals", "Indian Wear", "Grains and Pulses", "Spices and Condiments", "Snacks", \
                  "Cook Essentials", "Cleaners", "Stationary", "Skin and Hair care", "Makeup", "Cloth Decors",
                  "Serving items", "Decorative pieces", "Kitchen storage", "Paintings", \
                  "Wall Hangings", "Craft Section", "Gift Items"]
    category_box = Listbox(a, listvariable=cat)
    category_box.grid(row=10, column=6, columnspan=5, rowspan=2, ipadx=70, ipady=10, sticky=W)

    for category in list_items:
        category_box.insert('end', category)

    scrollbar = Scrollbar(a)
    scrollbar.grid(row=10, column=11, rowspan=2, ipady=50, sticky=W)
    category_box.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=category_box.yview)

    editbutton = Button(a, text="EDIT PRODUCT", bg="dark turquoise", command=get_insgui)
    editbutton.grid(row=14, column=6, pady=10, ipadx=20, ipady=10)

    font2 = ("Berlin Sans FB", 15)

    editpro.mainloop()


def inspro1():
    def get_setgui():
        ids = s_id.get()
        namec = c_name.get()
        names = s_name.get()
        conts = s_contact.get()
        b.add_supplier(ids, names, namec, conts)

    font1 = ("BahnSchrift Light SemiCondensed", 50)
    font2 = ("Berlin Sans FB", 15)
    inspro1 = Tk()
    inspro1.geometry("1920x1080")
    inspro1.config(bg="black")
    Label(inspro1, text="SUPPLIER PAGE", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                           column=0,
                                                                                                           columnspan=10,
                                                                                                           padx=200,
                                                                                                           ipadx=50,
                                                                                                           ipady=50)

    a = Frame(inspro1, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Supplier Id", font=font2, background="#F25278", foreground="white")
    l1.grid(row=3, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_id = Entry(a, background="#F25278", font=font2)
    s_id.grid(row=3, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Company Name", font=font2, background="#F25278", foreground="white")
    l2.grid(row=4, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    c_name = Entry(a, background="#F25278", font=font2)
    c_name.grid(row=4, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Supplier Name", font=font2, background="#F25278", foreground="white")
    l3.grid(row=5, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_name = Entry(a, background="#F25278", font=font2)
    s_name.grid(row=5, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Contact No", font=font2, background="#F25278", foreground="white")
    l4.grid(row=6, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_contact = Entry(a, background="#F25278", font=font2)
    s_contact.grid(row=6, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    font2 = ("Berlin Sans FB", 15)

    b1 = Button(inspro1, text="Add Supplier", fg="Black", font=font2, background="dark turquoise", height=1,
                width=20,
                command=get_setgui).grid(row=8, column=0, ipadx=15, ipady=10,
                                         columnspan=2)
    inspro1.mainloop()


def editpro1():
    def get_setgui1():
        ids = s_id.get()
        namec = c_name.get()
        names = s_name.get()
        conts = s_contact.get()
        b.modify_supplier(ids, names, namec, conts)

    font1 = ("BahnSchrift Light SemiCondensed", 50)
    font2 = ("Berlin Sans FB", 15)
    editpro1 = Tk()
    editpro1.geometry("1920x1080")
    editpro1.config(bg="black")
    Label(editpro1, text=" MODIFY SUPPLIER", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                              column=0,
                                                                                                              columnspan=10,
                                                                                                              padx=200,
                                                                                                              ipadx=50,
                                                                                                              ipady=50)

    a = Frame(editpro1, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)
    l1 = Label(a, text="Enter Supplier Id", font=font2, background="#F25278", foreground="white")
    l1.grid(row=3, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_id = Entry(a, background="#F25278", font=font2)
    s_id.grid(row=3, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Enter Company Name", font=font2, background="#F25278", foreground="white")
    l2.grid(row=4, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    c_name = Entry(a, background="#F25278", font=font2)
    c_name.grid(row=4, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l3 = Label(a, text="Enter Supplier Name", font=font2, background="#F25278", foreground="white")
    l3.grid(row=5, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_name = Entry(a, background="#F25278", font=font2)
    s_name.grid(row=5, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    l4 = Label(a, text="Enter Contact No", font=font2, background="#F25278", foreground="white")
    l4.grid(row=6, column=1, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    s_contact = Entry(a, background="#F25278", font=font2)
    s_contact.grid(row=6, column=6, columnspan=5, padx=10, ipadx=15, ipady=10, sticky=W)

    font2 = ("Berlin Sans FB", 15)

    b1 = Button(editpro1, text="MODIFY Supplier", fg="Black", font=font2, background="dark turquoise", height=1,
                width=20,
                command=get_setgui1).grid(row=8, column=0, ipadx=15, ipady=10,
                                          columnspan=2)
    editpro1.mainloop()


def admin():
    admin = Tk()
    font1 = ("Berlin Sans FB", 50)
    font2 = ("Berlin Sans FB", 15)
    admin.geometry('1000x1000')
    Label(admin, text="ADMIN MENU", foreground="dark turquoise", font=font1).grid(row=0, column=0, ipadx=20, padx=20,
                                                                                  pady=20)
    Label(admin, text="Products", font=font2).grid(row=4, column=0)
    Label(admin, text="Suppliers", font=font2).grid(row=4, column=1)
    a = Button(admin, text="  Add Product", bg="dark turquoise", font=font2, command=sel)
    a.grid(row=5, column=0, ipadx=20, ipady=20, padx=10, pady=10)
    b = Button(admin, text="Modify Product", bg="slate gray1", font=font2, command=get)
    b.grid(row=6, column=0, ipadx=20, ipady=20, padx=10, pady=10)
    c = Button(admin, text="  Add Supplier", bg="orange", font=font2, command=sup)
    c.grid(row=5, column=1, ipadx=20, ipady=20, padx=10, pady=10)
    d = Button(admin, text="Modify Supplier", bg="light coral", font=font2, command=mod)
    d.grid(row=6, column=1, ipadx=20, ipady=20, padx=10, pady=10)


def sel():
    b.get_values(0)


def get():
    b.get_values(1)


def sup():
    b.get_values(2)


def mod():
    b.get_values(3)


class Admin:
    def _init_(self):
        admin()

    def get_values(self, val):
        print("Im there")
        print(val)
        if (val == 0):
            # print("Inside")
            inspro()
        elif (val == 1):
            editpro()
        elif (val == 2):
            # whatever is name of your page
            inspro1()
        elif (val == 3):
            editpro1()

        else:
            print("Only these much options")

    def add_product(self, idp, name, desc, price, stock, ids, disc, cat):
        # print("Hi")
        print(idp, name, desc, price, stock, ids, disc, cat)
        # insert into db
        conn = sqlite3.connect("projE_DB.db")
        cursor = conn.cursor()
        cursor.execute('select count(supplier_id) from supplier where supplier_id= (?)', (ids,))
        ab = cursor.fetchone()[0]
        print(ab)
        count = ab
        print(count)
        if (count == 0):
            pass
            # it means that supplier isnt  existing,display error message
            print("No")
            messagebox.showinfo("Shop Error", "The Supplier ID you entered doesnt exist.Please check credentials")
        elif (count == 1):
            cursor.execute(
                'insert into product(product_id,product_name,product_desc,quantity,discount,unit_price,supplier_id,category_id) values(?,?,?,?,?,?,?,?)',
                (idp, name, desc, stock, disc, price, ids, cat))
            conn.commit()
        cursor.close()
        conn.close()

    def modify_product(self, idp, name, desc, price, stock, ids, disc, cat):
        print(idp, name, desc, price, stock, ids, disc, cat)
        print("IM editing")
        # modify those values
        conn = sqlite3.connect("projE_DB.db")
        cursor = conn.cursor()
        cursor.execute('select count(supplier_id) from supplier where supplier_id= (?)', (ids,))
        ab = cursor.fetchone()[0]
        print(ab)
        count = ab
        print(count)
        if (count == 0):
            pass
            # it means that supplier isnt  existing,display error message
            print("No")
            messagebox.showinfo("Shop Error", "The Supplier ID you entered doesnt exist.Please check credentials")
        elif (count == 1):
            cursor.execute('select count(product_id) from product where product_id= (?)', (idp,))
            ac = cursor.fetchone()[0]
            print(ac)
            if (ac == 1):
                cursor.execute(
                    'update product set product_id=? ,product_name=?,product_desc=?,quantity=?,discount=?,unit_price=?,supplier_id=?,category_id=? where product_id=?',
                    (idp, name, desc, stock, disc, price, ids, cat, idp))
                conn.commit()
        cursor.close()
        conn.close()

    def add_supplier(self, ids, sname, c_name, s_contact):
        # print(ids, sname, c_name, s_contact)
        conn = sqlite3.connect("projE_DB.db")
        cursor = conn.cursor()
        cursor.execute('select count(supplier_id) from supplier where supplier_id= (?)', (ids,))
        ab = cursor.fetchone()[0]
        print(ab)
        count = ab
        print(count)
        if (count != 0):
            # print("No")
            messagebox.showinfo("Shop Error", "The Supplier ID you entered doesnt exist.Please check credentials")
        cursor.execute(
            'insert into supplier(supplier_id,supplier_name,company_name,contact) values(?,?,?,?)',
            (ids, sname, c_name, s_contact))
        conn.commit()
        cursor.close()
        conn.close()

    def modify_supplier(self, ids, sname, c_name, s_contact):
        # print(idp, name, desc, price, stock, ids, disc, cat)
        # print("IM editing")
        # modify those values
        conn = sqlite3.connect("projE_DB.db")
        cursor = conn.cursor()
        cursor.execute('select count(supplier_id) from supplier where supplier_id= (?)', (ids,))
        ab = cursor.fetchone()[0]
        print(ab)
        count = ab
        print(count)
        if (count == 0):
            messagebox.showinfo("Shop Error", "The Supplier ID you entered doesnt exist.Please check credentials")

        cursor.execute('select count(supplier_id) from product where supplier_id= (?)', (ids,))
        ac = cursor.fetchone()[0]
        print(ac)
        cursor.execute(
            'update supplier set supplier_name=?,company_name=?,contact=? where supplier_id=?',
            (sname, c_name, s_contact, ids))
        conn.commit()
        cursor.close()
        conn.close()


b = Admin()
