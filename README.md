# py-sourceforge-demo

## Purpose
Purpose of demo is to show an automated process steps (in Windows OS):
1. Scrape Sourceforge top 100 software links
2. Filter Windows PE files and download in current dir
3. Rename files after SHA-1 hashes
4. Compress files with 7-Zip (via GUI automation)


## 0. Dependencies
* Windows OS
* 7-Zip installed in default directory
* Python3 (developed w/ version 3.10.2, other versions not tested)

## 1. Setup & execute
0. Pull dependencies (from private repo):
```git submodule update --init --recursive```
* In case updated branch required: ```git submodule update --remote --merge```

1. Install: 
```
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
pip install sourceforge-scraper/
```
2. Run command for demo: ```python ./demo.py```  

## 2. Potential demo improvement list
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
