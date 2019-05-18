import sqlite3

connect = sqlite3.connect('./college.db')
cursor = connect.cursor()

rollno=input("Enter Rollno :")
name=input("Enter Name :")
branch=input("Enter Branch :")
mail=input("Enter Email :")
mobile=input("Enter MobileNumber :")

query="insert into studentDetails(rollno,name,branch,email,mobiles) values(?,?,?,?,?)"

cursor.execute(query,(rollno,name,branch,mail,mobile))

connect.commit()
print("Successfully Inserted...!")

cursor.close()
connect.close()
