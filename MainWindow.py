#!/usr/bin/python


import sys, os, shutil

import gzip
import tarfile
import glob
import time
import datetime
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

__author__ = 'Hubert Kozij & Pawel Zaborowski'
__version__ = '1.0'


# backup_dirs = ["/etc", "/usr/local", "/var/lib"]

class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.left = 20
        self.top = 20
        self.width = 400
        self.height = 300
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Backup')
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()


    def chceckIfDirExist(os_dir):
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


    # rsync("-auhv", "/home/pawel/Documents/untitled", "/home/pawel/Documents")

    def compressionGZIP(self, source, target):
        try:
            with gzip.open(target + '.gz' + 'wb') as target_file:
                with open(source, 'rb') as source_file:
                    target_file.writelines(source_file)
            print('Compress {}'.format(source))
        except FileNotFoundError:
            os.makedirs(os.path.dirname(target))
            self.compressionGZIP(source, target)

    def addToArchive(self, dest, backup_dirs, name=''):
        time = datetime.datetime.now().strftime('%d%m%Y %H:%M')
        with tarfile.open(dest + '/' + 'backup-' + time + '.tar.gz', mode='w|gz') as archive:
            for dir in backup_dirs:
                archive.add(dir, recursive=True)

    def restore(self):
        pass

    def test(self):
        content = "Lots of content here"
        f = gzip.open('/home/joe/file.txt.gz', 'wb')
        f.write(content)
        f.close()

        f_in = open('/home/joe/file.txt')
        f_out = gzip.open('/home/joe/file.txt.gz', 'wb')
        f_out.writelines(f_in)
        f_out.close()
        f_in.close()

        os.chdir('/home')

        for root, dirs, files in os.walk("/home/pawel/Documents/"):
            for file in files:
                gzip.write32u(os.path.join(root, file))

        # wypakuj tar.gz do obecnej lokalizacji
        tar = tarfile.open("sample.tar.gz")
        tar.extractall()
        tar.close()

        # informacje o gzip
        tar = tarfile.open("sample.tar.gz", "r:gz")
        for tarinfo in tar:
            print(tarinfo.name, "is", tarinfo.size, "bytes in size and is"),
            if tarinfo.isreg():
                print("a regular file.")
            elif tarinfo.isdir():
                print("a directory.")
            else:
                print("something else.")
        tar.close()

        # utworz tar
        tar = tarfile.open("sample.tar", "w")
        for name in glob.iglob('home/pawel/Documents'):  # dac directory
            tar.add(name)
        tar.close()

        # kompres gzip
        with open('home/pawel/Documents.tar', 'rb') as f_in:
            with gzip.open('ome/pawel/Documents.tar.gz', 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)

                # https://www.ibm.com/developerworks/library/l-config/index.html
                # http://www.comptechdoc.org/os/linux/commands/linux_crspfiles.html


if __name__ == "__main__":

    app = QApplication(sys.argv)
    mainW = MainWindow()

    backup_dirs = ["/home/pawel/Documents/jade", "/home/pawel/Documents/jade", "/home/pawel/Documents/untitled"]

    print('Foldery do zapisania:\n')
    for dir in backup_dirs:
        print(dir)

    if mainW.confirm() == 0:
        mainW.addToArchive('/home/pawel/Documents', backup_dirs)
    elif mainW.confirm() == 1:
        exit(1)
