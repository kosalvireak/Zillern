# # file_name = 'text.txt'
# # file_name = 'from_client_'+ file_name
# # file = open(file_name,'x')


# file = open('text.txt')

# content = file.readlines()
# i = 0
# while True:
    
#     print(content[i])
#     i = i + 1
#     if content[i-1] == '':
#         break

import mysql.connector

dataBase = mysql.connector.connect(

    host="localhost",

    user="root",

    passwd="",

    database="kosalvireak"
)


cursorObject = dataBase.cursor()
f = open("Light sensor.txt","r")
for x in f:
    res = x.split()
    sql = "INSERT INTO tbl_STUDENT (NAME, EMAIL) VALUES (%s, %s)"
    val = (str(res[0]), str(res[1]))
    cursorObject.execute(sql, val)
    dataBase.commit()