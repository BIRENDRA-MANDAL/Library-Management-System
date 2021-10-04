#--------------------------------PYTHON MODULE:MEMBER--------------------------------------------------
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import (connection)
import os
import platform
########################################################################################################
def clrscreen():
    if platform.system()=="Windows":
        os.system("cls")
########################################################################################################
def display():
    try:
        os.system('cls')
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        query = ("SELECT * FROM Member")
        Cursor.execute(query)
        for (Mno,Mname,MOB,DOM,ADR) in Cursor:
            print("==============================================================")
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Mobile No.of Member : ",MOB)
            print("Date of Membership : ",DOM)
            print("Address : ",ADR)
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
#######################################################################################################
def insertMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Mno=input("Enter Member Code : ")
        Mname=input("Enter Member Name : ")
        MOB=input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date,Month and Year seperately): ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        ADR=input("Enter Member Address : ")
        Qry = "INSERT INTO Member VALUES (%s, %s, %s, %s, %s)"
        data = (Mno,Mname,MOB,date(YY,MM,DD),ADR)
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
#######################################################################################################
def deleteMember():
    try:
        cnx = connection.MySQLConnection(user='root',  password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Mno=input("Enter Member Code to be deleted from the Library : ")
        Qry =("""DELETE FROM Member WHERE Mno = %s""")
        del_rec=(Mno,)
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
#########################################################################################################
def SearchMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Mname=input("Enter Member Name to be Searched from the Library : ")
        query = ("SELECT * FROM Member where Mname = %s ")
        rec_srch=(Mname,)
        Cursor.execute(query,rec_srch)
        Rec_count=0
        for (Mno,Mname,MOB,DOM,ADR) in Cursor:
            print("==============================================================")
            print("Member Code : ",Mno)
            print("Member Name : ",Mname)
            print("Mobile No.of Member : ",MOB)
            print("Date of Membership : ",DOM)
            print("Address : ",ADR)
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
######################################################################################################
def UpdateMember():
    try:
        cnx = connection.MySQLConnection(user='root', password='PANTHER123', host='localhost', database='Library',auth_plugin='mysql_native_password')
        Cursor = cnx.cursor()
        Mno=input("Enter Member Code of Member to be Updated from the Library : ")
        query = ("SELECT * FROM Member where Mno = %s ")
        rec_srch=(Mno,)
        print("Enter new data ")
        Mname=input("Enter Member Name : ")
        MOB=input("Enter Member Mobile No. : ")
        print("Enter Date of Membership (Date,Month and Year seperately): ")
        DD=int(input("Enter Date : "))
        MM=int(input("Enter Month : "))
        YY=int(input("Enter Year : "))
        ADR=input("Enter Member Address : ")
        Qry = "UPDATE Member SET Mname=%s,MOB=%s,DOM=%s,ADR=%s WHERE Mno=%s"
        data = (Mname,MOB,date(YY,MM,DD),ADR,Mno)
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
###########################################################################################################
