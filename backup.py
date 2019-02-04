#!/usr/bin/python3

# https://github.com/asermartinez/mysql-folders-backup
# Version 1.0
# 04-2018

# See README.md for details

import datetime
import glob2
import os
import shlex
import subprocess
import tarfile

# *** CONFIGURE ***
backup_dir = "/home/aser/www/backups"  # Set the destination for backups.
db_name = "/home/aser/dbname.txt"  # Set Full Path to File with databases names, one per line.
folder_name = "/home/aser/foldername.txt"  # Set Full Path to File with folders to backup, one per line.
upload = "yes" # Set to "no" if you do not want to upload to dropbox.
# *** END ***

message_start = " Starting ".center(80, "=")
message_end = " End ".center(80, "=")

backup_dir = os.path.normpath(backup_dir)  # Normalize path, eliminating double slashes, etc.


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
    print("\n" + " Mysql dump... ".center(80, "-"))
    with open(db_name) as databases_list_file:
        db_list = databases_list_file.readlines()
        for db in db_list:
            db = db.rstrip()  # deletes white space or new line character at the end of line
            os.chdir(backup_dir)
            dump_name = db + "-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".sql"
            subprocess.call(shlex.split('mysqldump --databases {} --result-file={}'.format(db, dump_name)))
            subprocess.call(shlex.split('bzip2 -f %s' % dump_name))
            dump_name = dump_name + ".bz2"
            print("\nBackup File created: {}".format(backup_dir + "/" + dump_name))


def backup_folder():
    """
    Make tar file from folders in folder_name file
    Creates tar.bz2 file in backup_dir
    """
    print("\n" + " Back up of folders... ".center(80, '-'))

    with open(folder_name) as directory_list_file:
        folder_list = directory_list_file.readlines()
        for folder in folder_list:
            folder = folder.rstrip()  # deletes white space or new line character at the end of line
            folder = os.path.normpath(folder) # Normalize path, eliminating double slashes, etc.
            os.chdir(backup_dir)
            tar_name = os.path.basename(folder) + "-" + datetime.datetime.now().strftime("%Y-%m-%d") + ".tar.bz2"
            make_tarfile(tar_name, folder)
            print("\nBackup File created: {}".format(backup_dir + "/" + tar_name))


os.system("clear")

if os.path.exists(db_name) and os.path.exists(folder_name):
    print("\n\nDatabases file and Folders file found...")
    print("..." + db_name + "...")
    print("..." + folder_name + "...")
    print("\n" + message_start)
    print("\n")
    subprocess.call("date")
    backup_sql()
    backup_folder()
    os.chdir(backup_dir)
    files = glob2.glob("*-{}".format(datetime.datetime.now().strftime("%Y-%m-%d") + "*.bz2"))
    if upload == "yes":
        try:
            for file in files:
                subprocess.call(shlex.split("dropbox_uploader.sh upload {} /".format(file)))
        except FileNotFoundError:
            print("\n\ndropbox_uploader.sh not found.".center(20, "*"))
    print("\n")
    subprocess.call("date")
    print("\n" + message_end)
else:
    print("\n" + message_start + "\n")
    print("Databases file and Folders file not found.")
    print("Set db_name & folder_name in the script...")
    print("\n" + message_end + "\n")
