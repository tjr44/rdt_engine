#now work with functions note time
import time
import os
from typing import Any

class ReqErr(Exception):
        pass

#OTO-inheritence(one to one)
class another:
        def __init__(self,file_name):
                try:
                    self.pro_dir = str(file_name).split('\\')
                    #record current time
                    self.rc_t = time.strftime('%I:%M:%S %p')   #type(c_t_n) <class 'str'>
                    #record current date
                    self.rc_d = time.strftime('%d-%b-%Y')
                    #current date and time
                    self.c_dt = time.strftime('%d-%b-%Y >>> %I:%M:%S %p')
                    #only module name using path class baesname(__file__) function
                    self.module_name = os.path.basename(file_name)
                    #full path of module
                    self.module_path = file_name
                    #this helps prevent default module_name
                    if self.module_name == 'run_m.py':
                            raise ReqErr("\033[91m you necessary to add \033[94m ` __file__ ` \033[0m \033[91m variable onto \033[94m ntime_code_name class\033[0m")
                    #file store operation
                    #currect time note # add data without erase and trancate the existsing data a also, create file wihout Filenot found error if is not exists
                    with open('ntime_date.py','a') as ntdo:
                         ntdo.write(f"\n#date : `{self.rc_d}` at directory : `{self.pro_dir[-2]}`  module name :`{self.module_name}`   time :`{self.rc_t}`")
                    """`Terminal return`s"""
                    #time record into ntime_date
                    print(f"\033[92m \ncurrent module and datetime was recored:) ---> \033[91m`{self.module_name}\033[0m` , \033[94m`{self.c_dt}`\033[0m \033[0m at package : \033[92m >>>\033[91m `{self.pro_dir[-2]}`\033[0m\n")

                except ReqErr as request_error:
                      "you must do enter __file__ Argument into the ntime_code_name class"
                      print(f"Error : {request_error}")
                
                except Exception:
                       print("\033[91m Error :  Check...Code...please...check...code \033[0m")
                finally:
                  pass

#OTO-inheritence(one to one)
class ntime_code_name(another):
          '''
                varibles-Datamembers
          '''
          #init should return None not list
          def __init__(self,file_name):
                super(ntime_code_name,self).__init__(file_name)
                self.return_list =  [self.rc_d, self.rc_t, self.pro_dir[1], self.module_name]
          

#tri_underscore main function very important private method treadted by python 
def ___main___() -> Any:
        n2c = ntime_code_name(__file__)

if __name__ == f'__main__':
        ___main___()  