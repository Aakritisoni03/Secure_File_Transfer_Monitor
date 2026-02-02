import os
import time
import getpass
import psutil
from hash_utils import calculate_hash
from logger import log_event
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from config import SENSITIVE_DIRECTORIES
from hash_utils import calculate_hash
from logger import log_event, log_alert
file_hashes = {}

def get_active_process():
    try:
        for proc in psutil.process_iter(['pid', 'name']):
            return proc.info['name']
    except Exception:
        return "Unknown"



class MonitorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            self.process("CREATED", event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self.process("DELETED", event.src_path)


    def is_sensitive(self, path):
        return any(path.startswith(d) for d in SENSITIVE_DIRECTORIES)

    def on_created(self, event):
        if not event.is_directory:
            self.process("CREATED", event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            self.process("MODIFIED", event.src_path)
    def on_moved(self, event):
        src = event.src_path
        dest = event.dest_path

        if src.startswith("C:\\SensitiveData") and not dest.startswith("C:\\SensitiveData"):
            self.process("TRANSFERRED OUT", dest)
        else:
            self.process("MOVED", dest)
   
    
    def get_active_process():
        try:
            for proc in psutil.process_iter(['pid', 'name']):
                return proc.info['name']
        except Exception:
            return "Unknown"


    def process(self, action, path):
        print("EVENT DETECTED:", action, path)

        user = getpass.getuser()
        process_name = get_active_process()
        file_hash = calculate_hash(path)

    # ✅ PASS TWO ARGUMENTS
        log_event(
            f"{action} | User: {user} | Process: {process_name} | Hash: {file_hash}",
            path
     )

        if self.is_sensitive(path):
           log_alert(f"Sensitive file {action}: {path}")
           log_alert(f"Hash: {file_hash}")


if __name__ == "__main__":
    path = r"C:\SensitiveData"
    observer = Observer()
    observer.schedule(MonitorHandler(), path, recursive=True)
    observer.start()

    print("Monitoring started... Press CTRL+C to stop")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
