from language_menu import language as lang
import time
from search_us_file import search_file as sf
import threading
from Jarvis import main_loop



T = "\t\t\t\t"


def animation1():
    for item in lang.animation2:
        print(f"{T}{item}")
        time.sleep(0.4)
        lang.clear_terminal()
        if sf.finish == True:
            break



def Menu_Jarvis():

    lang.clear_terminal()
    lang.animation_welcome()
    time.sleep(1)
    lang.clear_terminal()

    print(f"{T}{lang.UA[0]}\n")
    print(f"({lang.UA[1]})\n")

    time.sleep(1)

    print(f"{T}'{lang.UA[2]}'")
    input("")

    lang.clear_terminal()


    while True:

        print(f"{T}{lang.UA[3]}\n \
    {T}{lang.UA[4]}\n\
    {T}{lang.UA[5]}\n")

        choose = int(input())

        if choose == 1:
            lang.clear_terminal()

            print(f"{T}Зараз тут нічого немає")

            print(f"{T}'{lang.UA[6]}'")
            choose = str(input())

            if choose == "q":
                lang.clear_terminal()
                
            else:
                pass

        elif choose == 2:
            thread = threading.Thread(target = sf.found)
            
            thread.start()
            animation1() 
            thread.join()
        
            
        elif choose == 3:
            main_loop()
                


Menu_Jarvis()




