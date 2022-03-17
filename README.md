# py-sourceforge-file-hasher

## 1. Dependencies
* Windows OS
* 7-Zip installed in default directory
* Python3 (developed w/ version 3.10.2, other versions not tested)

## 2. Setup
* ```pip install -r requirements.txt```

## 2. Purpose of demo
Purpose of demo is to show a process steps (in Windows OS):
1. Scrape Sourceforge top 100 software links
2. Filter Windows PE files and download in current dir
3. Rename files after SHA-1 hashes
4. Compress files with 7-Zip (via GUI automation)

* Run command for demo: ```python ./main.py```  

## 3. Potential demo improvement list
* Optimize/refactor process
* Improve 7-Zip GUI handling, application cleanup/close down
* Exception handling
* Include archive behaviour if WinRAR is install instead of 7Z
* Move archived folder to another location and cleanup after
* Additional archiving settings (filetype, compression, directory)
* Create temp cache logs for previously downloaded files to avoid duplicates
* Add other criteria from release filtering
* Async file downloads
* SFScraper module as commandline tool
* SFScraper get projects by count, not by pages