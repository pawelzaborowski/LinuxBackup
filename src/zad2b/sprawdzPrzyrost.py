#!/usr/bin/env python
import os
import subprocess
import archiver


def AdditiveBackup(sourceDir, targetDir):
    backup_dir = targetDir
    date = subprocess.Popen(['date', '+%F'], stdout=subprocess.PIPE)
    today, err = date.communicate()
    today = today[:len(today) - 1]

    last_backup = os.system('find /home/quanzig/ASK-projekt/ -maxdepth 1 -name "????-??-??" | sort -g | tail -n 1')

    new_backup = backup_dir + '/' + today
    os.system('mkdir ' + new_backup)

    os.system('rsync -avHz --numeric-ids --progress ' + sourceDir + '/ ' + new_backup + '/')

    archiver.addToArchive(sourceDir, targetDir, today)
