import tkinter as tk
from tkinter import filedialog, messagebox
from backup import Backup 
from config_manager import load_config,save_config


def start_gui():
    root=tk.Tk()
    root.title("File-Backup-Logger")
    root.geometry("400x200")
    
    path_var=tk.StringVar()
    zip_var=tk.BooleanVar()
    
    tk.Label(root, text="Select Source folder: ").pack(pady=5)
    
    frame=tk.Frame(root)
    frame.pack(pady=5)
    
    tk.Entry(frame, textvariable=path_var,width=40).pack(side=tk.LEFT)
    tk.Button(frame, text="Browse", command=lambda: path_var.set(filedialog.askdirectory())).pack(side=tk.LEFT)
    
    tk.Checkbutton(root, text="Compress to ZIP", variable=zip_var).pack(pady=10)
    
    config=load_config()
    path_var.set(config.get("last_source",""))
    zip_var.set(config.get("zip_default",False))
    def run_backup():
        path=path_var.get()
        if not path:
            messagebox.showerror("Error","Please select a folder!")
            return
        
        new_config={
        "last_source":path_var.get(),
        "zip_default":zip_var.get()
                    }
        save_config(new_config)
        
        success=Backup.backup(path, zip_it=zip_var.get())
        
        if success:
            messagebox.showinfo("Success", "Backup completed successfully!")
        else:
            messagebox.showerror("Error", "Backup failed! Check the log file for details.")


    tk.Button(root,text="Start backup", command=run_backup).pack(pady=10)
    
    
    root.mainloop()
    
    
if __name__=="__main__":
    start_gui()