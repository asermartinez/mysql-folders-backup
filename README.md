# mysql-folders-backup

##### https://github.com/asermartinez/mysql-folders-backup
##### Version 1.0
##### 04-2018

:floppy_disk:
 
 Python script to backup multiple mysql databases and folders.
 to use with my drupal / wordpress sites

 Tested with Python 3.6.3

##### Requirements: 
 `pip3 install glob2`

##### Optional: to upload the files to Dropbox:

* Install [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)

##### Configure

* Create dbname.txt with a database name per line

        database1
        database2

* Create foldername.txt with a folder per line

        /home/user/www/folder1
        /home/user/www/folder2

* Set the path variables db_name and folder_name

        db_name = "/home/user/dbname.txt"
        folder_name = "/home/user/foldername.txt" 
 
* Set path variable backup_dir

        backup_dir = "/home/user/www/backups"

* Set upload to "yes" to use the dropbox_uploader.sh

        upload = "yes"

 To avoid passing mysql password to the script, save it in a file in your home folder:

* Create file 
        
        ~/.my.cnf

* Insert:
    
        [mysqldump]

        user=user

        password=pass

Execute:

        chmod +x backup.py
        
        ./backup.py
        
        Databases file and Folders file found...
        .../home/user/dbname.txt...
        .../home/user/foldername.txt...

        =================================== Starting ===================================


        Mon Apr 23 19:41:15 CEST 2018

        -------------------------------- Mysql dump... ---------------------------------

        Backup File created: /home/user/www/backups/database1-2018-04-23.sql.bz2

        Backup File created: /home/user/www/backups/database2-2018-04-23.sql.bz2

        ---------------------------- Back up of folders... -----------------------------

        Backup File created: /home/user/www/backups/folder1-2018-04-23.tar.bz2

        Backup File created: /home/user/www/backups/folder2-2018-04-23.tar.bz2


        dropbox_uploader.sh not found.


        Mon Apr 23 19:41:16 CEST 2018

        ===================================== End ======================================

