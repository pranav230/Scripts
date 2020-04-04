import mysql.connector
import csv

con = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Your Password"
)

cur = con.cursor()

cur.execute("USE DbName")
cur.execute("""
select col1,col2 from table
where <cond>
""")

with open('Filename.csv',mode='w') as data:
	fieldnames=["Field1","Field2"]
	writer=csv.DictWriter(data,fieldnames=fieldnames)
	writer.writeheader()
	for i in cur:
		writer.writerow({'Field1':i[0],'Field2':i[1]})