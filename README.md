# Sript_purge_logfiles.py
Скрипт для очистки лог-файла. 
Этот скрипт делает чистку лог-файлов, Если вы не хотите чтобы ваш лог-файл не превышал кокого то размера (к примеру 100мБ), то вы в параметрах (в первом параметре), при запуске скрипта, указываете, нужный вам размер файла (в килобайтах). И если лог файл превышает данный размер, то он создает копию лог-файла, куда записывает все логи, а основной лог файл очищает. Вторым параметром вы указываете сколько последующих копий лог-файла создавать, при этом данные основного лог-файла копируются в первую копию, а данные первой копии в третью и тд..


Запускаем скрипт через командную строку python Sript_purge_logfiles.py и прописываем тут же два аргумента:
python Sript_purge_logfiles.py 100 5    где: 100 - это размер логфайла в килобайтах,  5 - максимальное количество создаваемых копий лог-файлов.
