# import the PostgreSQL adapter for Python


from __future__ import print_function
import mysql.connector
from mysql.connector import errorcode

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="mypass123",
    database="lascope")

#Show Tables
def show_table():
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES")
    for x in mycursor:
        print(x) 

#Create Table empty first
def create_table(table_name):
    # Connect to the MySQL database server
    mycursor = mydb.cursor()
    mycursor.execute("CREATE TABLE "+table_name+" (id INT AUTO_INCREMENT UNIQUE KEY)")

#alter table to add column
def alter_table(params):
    print("Alter Table"+params[0]+" with=>",params)
    mycursor = mydb.cursor()

    #on définit le type
    if params[3]=="Texte":
        tpe="VARCHAR(255)"
    elif params[3]=="Date":
        tpe="DATETIME"
    else:
        tpe="FLOAT"
    mycursor.execute("ALTER TABLE "+params[0]+" ADD COLUMN "+params[1]+" "+tpe+" AFTER id")
    if params[4]==2:
        print("ALTER TABLE "+params[0]+" ADD FOREIGN KEY ("+str(params[1])+") REFERENCES "+params[5]+"("+str(params[1])+") ON DELETE RESTRICT ON UPDATE RESTRICT")
        mycursor.execute("ALTER TABLE "+params[0]+" ADD FOREIGN KEY ("+str(params[1])+") REFERENCES "+str(params[5])+"("+str(params[1])+") ON DELETE RESTRICT ON UPDATE RESTRICT")
    elif params[4]==1:
        print("ALTER TABLE "+params[0]+" ADD PRIMARY KEY ("+params[1]+")")
        mycursor.execute("ALTER TABLE "+str(params[0])+" ADD PRIMARY KEY ("+params[1]+")")
    else:
        pass
