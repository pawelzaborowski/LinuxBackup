#!/usr/bin/python

import os


def restore():
    os.system("tar -C / -xzvf system_backup.tar.gz")


restore()
