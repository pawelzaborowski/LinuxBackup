#!/usr/bin/python

from archiver import addToArchive


def FullBackUp():
    # backup_dirs = ['/home/pawel/Downloads/ASK-projekt/dbs/mySql/mySqlDb1',
    #              '/home/pawel/Downloads/ASK-projekt/dbs/mySql/mySqlDb2'
    #             '/home/pawel/Downloads/ASK-projekt/dbs/postgreSql/16385',
    #             '/home/pawel/Downloads/ASK-projekt/dbs/postgreSql/16386']

    # repo_bck = ['/home/pawel/Downloads/ASK-projekt/repos/Svn/repSvn1',
    #           '/home/pawel/Downloads/ASK-projekt/repos/Svn/repSvn1']


    backup_dirs = ['/home/pawel/Downloads/ASK-projekt/dbs/mySql']
    repo_bck = ['/home/pawel/Downloads/ASK-projekt/repos/Svn/']

    print('Foldery do zapisania:\n')
    for dir in backup_dirs:
        print(dir)

    for dir in repo_bck:
        print(dir)

    addToArchive('/home/pawel/Documents', repo_bck, 'repositories_backup')

    addToArchive('/home/pawel/Documents', backup_dirs, 'DB_backup')
