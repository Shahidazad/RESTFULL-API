from multiprocessing import connection
# from select import select 
import sqlite3

connection=sqlite3.connect('data.db')

cursor=connection.cursor()

create_table="CREATE TABLE users (id int,username text,password text)"
cursor.execute(create_table) 


# sample data insert
user=(1,'jose','asdf')  # insert data 
insert_query="INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query,user)



users=[
    (2,'rolf','asdf'),
    (3,'anne','xyz'),
    

]


cursor.executemany(insert_query,users)  # insert many

select_query="SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row   )







connection.commit()  # save change

connection.close()