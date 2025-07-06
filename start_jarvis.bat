@echo off
setlocal enabledelayedexpansion

::Імя файлу який шукаємо
set "filename=menu.py"

:: Шукаємо файл у всіх підпапках
for /r %%f in (*%filename%) do (
    echo Знайдено: %%f

    :: Запуск
    python "%%f"
    goto :eof
)

echo Файл %filename% не знайдено
pause