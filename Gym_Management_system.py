import mysql.connector

mydb = mysql.connector.connect(user="root", password = "mysql", host="localhost",database = "shilp")
print(mydb)   # <mysql.connector.connection_cext.CMySQLConnection object at 0x000002582DADC6D0>

if mydb.is_connected():
    print("Database Connected...")
else:
    print("Not Connected...")


cur = mydb.cursor()

cur.execute("create table if not exists cust_details (ID INT PRIMARY KEY AUTO_INCREMENT, NAME VARCHAR(30), GENDER CHAR, CONTACT INT, USERNAME VARCHAR(30), PASSWORD VARCHAR(30))")

cur.execute("create table if not exists phy_details1 (PID int primary key, Name varchar(30) not null, height float not null, weight float not null, bmi float, diet varchar(30), ID int, foreign key (ID) REFERENCES CUST_DETAILS(ID)) ")

# cur.execute()

print("Gym Management System".center(40))

try:
    while True:
        print("1 ---- Signup")
        print("2 ---- Login")
        print("3 ---- Exit")

        choice = int(input("Enter your Choice: "))
        if choice == 1:
            username = input("Enter Email ID: ")

            q = "select username from cust_details"

            cur.execute(q)

            x = cur.fetchall()   # [("w1@gmail.com",), ("Aman@gmail.com",)]
            
            h = 0
            for subtup in x:
                if subtup[0] == username:
                    h=1
                    print('User ID Taken')
                    break

            if h == 0:

                password = input("Enter Password: ")
                name = input("Enter Name: ")
                gender = input("Enter Gender: ")
                contact = int(input("Enter Contact No: "))


                q = "INSERT INTO CUST_DETAILS (NAME, GENDER, CONTACT, USERNAME, PASSWORD) VALUES (%s, %s, %s, %s, %s)"
                val1 = (name, gender, contact, username, password)
                cur.execute(q,val1)

                mydb.commit()

                height = float(input("Enter Height: "))
                weight = float(input("Enter weight: "))


                q = "select id, name from cust_details where username = %s"
                a = (username,)
                cur.execute(q,a)

                data1 = cur.fetchone()

                id1 = data1[0]
                name1 = data1[1]


                q1 = "INSERT INTO PHY_DETAILS1(NAME, HEIGHT, WEIGHT, ID) VALUES (%s, %s, %s, %s)"
                val2 = (name1, height, weight, id1)
                cur.execute(q1, val2)
                mydb.commit() 

        elif choice == 2:
            user_name = input("Enter UserName: ")
            user_pass = input("Enter Password: ")

            cur.execute("select username, password from cust_details")


            # print("-----")
            ans = cur.fetchall()   # ans = [('Aman@gmail.com', 'Ashok@123'), ('Manoj@gmail.com', 'fg@890')]
            f = 0
            for subtup in ans:   # subtup = ('Aman@gmail.com', 'Ashok@123')
                if subtup[0] == user_name and subtup[1] == user_pass:
                    print("Login Successfull...")
                    f=1
                    break
            
            if f == 0:
                print("Cred. Invalid, Try again")
                continue

        elif choice == 3:
            print("Thank You !!")
            break


except:
    print("An Error Occured")