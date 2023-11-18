import mysql.connector

mydb = mysql.connector.connect(user="root", password = "mysql", host="localhost",database = "shilp")
print(mydb)   # <mysql.connector.connection_cext.CMySQLConnection object at 0x000002582DADC6D0>

if mydb.is_connected():
    print("Database Connected...")
else:
    print("Not Connected...")


cur = mydb.cursor()

cur.execute("create table if not exists COUNTRIES (CODE INT, NAME VARCHAR(10), GDP FLOAT)")


# cur.execute("insert into countries values (30,'USA',30.90)")
# cur.execute("insert into countries (code, name) values (10,'India')")

# c_code = 67
# n = input("Enter your country Name: ")
# gddp = float(input("Enter Gdp: "))


# query = "insert into countries values (%s, %s, %s)"
# val = (c_code,n,gddp)


# cur.execute(query, val)

# cur.execute("Alter table countries modify code int primary key")

condition = "gdp = %s"
q = f"select * from countries where {condition}"   # fstring
float_value = 30.9000  # Replace with the actual float value you're looking for
parameter_values = (float_value,)
cur.execute(q,parameter_values)
# data = cur.fetchone()
data = cur.fetchall() 

print(data)   # [(20, 'uk', 10.9), (30, 'USA', 30.9)]

for subtup in data:
    print(subtup[1])

mydb.commit()