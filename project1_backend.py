import mysql.connector
#import project1_frontend

def studentData():
        con = mysql.connector.connect(host="localhost",user="root",passwd="#password",database="project")
        cur=con.cursor()
       
        cur.execute("CREATE TABLE IF NOT EXISTS srikanth(id integer primary key AUTO_INCREMENT,StdID text,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
        con.commit()
        con.close()              
def addStdRec(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="#password")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("INSERT INTO srikanth VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close() 
def viewData():
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="#password")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("select * from srikanth")
        row=cur.fetchall()
        con.close()       
        return row
def deleteRec(id):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="#password")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("DELETE FROM srikanth WHERE id=%s",(id,))
        con.commit()
        con.close()         
def searchData(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile):
        con=con = mysql.connector.connect(host="localhost",user="root",passwd="#password")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("SELECT * FROM srikanth WHERE StdID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        rows=cur.fetchall()
        con.close()        
        return rows
def dataUpdate(id,StdID="",Firstname="",Surname="",DoB="",Age="",Gender="",Address="",Mobile=""):
        con = mysql.connector.connect(host="localhost",user="root",passwd="#password")
        cur=con.cursor()
        cur.execute("use project")
        cur.execute("UPDATE srkanth SET StdID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",(StdID,Firstname,Surname,DoB,Age,Gender,Address,Mobile))
        con.commit()
        con.close()    
