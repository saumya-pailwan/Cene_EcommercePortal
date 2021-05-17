import tkinter
from tkinter import *
import Addprodct


def adminlogin():
    ad = Tk()
    ad.geometry('900x450')
    font1 = ("BahnSchrift Light SemiCondensed", 50, "bold")
    font2 = ("BahnSchrift Light SemiCondensed", 20, "bold")
    Label(ad, text="ADMIN LOGIN", font=font1, foreground="Orange").grid(row=0, column=0, columnspan=10,
                                                                                padx=200, ipadx=50, ipady=50)


    def check():
        if ad_user.get() == "SASA" and ad_pass.get() == "SaAdShAn":
            tkinter.messagebox.showinfo("Login", "Login Successful")
            ad.destroy()
            Addprodct.admin()

    a = Frame(ad, background="#F25278", height=50, width=100)
    u = Label(ad, text="Username", font=font2)
    u.grid(row=3, column=1, columnspan=1, padx=10, pady=5, ipadx=15, ipady=10, sticky=W)

    ad_user = Entry(ad, font=font2)
    ad_user.grid(row=3, column=6, columnspan=1, padx=10, pady=5, ipadx=15, ipady=10, sticky=W)

    p = Label(ad, text="Password", font=font2)
    p.grid(row=6, column=1, columnspan=1, padx=10, ipadx=15, pady=5, ipady=10, sticky=W)

    ad_pass = Entry(ad, font=font2, show='*')
    ad_pass.grid(row=6, column=6, columnspan=1, padx=10, ipadx=15, pady=5, ipady=10, sticky=W)

    b_ad = Button(ad, text="Login", font=font2, command=check)
    b_ad.grid(row=8, column=6, padx=20, pady=20, ipadx=10, ipady=10)


    ad.mainloop()


# adminlogin()