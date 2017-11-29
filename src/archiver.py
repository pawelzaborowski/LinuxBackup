#!/usr/bin/python
import tarfile
import datetime


def addToArchive(source, dest, name):
    time = datetime.datetime.now().strftime('%d%m%Y_%H:%M')
    with tarfile.open(dest + '/' + name + time + '.tar.gz', mode='w:gz') as archive:
        archive.add(source, recursive=True)
