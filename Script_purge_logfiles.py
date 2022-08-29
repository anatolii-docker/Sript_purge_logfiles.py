import shutil    # Библиотека для копирования файлов
import os        # Библиотека для того что бы узнать размер файла и его наличие (файла)
import sys       # Для аргументов в CLI


if(len(sys.argv) < 4):
    print("Недостаточно аргументов!   Script_purge_logfiles.py  10  5")  # 10 - размер логфайла в килобайтах; 5 - количество создоваемых логфайлов
    exit(1)

file_name = sys.argv[1]
limitsize = int(sys.argv[2])
logsnumber = int(sys.argv[3])

if(os.path.isfile(file_name) == True):          #Проверка существует ли основной лог файл
    logfile_size = os.stat(file_name).st_size   # Проверка размера файлов в байтах
    logfile_size = logfile_size / 1024          # Переводим байты в килобайты

    if(logfile_size >= limitsize):
        if(logsnumber > 0):
            for currentFileNum in range(logsnumber, 1, -1):
                src = file_name + "_" + str(currentFileNum - 1)
                dst = file_name + "_" + str(currentFileNum)
                if(os.path.isfile(src) == True):
                    shutil.copyfile(src, dst)

                shutil.copyfile(file_name, file_name + "_1")




