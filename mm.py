import mysql.connector as m
conn=m.connect(host="localhost",user="root",password="",database='librarydb')

print("connection is successfull")
cursor=conn.cursor()
#def _displaystudentdata():

def _availablebook(s):
    sub=s
    #cursor.execute("select * from `book` WHERE accessionnumber NOT in (select accessionnumber from `issue` WHERE returndate is null)")
    cursor.execute("SELECT * FROM `book` NATURAL JOIN `title` WHERE title LIKE '%"+sub+"%'")
    record=cursor.fetchall()
    for row in record:
        print(row)
#_availablebook("c")
def getfinedetails():
    cursor.execute("SELECT fname,lname,(datediff(CURRENT_DATE,issuedate)-7)*50 AS fine FROM `issue` NATURAL JOIN `student` WHERE(datediff(CURRENT_DATE,issuedate)>7)")
    record = cursor.fetchall()
    for row in record:
        print(row)
getfinedetails()
