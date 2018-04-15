# mysql-folders-backup

Python script to backup multiple mysql databases and folders.
to use with my drupal / wordpress sites

Tested with Python 3.6.3

Requirement: Glob2

pip3 install glob2

Create dbnames.txt with a database name per line.

Create foldernames.txt with a folder per line.

Set the path variables DB_NAME and FOLDER_NAME.

To avoid passing mysql password to the script, save it in a file in your home folder:

~/.my.cnf

[mysqldump]

user=user

password=pass

Uploads files to Dropbox with dropbox_uploader.sh :
https://github.com/andreafabrizi/Dropbox-Uploader

Scripts for reference:
bash script https://tecadmin.net/python-script-for-mysql-database-backup/
python script http://www.guyrutenberg.com/2010/02/28/improved-ftp-backup-for-wordpress/