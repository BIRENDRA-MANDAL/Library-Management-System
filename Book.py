#-------------------------------MODULE NAME:BOOK-------------------------------------------
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import connection
import os
import platform
####################################################################################################
def clrscreen():
    if platform.system()=="Windows":
        os.system("cls")
####################################################################################################
def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost',
        database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM BookRecord")
        Cursor.execute(query)
        for (Bno,Bname,Author,Price,Publ,Qty,d_o_purchase) in Cursor:
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",Price)
            print("Publisher : ",Publ)
            print("Total Quantity in Hand : ",Qty)
            print("Purchased On : ",d_o_purchase)
            print("===============================================================")
        Cursor.close()
        cnx.close()
        print("You have done it!!!!!!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    else:
        cnx.close()
#########################################################################################################################################
def insertData():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book Code : ")
        Bname=input("Enter Book Name : ")
        Auth=input("Enter Book Author's Name : ")
        Price=int(input("Enter Book Price : "))
        Publ=input("Enter Publisher of Book : ")
        Qty=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date,Month and Year seperately): ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = "INSERT INTO BookRecord VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (Bno,Bname,Auth,Price,Publ,Qty,date(YY,MM,DD))
        Cursor.execute(Qry,data)
# Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted..............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()
######################################################################################################################################
def deleteBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book Code of Book to be deleted from the Library : ")
        Qry =("""DELETE FROM BookRecord WHERE Bno = %s""")
        del_rec=(Bno,)
        Cursor.execute(Qry,del_rec)
# Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Deleted Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()
######################################################################################################################################
def SearchBookRec():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book No to be Searched from the Library : ")
        query = ("SELECT * FROM BookRecord where Bno = %s ")
        rec_srch=(Bno,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (Bno,Bname,Author,Price,Publ,Qty,d_o_purchase) in Cursor:
            Rec_count+=1
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Author of Book : ",Author)
            print("Price of Book : ",Price)
            print("Publisher : ",Publ)
            print("Total Quantity in Hand : ",Qty)
            print("Purchased On : ",d_o_purchase)
            print("===============================================================")
            if Rec_count%2==0:
                input("Press any key to continue")
                clrscreen()
                print(Rec_count, "Record(s) found")
# Make sure data is committed to the database
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()
#######################################################################################################################################
def UpdateBook():
    try:
        cnx = connection.MySQLConnection(user='root',  password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book Code of Book to be Updated from the Library : ")
        query = ("SELECT * FROM BookRecord where Bno = %s ")
        rec_srch=(Bno,)
        print("Enter new data ")
        Bname=input("Enter Book Name : ")
        Auth=input("Enter Book Author's Name : ")
        Price=int(input("Enter Book Price : "))
        Publ=input("Enter Publisher of Book : ")
        Qty=int(input("Enter Quantity purchased : "))
        print("Enter Date of Purchase (Date,Month and Year seperately): ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = "UPDATE BookRecord SET Bname=%s,Author=%s, Price=%s,Publ=%s,Qty=%s,d_o_purchase=%s  WHERE Bno=%s"
        data = (Bname,Auth,Price,Publ,Qty,date(YY,MM,DD),Bno)
        Cursor.execute(Qry,data)
# Make sure data is committed to the database'''
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount,"Record(s) Updated Successfully.............")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
            cnx.close()
