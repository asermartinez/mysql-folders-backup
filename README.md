### mysql-folders-backup

##### https://github.com/asermartinez/mysql-folders-backup
##### Version 1.0
##### 04-2018

 Python script to backup multiple mysql databases and folders.
 to use with my drupal / wordpress sites

 Tested with Python 3.6.3

##### Requirements: 
 Glob2 => pip3 install glob2

######(Optional) To upload the files to Dropbox:
 
 install dropbox_uploader.sh from:

 https://github.com/andreafabrizi/Dropbox-Uploader

##### Configure

 Create dbname.txt with a database name per line

 Create foldername.txt with a folder per line

 Set the path variables db_name and folder_name

 To avoid passing mysql password to the script, save it in a file in your home folder:

 ~/.my.cnf

 [mysqldump]

 user=user

 password=pass

##### Scripts for reference:

 bash 
 https://tecadmin.net/python-script-for-mysql-database-backup/

 python http://www.guyrutenberg.com/2010/02/28/improved-ftp-backup-for-wordpress/
