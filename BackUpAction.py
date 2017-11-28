#!/usr/bin/python


import sys, os, shutil

import gzip
import tarfile
import glob
import time
import datetime
import re


__author__ = 'Hubert Kozij & Pawel Zaborowski'
__version__ = '1.0'


def chceckIfDirExist(self, os_dir):
    if not os.path.exists(os_dir):
        print(os_dir, "Nie ma takiego katalogu\n")
        exit(1)


def confirm(self):
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
        self.confirm()


def addToArchive(dest, backup_dirs, name):
    time = datetime.datetime.now().strftime('%d%m%Y_%H:%M')
    with tarfile.open(dest + '/' + name + time + '.tar.gz', mode='w|gz') as archive:
        for dir in backup_dirs:
            archive.add(dir, recursive=True)


def restore():
    os.chdir('/home/pawel/temp')   #/
    date = re.search(r'[0-3]+[0-9]+"_"[0-23]?":"[0-59]?')
    tar = tarfile.open("/home/pawel/Documents/repositories_backup" + date + "tar.gz")
    tar.extractall()
    tar.close()



backup_dirs = ['/etc',
               '/proc',
               '/usr/local'
               ]

bck_dir = ['/home/pawel/Downloads/ASK-projekt/dbs/mySql/mySqlDb1',
           '/home/pawel/Downloads/ASK-projekt/dbs/mySql/mySqlDb2'
           '/home/pawel/Downloads/ASK-projekt/dbs/postgreSql/16385',
           '/home/pawel/Downloads/ASK-projekt/dbs/postgreSql/16386']

repo_bck = ['/home/pawel/Downloads/ASK-projekt/repos/Svn/repSvn1',
            '/home/pawel/Downloads/ASK-projekt/repos/Svn/repSvn1']


print('Foldery do zapisania:\n')
for dir in backup_dirs:
    print(dir)

for dir in bck_dir:
    print(dir)

for dir in repo_bck:
    print(dir)

"""
addToArchive('/home/pawel/Documents', repo_bck, 'repositories_backup')

addToArchive('/home/pawel/Documents', bck_dir, 'DB_backup')

addToArchive('/home/pawel/Documents', backup_dirs, 'system_backup')
"""
restore()