from tkinter import messagebox
import mysql.connector
import globalsVar
import MainScreen

global mycursor, mydb


# check if the details are illegal and then if its legal he goes to the next view


# forgot password QUERY to update the new password
def update_password_query(mail, new_password):
    global mycursor, mydb
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="redb")
        mycursor = mydb.cursor()
        # Update password
        mycursor.execute("UPDATE redb.mamas SET password = %s WHERE mail = %s", (new_password, mail))
        mydb.commit()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to update password: {error}")
    finally:
        mycursor.close()
        mydb.close()


# this for forgot password to check if the details are legal
def check_exist(mail):
    global mycursor, mydb
    mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!",
                                   database="redb")

    # Check login field
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM redb.mamas WHERE mail = %s", (mail,))
    result = mycursor.fetchone()
    if result:
        return True
    return False


def sign_up_query(firstName, lastName, mail, password):
    global mycursor, mydb
    try:
        mydb = mysql.connector.connect(host="localhost", user="root", password="Shitrit1!", database="redb")
        mycursor = mydb.cursor()
        # Update password
        query = "INSERT INTO redb.mamas (mail, password, name, lastname) VALUES (%s, %s, %s, %s)"
        mycursor.execute(query, (mail, password, firstName, lastName))
        mydb.commit()

    except mysql.connector.Error as error:
        messagebox.showerror("Error", "Failed to update password: {error}")
    finally:
        mycursor.close()
        mydb.close()
