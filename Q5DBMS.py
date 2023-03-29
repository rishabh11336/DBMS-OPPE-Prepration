#Problem Statement:
#Write a Python program to print the name and date of birth, year of joining(since) is a leap year as “Yes” or “No” of the manager of the player. 
#Player's name is given in a file named 'player.txt' resides in the same folder as python program file. 

#The output of the python program is only manager's name, date of birth, year of joining is a leap year as “Yes” or “No”.
 
#For example, 'Adom' and '1991-02-17' is the name and date of birth of the manager of the player's name 'Jerry'. '2020-02-15' is the year of joining. 2020 is a leap year. Then, the final output will be Adom,1991-02-17,Yes only. Note: No spaces and the date format should be the same as shown.
#For example, 'Brandon' and '1995-02-15' is the name and date of birth of the manager of the player's name 'Kabir'. '2019-04-02' is the year of joining. 2019 is not a leap year. Then, the final output will be Brandon,1995-02-15,No only. Note: No spaces and the date format should be the same as shown.


import sys
import os
import psycopg2

file = open("player.txt","r")
p_name = file.read()

try:
    connection = psycopg2.connect(
        database = sys.argv[1],
        user = os.environ.get('PGUSER'),
        password = os.environ.get('PGPASSWORD'),
        host = os.environ.get('PGHOST'),
        port = os.environ.get('PGPORT'))
    
    cursor = connection.cursor()
    query = "select managers.name, managers.dob, managers.since from managers,players where players.name = '{}' and players.team_id = managers.team_id".format(p_name)
    
    cursor.execute(query)
    
    result = cursor.fetchall()
    
    def Leap(year):
        if (year % 4 == 0) and (year % 100 != 0):
            return True
        elif year%100 == 0 and (year % 400 == 0):
            return True
        else:
            return False
    
    for res in result:
        if Leap(res[2].year):
            print(res[0]+","+str(res[1])+","+"Yes")
        else:
            print(res[0]+","+str(res[1])+","+"No")
    
    cursor.close()
except(Exception, psycopg2.DatabaseError) as error:
    print(error)
finally:
    connection.close
