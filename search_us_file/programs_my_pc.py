

key = None # ключ


# список програм
programs = {
    "Spotify.exe" : r"",
    "Jarvis.py" : r"",
    "Telegram.exe" : r"",
    "steam.exe" : r"",
    "Code.exe" : r""
} 


# ключі які порівнюються з назвою розшуковоного файлу
keys = ["Spotify.exe" , "Jarvis.py" , "Telegram.exe" , "steam.exe" , "Code.exe"]



"""
ФУНКЦІЯ ЩО ПОВЕРТАЄ ДИРЕКТОРІЮ ФАЙЛУ
"""
def get_program(key , programs) -> None:
    if key != None: # якщо ключ пустий програма нічого не шукатиме
        get_dir = programs[key] 
        return get_dir
    else:
        print("asd")




