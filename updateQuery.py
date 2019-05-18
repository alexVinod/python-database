import sqlite3

connect = sqlite3.connect('./college.db')
cursor = connect.cursor()

rollno=input("Enter Rollno :")


try:
    getData=cursor.execute('select*from studentDetails where rollno='+rollno)
    regno=str(getData.fetchone()[1])

    if(rollno == regno ):
        name=input("Enter Name :")
        branch=input("Enter Branch :")
        mail=input("Enter Email :")
        mobile=input("Enter MobileNumber :")

        query="update studentDetails set name=?, branch=?, email=?,mobiles=? where rollno=?"
        cursor.execute(query,(name,branch,mail,mobile,rollno))
        connect.commit()
    else:
        print("Warning : You Are Not Authencated Person, Perform this Operation ...!")
        
except Exception as e:
    print(e)
    print("Warning : You Are Not Authencated Person, Perform this Operation ...!")

cursor.close()
connect.close()
