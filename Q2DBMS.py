#Write a Python program to print the roll number of the student. Student's first name is given in a file named 'name.txt' resides in the same folder as
#python program file.
#The output of the python program is only roll number.  
#For example, if the first name of the student is 'Vikas'. Then output must be CS01 only. Note: No spaces.



import sys
import os
import psycopg2

file = open("name.txt","r")
name = file.read()

try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.environ.get('PGHOST'),
        port = os.environ.get('PGPORT'))
        
    cursor = connection.cursor()
    query = "select roll_no from students where student_fname = '{}'".format(name)
    
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    for res in result:
        print(res[0])
        
    cursor.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close
