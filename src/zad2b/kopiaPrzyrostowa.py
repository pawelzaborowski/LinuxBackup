#!/usr/bin/env python
import os
import subprocess
import sys

import zad2b.sprawdzPrzyrost


# na wywolanie podaje sie 3 sciezki - sciezke do pliku z backupem,
# sciezke gdzie koncowy backup sie zapisze i sciezke do bazy danych plikow, ktore sie archiwizuje
# np. python kopiaPrzyrostowa.py /home/quanzig/ASK-projekt/Backups/repos/git/2017-11-28.tar.gz /home/quanzig/ASK-projekt/Backups/repos/git/ /home/quanzig/ASK-projekt/repos/git

def compareBackups():
    filePath = sys.argv[1]  # np. /home/quanzig/ASK-projekt-Backups/repos/git/2017-11-29.tar.gz
    currentPosition = '/tmp/tmpBackup'
    backup_directory = sys.argv[
        2]  # gdzie zapisywany jest backup 		np. /home/quanzig/ASK-projekt/Backups/dbs/postgreSql
    dbs_dierctory = sys.argv[3]  # skad wyciagany jest backup 		np. /home/quanzig/ASK-projekt/dbs/postgreSql
    whatIsBackupped = dbs_dierctory.rsplit('/', 1)[-1]  # wyciaga ostatni wyraz po '/'
    fileName = filePath.rsplit('/', 1)[-1]  # wyciaga nazwe pliku

    # przygotowanie katalogu tymczasowego
    os.system('mkdir ' + currentPosition)
    os.system('cp ' + filePath + ' ' + currentPosition) # anie cd

    # przygotowanie danych do sprawdzenia
    os.chdir(currentPosition)
    os.system('tar -xzf ' + fileName + ' -C ' + currentPosition)

    # zmniejszenie zagniezdzenia katalogow
    # zlokalizowanie najnizszego potrzebnego katalogu (po nazwie danych, ktore backupujemy)
    path = subprocess.Popen(['find', '.', '-mindepth', '3', '-name', whatIsBackupped], stdout=subprocess.PIPE)
    path, err = path.communicate()
    path = path[:len(path) - 1]

    # przekopiowanie potrzebnych danych 'nizej'
    os.chdir(path)
    current_path = subprocess.Popen(['pwd'], stdout=subprocess.PIPE)
    current_path, err2 = current_path.communicate()
    current_path = current_path[:len(current_path) - 1]
    os.system('cp -r ../* ' + current_path + ' ' + currentPosition)

    # sprawdzenie przyrostu
    os.chdir(currentPosition)
    zad2b.sprawdzPrzyrost.AdditiveBackup(dbs_dierctory, currentPosition)

    # usuniecie danych, ktore nie sa nowym backupem
    directories = os.listdir(currentPosition)
    for katalog in directories:
        if katalog.endswith('.tar.gz'):
            print('')
        else:
            os.system('rm -r ' + katalog)

    # przekopiowanie backupu do prawidlowego katalogu
    os.system('cp * ' + backup_directory)

    # sprzatniecie danych tymczasowych
    os.chdir("/tmp/")
    os.system('rm -r ' + "tmpBackup")


compareBackups()
