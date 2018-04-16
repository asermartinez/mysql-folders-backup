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

#####(Optional) To upload the files to Dropbox:

Install [dropbox_uploader.sh](https://github.com/andreafabrizi/Dropbox-Uploader)

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

