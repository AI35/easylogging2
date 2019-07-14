# easylogging2
###### Simple and Easy Logging lib for python V2

[![easylogging2](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![version](https://img.shields.io/badge/version-2.0.1-green.svg)]()
[![status](https://img.shields.io/badge/status-stable-brightgreen.svg)]()
[![python](https://img.shields.io/badge/python-3-blue.svg)](http://www.python.org/download/)
[![windows](https://img.shields.io/badge/windows-tested-brightgreen.svg)]()
[![linux](https://img.shields.io/badge/linux-tested-brightgreen.svg)]()
[![license](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/AI35/easylogging2/blob/master/LICENSE)

## REQUIREMENTS
- Python-3 --> http://www.python.org/download/

## Notes
- After 9 months this library has returned better and more useful.
- This library is very simple so it is not better than a logging library and it is derived from it.
- This library is created because I wanted a simple and easy logging library.

## Installation

- Clone this repo:
	
	```
	$ git clone https://github.com/AI35/easylogging2
	```
- Using pip:
	
	```
	$ pip install easylogging2
	```

## Usage
- First you need import lib and Set name :
  ```
    import easylogging2
    
    log = easylogging2.logname(__file__)
  ```
- Use the functions you need:
  - log.critical(msg)
  - log.error(msg, exc_info) **default: exc_info=False**
  - log.warning(msg)
  - log.info(msg)
  - log.debug(msg)
- You can start logging from Cmd or PowerShell :
  ```
    $ Python yourfile.py --logging --logfile
    
    usage: youefile.py [--logging] [--logfile]
    
    optional arguments:
      --logging            Display log in Console
      --logfile            Create log file
  ```
- After first run you will see new file **logging.conf** :
  - Change **level** number to display log in console **without** --logging (0 display all level).
  	```
  	  level=50
  	```
  - Change **file_level** number to set level in log file **with** --logfile (50 hide all level).
  	###### - This option work on --logfile without use --logging (if use --logging file write all level)
  	```
   	  file_level=0
  	```
 - Show and hide error info from **logging.conf** :
  	###### - Show Error info (easylogging.error(msg, exc_info))
	###### - True or False or None
	###### - * (None) means that exc_info takes the value entered from the user, example: easylogging.error(msg, exc_info=True)
  	```
  	  exc_info=None
  	```
 - **formatter** :
    ###### - You can use all defaults logging formats.
  	```
	  formatter = %(asctime)s - %(name)s - %(levelname)s - %(message)s
	```
## Changlog
### V 2.0.1 Bug fix:
###### - Increase performance


## - Level table :

    | Level  | Numeric value |
    | ------------- | ------------- |
    | CRITICAL  | < 50  |
    | ERROR  | < 40  |
    | WARNING  | < 30  |
    | INFO  | < 20  |
    | DEBUG  | < 10  |
    | NOTSET  | 0  |
    
- You can see test file **test.py** to know how this lib is work.


  
## LICENSE
```
Copyright 2019 LinePY - ALI B OTHMAN(AI35), Inc.

easylogging2

   Licensed under the GNU License , you may not use this
   file except in compliance with the License.
   You may obtain a copy of the License at :

   https://github.com/AI35/easylogging2/blob/master/LICENSE
```
###### ALI .B .OTH - ORG : LinePY  
