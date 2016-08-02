import csv
import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost',
                              database='employees')
cursor = cnx.cursor()

query = ("SELECT first_name,last_name FROM `employees` WHERE `birth_date` = '1954-05-01' ")


cursor.execute(query)
name=[]
for fname,lname in cursor:
	print("Firstname:- {} Lastname:- {} ".format(fname,lname))
	name.append([fname,lname])
#print (Name)


out = open('out.csv', 'w')
writer = csv.DictWriter(out, fieldnames = ["First Name", "Last Name"])
writer.writeheader()

for row in name:
	writer.writerow({'First Name': row[0], 'Last Name': row[1]})
	out.write('\n')
out.close()

  

cursor.close()
cnx.close()