import psutil
import os
import time
from language_menu import language as lang
#from search_us_file import programs_my_pc as pmp

def search_ranning_program(name):
    found = False
    for proc in psutil.process_iter(["name"]):
        
        if proc.info["name"] and name.lower() in proc.info["name"].lower():
            found = True
            try:
                proc.terminate()    
                proc.wait(timeout=5)
                print(lang.UA[7])
            
            except psutil.NoSuchProcess:
                print(lang.UA[8])
                time.sleep(1)

            except psutil.TimeoutExpired:
                print(lang.UA[9])
                time.sleep(1)
                proc.kill()
            
    if not found:
        print(lang.UA[10])
    


def found_file(name):
    search_ranning_program(name)
    time.sleep(1)


#print(pmp.keys[2])
#found_file(pmp.keys[2])
        