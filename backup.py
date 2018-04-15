#!/usr/bin/python3

# Python script to backup multiple mysql databases and folders.
# to use with my drupal / wordpress sites
# Tested with Python 3.6.3
# Requirement: Glob2
#   pip3 install glob2

# Create dbnames.txt with a database name per line
# Create foldernames.txt with a folder per line
# Set the path variables DB_NAME and FOLDER_NAME

# To avoid passing mysql password to the script, save it in a file in your home folder:
# ~/.my.cnf
# [mysqldump]
# user=user
# password=pass

# Uploads files to Dropbox with dropbox_uploader.sh :
# https://github.com/andreafabrizi/Dropbox-Uploader

# Scripts for reference:
# bash script https://tecadmin.net/python-script-for-mysql-database-backup/
# python script http://www.guyrutenberg.com/2010/02/28/improved-ftp-backup-for-wordpress/


import os
import shlex
import subprocess
import datetime
import tarfile
import shutil
import glob2

message_start = " Starting ".center(80, '=')
message_end = " End ".center(80, '=')

backup_dir = "/home/aser/www/backups"

db_name = '/home/aser/dbname.txt'  # file with databases names, one per line.
folder_name = '/home/aser/foldername.txt'  # file with folders to backup, one per line.


def make_tarfile(output_filename, source_dir):
    """
    Using tarfile to backup folders
    """
    with tarfile.open(output_filename, "w:bz2") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))


def backup_sql():
    """
    Make mysql dump of databases in db_name file
    Creates .sql.bz2 file in backup_dir
    """
    print("\n" + " Mysql dump... ".center(80, '-'))
    with open(db_name) as databases_list_file:
        file_length = len(databases_list_file.readlines())

    counter = 1

    with open(db_name) as databases_list_file:
        while counter <= file_length:
            dbname = databases_list_file.readline()
            db = dbname.rstrip() # deletes white space or new line character at the end of line
            os.chdir(backup_dir)
            dump_name = db + "-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".sql"
            subprocess.call(shlex.split('mysqldump --databases {} --result-file={}'.format(db, dump_name)))
            subprocess.call(shlex.split('bzip2 -f %s' % dump_name))
            dump_name = dump_name + ".bz2"
            shutil.move(os.path.join(backup_dir, dump_name), os.path.join(backup_dir, dump_name))
            print("\nBackup File created: {}".format(backup_dir + "/" + dump_name))
            counter = counter + 1


def backup_folder():
    """
    Make tar file from folders in folder_name file
    Creates tar.bz2 file in backup_dir
    """
    print("\n" + " Back up of folders... ".center(80, '-'))
    with open(folder_name) as directory_list_file:
        file_length = len(directory_list_file.readlines())

    counter = 1

    with open(folder_name) as directory_list_file:
        while counter <= file_length:
            foldername = directory_list_file.readline()
            folder = foldername.rstrip('\n') # deletes white space or new line character at the end of line
            os.chdir(folder)
            tar_name = os.path.basename(folder) + "-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".tar.bz2"
            make_tarfile(tar_name, folder)
            shutil.move(os.path.join(folder, tar_name), os.path.join(backup_dir, tar_name))
            print("\nBackup File created: {}".format(backup_dir + "/" + tar_name))
            counter = counter + 1


os.system("clear")

if os.path.exists(db_name) and os.path.exists(folder_name):
    print("\n\nDatabases file and Folders file found...")
    print("..." + db_name + "...")
    print("..." + folder_name + "...")
    print("\n" + message_start)
    backup_sql()
    backup_folder()
    os.chdir(backup_dir)
    files = glob2.glob("*-{}".format(datetime.datetime.now().strftime("%Y-%m-%d") + "*.bz2"))
    for file in files:
        subprocess.call(shlex.split("dropbox_uploader.sh upload {} /".format(file)))
    print("\n" + message_end)
else:
    print("\n" + message_start + "\n")
    print("Databases file and Folders file not found.")
    print("Set db_name & folder_name in the script...")
    print("\n" + message_end + "\n")