#importaions of mysql.connector
import mysql.connector
from run_m import ntime_code_name

run_m = ntime_code_name()
#connect to mysql server
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password='',
    database='dbs_fntd'
)

#data varible import data
rc_d , rc_t , pro_dir , module_name = run_m.rc_d , run_m.rc_t , run_m.pro_dir , run_m.module_name
#create a cursor
cursor = conn.cursor()

#data varibles
queue = 0
recored_datetime = f'date : `{rc_d}` at directory : `{pro_dir[-2]}`  module name :`{module_name}`   time :`{rc_t}`'

#execute cursor in mysql-server to handle mysql database technology
cursor.execute("use dbs_fntd;")
cursor.execute("INSERT INTO rdt_table(queue,recored_datetime) value(%s,%s);",(queue,recored_datetime))

#commit present changes(means save)
conn.commit()

#got data from database by database-server(db_server)
cursor.execute("select * from rdt_table;")
for record in cursor.fetchall():#read the records
    print(record)

#close opened connections
cursor.close()
conn.close()