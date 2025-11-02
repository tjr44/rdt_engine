#importaions of mysql.connector
import db
import mysql.connector
from typing import Any

#database not connected error
class dbncError(Exception):
       pass

def db_connect_code():
        #connect to mysql server
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password='',
            database='dbs_fntd'
        )
        return conn

def db_commands(conn):
            conn = db_connect_code()
            
            #data varible import data
            rc_d , rc_t , pro_dir , module_name = db.cdbwd[0] ,db.cdbwd[1], db.cdbwd[2] , db.cdbwd[3]

            #data varible
            #number of recordings
            nor = 0
            recored_datetime = f'date : `{rc_d}` at directory : `{pro_dir}`  module name :`{module_name}`   time :`{rc_t}`'

            #create a cursor
            cursor = conn.cursor()

            #execute cursor in mysql-server to handle mysql database technology
            cursor.execute("use dbs_fntd;")
            cursor.execute("INSERT INTO rdt_table(recored_datetime,nor) value(%s,%s);",(recored_datetime,nor))

            #commit present changes(means save)
            conn.commit()

            #got data from database by database-server(db_server)
            cursor.execute("select * from rdt_table;")

            #read all data from database inside the func
            def db_run_terminal():
                   for record in cursor.fetchall():
                          print(f'''\033[91m 
                                In DataBase Table `rdt_table` :
                                {record}
''')
            
            #close opened connections
            cursor.close()
            conn.close()

class run_mysql_db:
            def __init__(self,):
                    try:
                        conn = db_connect_code()
                        
                        #data varible import data
                        rc_d , rc_t , pro_dir , module_name = db.cdbwd[0] ,db.cdbwd[1], db.cdbwd[2] , db.cdbwd[3]

                        #data varible
                        #number of recordings
                        nor = 0
                        recored_datetime = f'date : `{rc_d}` at directory : `{pro_dir}`  module name :`{module_name}`   time :`{rc_t}`'

                        #create a cursor
                        cursor = conn.cursor()

                        #execute cursor in mysql-server to handle mysql database technology
                        cursor.execute("use dbs_fntd;")
                        cursor.execute("INSERT INTO rdt_table(recored_datetime,nor) value(%s,%s);",(recored_datetime,nor))

                        #commit present changes(means save)
                        conn.commit()

                        #got data from database by database-server(db_server)
                        cursor.execute("select * from rdt_table;")

                        #read all data from database in func
                        def db_run_terminal():
                                for record in cursor.fetchall():#read the records
                                     print(f''' 
                                {record}
                                     ''')
                                     
                        #close opened connections
                        cursor.close()
                        conn.close()

                        #if database not connect raise database not connect error(db_nc)
                        if not conn:
                              raise dbncError(f"\033[91m Error: \033[0m\033[92m DataBase is not connected! I am working Background Process in Progress:)")
                        
                    except dbncError as Edbnc:#Error dbnc
                            print(Edbnc)
                            while True:
                                if db_connect_code == True:
                                        #loop breaks if is sucessfully connected:)
                                        break
                                if db_connect_code() == False:
                                        #loop continues trying to connect database
                                        db_connect_code()
                                        db_commands(db_connect_code())
                    except Exception:
                           pass

                    finally:
                        pass

def ___main___() -> Any:
       rdb = run_mysql_db()

if __name__ == f'__main__':
      ___main___()