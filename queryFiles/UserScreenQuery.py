from tkinter import messagebox
import mysql.connector

import globalsVar


def details_of_user_query(mail):
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!",
                                   database="redb")

    # Check login field
    print(mail)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT name,lastname FROM redb.mamas WHERE mail = %s", (mail,))
    result = mycursor.fetchone()
    mydb.commit()
    if result:
        globalsVar.private_Name_global = result[0]
        globalsVar.last_name_global = result[1]
    else:
        messagebox.showerror('Error', "DataBase PROBLEM")

