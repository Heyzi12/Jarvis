import pyfiglet
import os
import time
import colorama

Jarvis_text_welcome_animation1 = pyfiglet.figlet_format("J" , font="isometric2")
Jarvis_text_welcome_animation2 = pyfiglet.figlet_format("JA" , font="isometric2")
Jarvis_text_welcome_animation3 = pyfiglet.figlet_format("JAR" , font="isometric2")
Jarvis_text_welcome_animation4 = pyfiglet.figlet_format("JARV" , font="isometric2")
Jarvis_text_welcome_animation5 = pyfiglet.figlet_format("JARVI" , font="isometric2")
Jarvis_text_welcome_animation6 = pyfiglet.figlet_format("JARVIS" , font="isometric2")

a = [Jarvis_text_welcome_animation1 , Jarvis_text_welcome_animation2, Jarvis_text_welcome_animation3 , Jarvis_text_welcome_animation4 , Jarvis_text_welcome_animation5 , Jarvis_text_welcome_animation6]

def clear_terminal() -> None: 
    os.system('cls' if os.name == 'nt' else 'clear')

def animation_welcome() -> None:

    for animation_cadr in a:
        clear_terminal()
        print(colorama.Fore.BLUE + colorama.Style.DIM + animation_cadr + colorama.Style.RESET_ALL)
        time.sleep(0.5)
    time.sleep(2)
    clear_terminal()

animation2 = [" \\" , " |" , " /" , "--"]  * 55    





UA = [
    "Привіт вітаю тебе в Jarvis",
    "Увага : " + "радиться запустити перевірочний файл якщо ви хочете щоб джарвіс вам відкривав ваші програми",
    "Нажміть Enter",
    "1. Настройки",
    "2. Запустити перевірку",
    "3. Запустити Джарвіс",
    "q - вийти",
    "програму закрито",
    "процес вже завершено",
    colorama.Fore.WHITE + "не втиг завершитися " + colorama.Style.RESET_ALL + colorama.Fore.RED + "- доведеться вбити" + colorama.Style.RESET_ALL,
    "процес не знайдено"
]

