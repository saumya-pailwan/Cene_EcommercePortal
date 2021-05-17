from tkinter import *
import sqlite3
import functools
from datetime import date
import datetime
import random


def cart_gui(cust_id):
    font2 = ("Berlin Sans FB", 15)
    font1 = ("Berlin Sans FB", 50)
    cart = Tk()

    cart.geometry("1920x1080")
    cart.config(bg="black")
    cart.title("My Shopping Cart")
    Label(cart, text="MY SHOPPING CART", font=font1, background="black", foreground="dark turquoise").grid(row=0,
                                                                                                           column=0,
                                                                                                           columnspan=10,
                                                                                                           padx=200,
                                                                                                           ipadx=50,
                                                                                                           ipady=50)
    a = Frame(cart, background="#F25278", height=50, width=100)
    a.grid(row=5, column=0, ipadx=170, ipady=10, padx=40, pady=20)

    pro_id_list = []
    prices_list = []
    qty_list = []
    conn = sqlite3.connect('projE_DB.db')
    cursor = conn.cursor()

    cursor.execute('select count(product_id) from cart where customer_id=(?)', (cust_id,))
    count1 = cursor.fetchone()[0]
    print(count1)

    for i in range(count1):
        pro_id_list.append(0)
        prices_list.append(0)
        qty_list.append(0)

    pro = cursor.execute('select * from cart where customer_id= ?', (cust_id,))
    i = -1
    for x in pro:
        i = i + 1
        pro_id_list[i] = x[0]
    print(pro_id_list)
    i = -1
    for j in pro_id_list:
        i = i + 1
        ab = cursor.execute('select unit_price,discount from product where product_id=(?)', (j,))
        for y in ab:
            mainprice = y[0]
            disc = y[1]
        prices_list[i] = mainprice - mainprice * (disc / 100)
    print(prices_list)

    labels = []
    prices = []
    qty = []

    def fill():
        cost = 0
        for i in range(count1):
            print(qty[i].get())
            qty_list[i] = int(qty[i].get())
            cost = cost + prices_list[i] * qty_list[i]
            cursor.execute('update cart set no_of_products=(?) where product_id=(?) and customer_id=(?)',
                           (qty_list[i], pro_id_list[i], cust_id))
            conn.commit()

        l9 = Label(a, text=cost, font=font2, background="#F25278")
        l9.grid(row=count1 + 6, column=3, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)
        cursor.close()
        conn.close()

    def ab(cust_id):
        cost = 0
        print(cust_id)
        for i in range(count1):
            print(qty[i].get())
            qty_list[i] = int(qty[i].get())
            cost = cost + prices_list[i] * qty_list[i]
        print(cost)

        place1(cust_id, cost)

    l1 = Label(a, text="Product ID ", font=font2, background="#F25278")
    l1.grid(row=3, column=1, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l2 = Label(a, text="Cost per Item  ", font=font2, background="#F25278")
    l2.grid(row=3, column=2, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l5 = Label(a, text="Quantity", font=font2, background="#F25278")
    l5.grid(row=3, column=3, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    count = 0
    for i in range(count1):
        labels.append(Label(a, text=pro_id_list[i], font=font2, background="#F25278"))
        labels[i].grid(row=i + 4, column=1, padx=10, ipadx=15, ipady=10, sticky=W)

        prices.append(Label(a, text=prices_list[i], font=font2, background="#F25278"))
        prices[i].grid(row=i + 4, column=2, padx=10, ipadx=15, ipady=10, sticky=W)

        qty.append(Spinbox(a, background="#F25278", from_=0, to=5))
        qty[i].grid(row=i + 4, column=3, columnspan=1, padx=10, ipadx=60, ipady=10, sticky=W)

    place = Button(a, text="CONFIRM DETAILS", bg="dark turquoise", command=fill)
    place.grid(row=13, column=3, pady=10, ipadx=20, ipady=10)

    l3 = Label(a, text="No . of Products :  ", font=font2, background="#F25278")
    l3.grid(row=count1 + 5, column=2, columnspan=1, padx=10, ipadx=15, ipady=20, sticky=S)

    l4 = Label(a, text="Cost Total", font=font2, background="#F25278")
    l4.grid(row=count1 + 6, column=2, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    l5 = Label(a, text=count1, font=font2, background="#F25278")
    l5.grid(row=count1 + 5, column=3, columnspan=1, padx=10, ipadx=15, ipady=10, sticky=W)

    plac = Button(a, text="PLACE ORDER", bg="dark turquoise", command=functools.partial(ab, cust_id))
    plac.grid(row=14, column=3, pady=10, ipadx=20, ipady=10)

    cart.mainloop()


def place1(cust_id, cost):
    """print(cust_id)
    print(cost)"""

    conn = sqlite3.connect('projE_DB.db')
    cursor = conn.cursor()
    cursor.execute('select count(order_id) from order_info')
    x = cursor.fetchone()[0]
    # print(x)
    idr = x + 1
    # print(date.today() + datetime.timedelta(days=1))
    cursor.execute('select count(shipper_id) from shipper')
    sc = cursor.fetchone()[0]
    sid = random.randint(8801, 8801 + sc)
    # print(sid)
    cursor.execute('insert into order_info values(?,?,?,?,?)',(idr,date.today(),date.today()+datetime.timedelta(days=1),cust_id,sid))
    conn.commit()
    cursor.execute('select address from customer where customer_id=(?)', (cust_id,))
    address = cursor.fetchone()[0]
    cursor.execute('insert into billing_info values(?,?,?,?,?,?)', (idr, date.today(), address, cost, cust_id, idr))
    conn.commit()
    cursor.close()
    conn.close()

# cart_gui()