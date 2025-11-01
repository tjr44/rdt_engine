#database store from ntime_date.py .file
import mysql.connector

conn = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='',
    database='dbs_fntd'
)


#creating cursor
cursor = conn.cursor()

with open("ntime_date.py",'r+') as raw_data :
     #line by line data bundling and holding
     lbl = raw_data.readlines()

for line in range(len(lbl) -1):
     if lbl[line].strip().startswith('#'):
          comment = lbl[line].strip()

#insert data into database and that table
ist_rdt = f'''
'''
