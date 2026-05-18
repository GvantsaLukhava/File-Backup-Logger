import datetime
from pathlib import Path
import shutil

class Backup:
    @staticmethod
    def backup(backup_source):
        VERSION="v1.0.0" 
       # backup_source=Path(input("Enter source folder path: "))
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_destination=f'backup_{timestamp}_{VERSION}'

        try:
            if backup_source.exists() and backup_source.is_dir():
                shutil.copytree(backup_source,backup_destination)
            
                log_entry=f"[{timestamp}] SUCCESS! Backed up: {backup_source} As: {backup_destination}\n"
                with open("backup_log.txt","a") as log_file:
                    log_file.write(log_entry) 
            else:
                print("ERROR: THat folder does not exist! ")
                log_entry=f"[{timestamp}] ERROR! Could NOT be Backed up: {backup_source} As: {backup_destination}\n"
                with open("backup_log.txt","a") as log_file:
                    log_file.write(log_entry) 
        except PermissionError:
                log_entry=f"[{timestamp}] Permission denied! Could NOT be Backed up: {backup_source} As: {backup_destination}\n"
                with open("backup_log.txt","a") as log_file:
                    log_file.write(log_entry)
        except Exception as e:
            log_entry=f"[{timestamp}] Error occured! Could NOT be Backed up: {backup_source} As: {backup_destination}\n"
            with open("backup_log.txt","a") as log_file:
                log_file.write(log_entry)
            print(f"Error; {e}")
        
        
        


