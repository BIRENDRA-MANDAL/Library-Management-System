#------------------------------PYTHON MODULE : ISSUE-----------------------------------------------
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os
import platform
##############################################################################################################################
def clrscreen():
    if platform.system()=="Windows":
        os.system("cls")
##############################################################################################################################
def ShowIssuedBooks():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='PANTHER123',  host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        query = " SELECT BookRecord.Bno,BookRecord.Bname,Issue.Mno,d_o_issue,d_o_return FROM BookRecord JOIN Issue ON BookRecord.Bno=Issue.Bno"
        Cursor.execute(query)
        for (Bno,Bname,Mno,doi,dor) in Cursor:
            print("==============================================================")
            print("Book Code : ",Bno)
            print("Book Name : ",Bname)
            print("Member Code : ",Mno)
            print("Date of issue : ",doi)
            print("Date of return : ",dor)
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
                cnx.close()
################################################################################################################
def issueBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book Code to issue : ")
        Mno=input("Enter Member Code : ")
        print("Enter Date of Issue (Date,Month and Year seperately): ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        Qry = "INSERT INTO Issue (Bno,Mno,d_o_issue) VALUES (%s, %s, %s)"
        data = (Bno,Mno,date(YY,MM,DD))
        Cursor.execute(Qry,data)
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
#####################################################################################################################
def returnBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Bno=input("Enter Book Code of Book to be returned to the Library : ")
        Mno=input("Enter Member Code of Member who is returning Book : ")
        RetDate=date.today()
        Qry =("""Update Issue SET d_o_return= %s WHERE Bno = %s and Mno= %s """)
        rec=(RetDate,Bno,Mno)
        Cursor.execute(Qry,rec)
# Make sure data is committed to the database
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
########################################################################################################################
def requestBook():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Mno=input("Enter Member Code of Member who wants to request Book : ")
        BookRequests=input("Enter name of the book to be requested:")
        Qry =("""INSERT INTO BookRequests VALUES(%s,%s)""")
        rec=(Mno,BookRequests)
        Cursor.execute(Qry,rec)
# Make sure data is committed to the database
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
