import datetime
from pathlib import Path
import shutil
import time
class Backup:
    
    @staticmethod
    def backup(backup_source, zip_it=False):
        start_time=time.time()
        VERSION="v1.0.0" 
        backup_source=Path(backup_source)
        print(f"DEBUG: Checking path: {backup_source.absolute()}") # Add this!
       # backup_source=Path(input("Enter source folder path: "))
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_destination=f'backup_{timestamp}_{VERSION}'
        
        try:
                if backup_source.exists() and backup_source.is_dir():
                    if zip_it==True:
                        zip_name=f'zip_{timestamp}_{VERSION}'
                        shutil.make_archive(zip_name,format='zip',root_dir=str(backup_source))
                        actual_destination=f"{zip_name}.zip"
                    else: 
                        shutil.copytree(backup_source,backup_destination)
                        actual_destination=backup_destination
                    
                    duration=time.time()-start_time
                    log_entry=f"[{timestamp}] SUCCESS!File count:{file_count} Source: {backup_source} Destination: {actual_destination} Duration: {duration:.2f} seconds \n"
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
        
        
        


