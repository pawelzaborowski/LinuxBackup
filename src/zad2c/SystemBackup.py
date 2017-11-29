#!/usr/bin/python

import datetime
import glob
import gzip
import os
import shutil
import tarfile

__author__ = 'Hubert Kozij & Pawel Zaborowski'
__version__ = '1.0'


def confirm():
    user_confirm = input("Kontynuuowac? tak/nie\n")
    global exit_
    if user_confirm == 'tak':
        exit_ = 0
        return exit_
    elif user_confirm == 'no':
        exit_ = 1
        return exit_
    else:
        print("Wpisz tak lub nie")
        confirm()


def addToArchive(self, dest, backup_dirs, name='backup'):
    time = datetime.datetime.now().strftime('%d%m%Y-%H:%M')
    with tarfile.open(dest + '/' + name + time + '.tar.gz', mode='w|gz') as archive:
        for dir in backup_dirs:
            archive.add(dir, recursive=True)



        # https://www.ibm.com/developerworks/library/l-config/index.html
        # http://www.comptechdoc.org/os/linux/commands/linux_crspfiles.html




backup_dirs = ["/etc",
               "/proc",
               "/usr/local"
               ]



print('Foldery do zapisania:\n')
for dir in backup_dirs:
    print(dir)

addToArchive('/home/pawel/Documents', backup_dirs, 'system_backup')


