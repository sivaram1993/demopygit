import MySQLdb.connections
mydb = MySQLdb.connections.Connection(host='localhost', user='Sivaram', passwd='1234', database='SAMPLE')
mycursor = mydb.cursor()
mycursor.execute("select * from student")
for i in mycursor:
    print(i)
