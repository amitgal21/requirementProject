from tkinter import *
from queryFiles.yourdetailsQuery import *

global text1, text2, text3, text4, text5, text6, text7, text8, text9, update_pass
global mail, password, firstname, lastname, country, city, age, field


# ====================== YOUR DETAILS SCREEN SHOW IN USER SCREEN ========================


def put_details_on_screen(window):
    global text1, text2, text3, text4, text5, text6, text7, text8, text9, update_pass
    text1 = Label(
        window,
        anchor="nw",
        text="Private Name: " + globalsVar.private_Name_global,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text1.place(x=350, y=250)

    text2 = Label(
        window,
        anchor="nw",
        text="Last Name: " + globalsVar.last_name_global,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text2.place(x=350, y=300)

    text3 = Label(
        window,
        anchor="nw",
        text="Email: " + globalsVar.mail_from_login,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text3.place(x=350, y=350)

    text4 = Label(
        window,
        anchor="nw",
        text="Password: " + globalsVar.password_global,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text4.place(x=350, y=400)

    text5 = Label(
        window,
        anchor="nw",
        text="Optional Details",
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 22 * -1),
        bg="#272A37"
    )
    text5.place(x=750, y=200)
    if globalsVar.country_global is not None:
        country_text = "Country: " + globalsVar.country_global
    else:
        country_text = "Country: Unknown"
    text6 = Label(
        window,
        anchor="nw",
        text=country_text,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text6.place(x=750, y=250)
    if globalsVar.country_global is not None:
        city_text2 = "City: " + globalsVar.city_global
    else:
        city_text2 = "City: Unknown"
    text7 = Label(
        window,
        anchor="nw",
        text=city_text2,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text7.place(x=750, y=300)
    if globalsVar.country_global is not None:
        age_text3 = "Age: " + globalsVar.age_global
    else:
        age_text3 = "Age: Unknown"
    text8 = Label(
        window,
        anchor="nw",
        text=age_text3,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text8.place(x=750, y=350)
    if globalsVar.country_global is not None:
        field_text3 = "Hobbie: " + globalsVar.field_global
    else:
        field_text3 = "Hobbie: Unknown"
    text9 = Label(
        window,
        anchor="nw",
        text=field_text3,
        fg="#FFFFFF",
        font=("yu gothic ui Bold", 18 * -1),
        bg="#272A37"
    )
    text9.place(x=750, y=400)
    # ======= Update password Button ============
    update_pass = Button(window, fg='#f8f8f8', text='Change Details', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                         cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                         command=lambda: want_update_details())
    update_pass.place(x=500, y=500, width=256, height=45)


def want_update_details():
    global mail, password, firstname, lastname, country, city, age, field
    win = Toplevel()
    window_width = 700
    window_height = 500
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Update Details')
    # win.iconbitmap('images\\aa.ico')
    win.configure(background='#272A37')
    win.resizable(False, False)

    # ====== Email ====================
    mail = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                 bd=0, state="readonly", disabledforeground="#FFFFFF", foreground="#FFFFFF")
    mail.place(x=40, y=80, width=256, height=50)
    mail.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    email_label = Label(win, text='• Email', fg="#FFFFFF", bg='#272A37',
                        font=("yu gothic ui", 11, 'bold'))
    email_label.place(x=40, y=50)

    # ====  Password ==================
    password = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                     bd=0)
    password.place(x=40, y=180, width=256, height=50)
    password.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    password_label = Label(win, text='• Password', fg="#FFFFFF", bg='#272A37',
                           font=("yu gothic ui", 11, 'bold'))
    password_label.place(x=40, y=150)

    # ====  First name ==================
    firstname = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                      bd=0)
    firstname.place(x=40, y=280, width=256, height=50)
    firstname.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    first_label = Label(win, text='• First Name', fg="#FFFFFF", bg='#272A37',
                        font=("yu gothic ui", 11, 'bold'))
    first_label.place(x=40, y=250)

    # ====  lastname name ==================
    lastname = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                     bd=0)
    lastname.place(x=40, y=380, width=256, height=50)
    lastname.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    last_label = Label(win, text='• Last Name', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 11, 'bold'))
    last_label.place(x=40, y=350)

    # ======= Update details Button ============
    upurdet = Button(win, fg='#f8f8f8', text='Update Details', bg='#1D90F5', font=("yu gothic ui", 12, "bold"),
                     cursor='hand2', relief="flat", bd=0, highlightthickness=0, activebackground="#1D90F5",
                     command=lambda: change_details_inDB(win))
    upurdet.place(x=200, y=440, width=256, height=45)

    # ====== Country ====================
    country = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                    bd=0)
    country.place(x=350, y=80, width=256, height=50)
    country.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    country_label = Label(win, text='• Country', fg="#FFFFFF", bg='#272A37',
                          font=("yu gothic ui", 11, 'bold'))
    country_label.place(x=350, y=50)

    # ====  City ==================
    city = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                 bd=0)
    city.place(x=350, y=180, width=256, height=50)
    city.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    city_label = Label(win, text='• City', fg="#FFFFFF", bg='#272A37',
                       font=("yu gothic ui", 11, 'bold'))
    city_label.place(x=350, y=150)

    # ====  Age ==================
    age = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                bd=0)
    age.place(x=350, y=280, width=256, height=50)
    age.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    age_label = Label(win, text='• Age', fg="#FFFFFF", bg='#272A37',
                      font=("yu gothic ui", 11, 'bold'))
    age_label.place(x=350, y=250)

    # ====  Field ==================
    field = Entry(win, bg="#3D404B", font=("yu gothic ui semibold", 12), highlightthickness=1,
                  bd=0)
    field.place(x=350, y=380, width=256, height=50)
    field.config(highlightbackground="#3D404B", highlightcolor="#206DB4")
    field_label = Label(win, text='• Your Hobbies', fg="#FFFFFF", bg='#272A37',
                        font=("yu gothic ui", 11, 'bold'))
    field_label.place(x=350, y=350)

    mail.insert(0, globalsVar.mail_from_login)
    password.insert(0, globalsVar.password_global)
    firstname.insert(0, globalsVar.private_Name_global)
    lastname.insert(0, globalsVar.last_name_global)
    if globalsVar.country_global is not None:
        country.insert(0, globalsVar.country_global)
    if globalsVar.city_global is not None:
        city.insert(0, globalsVar.city_global)
    if globalsVar.age_global is not None:
        age.insert(0, globalsVar.age_global)
    if globalsVar.field_global is not None:
        field.insert(0, globalsVar.field_global)
    '''country.insert(0, globalsVar.country_global)
    city.insert(0, globalsVar.city_global)
    age.insert(0, globalsVar.age_global)
    field.insert(0, globalsVar.field_global)'''


def change_details_inDB(win):
    # make update query
    send_to_db(globalsVar.mail_from_login, password.get(), firstname.get(), lastname.get(), country.get(), city.get(),
               age.get(), field.get())
    # update the new detials in details screen
    globalsVar.age_global = age.get()
    globalsVar.field_global = field.get()
    globalsVar.city_global = city.get()
    globalsVar.password_global = password.get()
    globalsVar.private_Name_global = firstname.get()
    globalsVar.last_name_global = lastname.get()
    globalsVar.country_global = country.get()
    messagebox.showinfo("Congrats", "Your Details has been Updated")
    win.destroy()
    from UserScreen import home_func
    home_func()


# @@@@@ clean the screen when we leave details screen
def clear_details_screen():
    text1.destroy()
    text2.destroy()
    text3.destroy()
    text4.destroy()
    text5.destroy()
    text6.destroy()
    text7.destroy()
    text8.destroy()
    text9.destroy()
    update_pass.destroy()
