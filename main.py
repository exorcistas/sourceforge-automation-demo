"""
+ 1. Scrape Sourceforge top 100 software links
+ 2. Filter Windows PE files and download
+ 3. Rename files after SHA-1 hashes
+ 4. Compress 7z/WinRAR files (via GUI automation)
"""
import SFScraper.sf as sforge
from datetime import datetime
import os
from os import listdir
from os.path import isfile, join
import wget
import hashlib
import psutil
from pywinauto.application import Application
from pywinauto import keyboard
import time

def _getTimestamp():
    timestamp = str(datetime.now())
    timestamp = (timestamp.replace(':', '').replace('-', '').replace('.', '').replace(' ', ''))
    return timestamp

def createTempFolder():
    timestamp = _getTimestamp()
    save_dir = os.path.join(os.getcwd(), timestamp)
    os.mkdir(save_dir)
    return save_dir, timestamp

def getProjectLinks(sf, max_pages):
    urls = []
    for pagenum in range(1, max_pages): # each page shows 25 projects
        urls += sf.getPopularProjectsByPage(pagenum)
    if not urls:
        raise("No project links found!")
    
    print(f"Found top {len(urls)} projects in SourceForge")
    return urls

def dowloadReleases(sf, urls, file_type, dir):
    for url in urls:
        rel = sf.getProjectBestReleases(url)
        try:
            if (rel['platform_releases']['windows']['file_type'] == file_type):
                download_url = rel['platform_releases']['windows']['url']
                md5sum = rel['platform_releases']['windows']['md5sum']

                print(f"[DOWNLOADING] {download_url}")
                wget.download(download_url, os.path.join(dir, md5sum))
                print("")
        except:
                print(f"[EXCEPTION] Releases not found in: {url}")

def renameFilesToSHA1(dir):
    files = [f for f in listdir(dir) if isfile(join(dir, f))]
    for file in files:
        file_path = os.path.join(dir, file)
        file_sha1 = _getFileSHA1(file_path)
        os.rename(file_path, os.path.join(dir, file_sha1))

def _getFileSHA1(filename):
   h = hashlib.sha1()
   with open(filename,'rb') as file:    # open file for reading in binary mode
       chunk = 0
       while chunk != b'':              # loop EOF
           chunk = file.read(1024)      # read only 1024 bytes at a time
           h.update(chunk)
   return h.hexdigest()                 # return the hex representation of digest

def connectArchiverApp():
    process = [proc for proc in psutil.process_iter() if proc.name() == "7zFM.exe"]
    if process:
        app = Application().connect(process=process[0].pid)
    else:
        app = Application().start('C:\\Program Files\\7-Zip\\7zFM.exe', timeout=3)
    return app

def addDirToArchive(app, save_dir):
    main_window = app.top_window()
    main_window['Edit'].click()
    main_window['Edit'].type_keys('{DEL}')
    main_window['Edit'].type_keys(save_dir)
    main_window['Edit'].type_keys('{ENTER}')
    keyboard.send_keys('^a')
    main_window['ToolbarAdd'].click()
    time.sleep(1)
    process = [proc for proc in psutil.process_iter() if proc.name() == "7zG.exe"]
    if not process:
        raise("Add to Archive dialog did not appear")
    arch_window = Application().connect(process=process[0].pid)
    dialog = arch_window.top_window()
    dialog['OK'].click()
    
    while True:
        process = [proc for proc in psutil.process_iter() if proc.name() == "7zG.exe"]
        if process:
            time.sleep(1)
        else:
            break
    

if __name__ == "__main__":
    save_dir, timestamp = createTempFolder()
    sf = sforge.SFScraper()
    urls = getProjectLinks(sf, 5)

    print("Filtering Windows PE32 executables from projects...")
    dowloadReleases(sf, urls, "PE32 executable", save_dir)
    
    print("Renaming files to SHA-1...")
    renameFilesToSHA1(save_dir)
            
    print("Archiving files...")
    app = connectArchiverApp()
    addDirToArchive(app, save_dir)
    print("Done!")