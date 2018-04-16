### mysql-folders-backup

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

* Create foldername.txt with a folder per line

* Set the path variables db_name and folder_name
 
* Set path variable backup_dir

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
        .../home/aser/dbname.txt...
        .../home/aser/foldername.txt...
        
        =================================== Starting ===================================
        
        -------------------------------- Mysql dump... ---------------------------------
        
        Backup File created: /home/aser/www/backups/db1-2018-04-17.sql.bz2
        
        Backup File created: /home/aser/www/backups/db2-2018-04-17.sql.bz2
        
        ---------------------------- Back up of folders... -----------------------------
        
        Backup File created: /home/aser/www/backups/folder1-2018-04-17.tar.bz2
        
        Backup File created: /home/aser/www/backups/folder2-2018-04-17.tar.bz2
        
        
        dropbox_uploader.sh not found.
        
        ===================================== End ======================================
