import os
from search_us_file import programs_my_pc



us_file = "" #тут буде силка на файл який шукає

ff = None #це для того щоб зробити змінну глобальною

finish = None


name = None #це теж саме


# список файлів яких потрібно найти
file_found = ["Spotify.exe" , "Jarvis.py", "Telegram.exe" , "steam.exe" , "Code.exe"] 


"""
ФУНКЦІЯ ДЛЯ ПОШУКУ ФАЙЛА
"""

def found_us_file() -> None:
    
    def file_find(file_name, search_path = "C:\\"): # ця функція принімає значення імя файлу та шлях по якому шкукати
        global ff # робимо змінну глобальною
        for root , dirs , files in os.walk(search_path): # перебирає root , деректорії і файли деректорій

            for file_need in files: # перебирає "потрібний файл" з файлами деректорій
                if file_need.endswith(".exe") and file_name == file_need:# перевіряє чи цей файл має кінець ".exe" 
                                                            # та перевіряє чи назма розшукуємого файлу має таку саму назву як і "потрібний файл"

                        ff = True
                        print(file_need)
                        return os.path.join(root, file_name) #повертає назву нашого файлу
                
                if file_need.endswith(".py") and file_name == file_need:# те саме що і в 26 рядку тільки з ".py"
                        
                        ff = True
                        return os.path.join(root, file_name)
                
        else: # якщо файл не находять то повертаємо False
            ff = False
            return ff
            


    def file_exe(file_found): # ця функція принімає список 
        global us_file # зробить деректорію файлу глобальною
        global name # робить змінну імя глобальною

        for name in file_found: # імя перебирає розшукуймі файли

            us_file = file_find(name) # використовує верхню функцію 

            if programs_my_pc.keys[0] == name:
                programs_my_pc.programs[programs_my_pc.keys[0]] = us_file 
    
            if programs_my_pc.keys[1] == name:
                programs_my_pc.programs[programs_my_pc.keys[1]] = us_file 

            if programs_my_pc.keys[2] == name:
                programs_my_pc.programs[programs_my_pc.keys[2]] = us_file 

            if programs_my_pc.keys[3] == name:
                programs_my_pc.programs[programs_my_pc.keys[3]] = us_file

            if programs_my_pc.keys[4] == name:
                programs_my_pc.programs[programs_my_pc.keys[4]] = us_file

            
            if us_file != ff: # якщо ff = True 
                
                
                print(us_file) # то виводиться деректорія

            
                   

            else:
                print(f"Програму не знайдено : {name}")
                
        
    

    return file_exe



start = found_us_file()

file_exe = start

def found():
    
    print(file_exe(file_found))
    global finish 
    finish = True
    with open("data_file_user.py" , "w" , encoding="utf8") as f:
     
     f.write("programs = ")
     f.write(str(programs_my_pc.programs))
     
    return finish





     
