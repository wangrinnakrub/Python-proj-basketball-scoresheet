from watchdog.observers.polling import PollingObserver
from watchdog.events import FileSystemEventHandler
import subprocess
import os
import time

import threading
import subprocess

class FileChangeHandler(FileSystemEventHandler):
    process = None

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"{event.src_path} ถูกแก้ไข, รันโปรแกรมใหม่...")

            if self.process:
                self.process.terminate()
                self.process.wait()

            self.process = subprocess.Popen(["python", event.src_path])

if __name__ == "__main__":
    path = os.getcwd()
    event_handler = FileChangeHandler()
    observer = PollingObserver()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        print("waiting for file edit...")
        while True:
            time.sleep(0)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
