#now work with functions note time
import time
import os
import sys
from typing import Any

class ntime_code_name:
          def __init__(self,file_name = __file__):
                    sys.path.append("C:/rdt_engine")
                    '''
                    varibles-Datamembers
                    '''
                    #record current time
                    rc_t = time.strftime('>>> %I:%M:%S %p')   #type(c_t_n) <class 'str'>
                    #record current date
                    rc_d = time.strftime('%d-%b-%Y')
                    #current date and time
                    c_dt = time.strftime('%d-%b-%Y >>> %I:%M:%S %p')
                    #only module name
                    self.module_name = os.path.basename(file_name)
                    #full path of module
                    self.module_path = file_name

                    #file store operation
                    #currect time note # add data without erase and trancate the existsing data a also, create file wihout Filenot found error if is not exists
                    with open('ntime_date.py','a') as ntdo:
                         ntdo.write(f"#  date : `{rc_d}`   module name :`{self.module_name}`   time :`{rc_t}`\n")

                    """
                    `Terminal return`s
                    """
                    #time record into ntime_date
                    print(f"\033[92m \n\t\t\tfilename and datetime was recored:) ---> \033[91m`{self.module_name}\033[0m` , \033[94m`{c_dt}`\033[0m \n\033[0m")

#tri_underscore main function very important private method treadted by python 
def ___main___() -> Any:
        n2c = ntime_code_name()

if __name__ == f'__main__':
        ___main___()    