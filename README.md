# easylogging2
###### Simple and Easy Logging lib for python3

[![easylogging2](https://img.shields.io/badge/build-passing-brightgreen.svg)]()
[![version](https://img.shields.io/badge/version-2.1.1-green.svg)]()
[![status](https://img.shields.io/badge/status-unstable-green.svg)]()
[![python](https://img.shields.io/badge/python-3-blue.svg)](http://www.python.org/download/)
[![windows](https://img.shields.io/badge/windows-tested-brightgreen.svg)]()
[![linux](https://img.shields.io/badge/linux-tested-brightgreen.svg)]()
[![license](https://img.shields.io/badge/license-GNU-blue.svg)](https://github.com/AI35/easylogging2/blob/master/LICENSE)

## REQUIREMENTS
- Python-3 --> http://www.python.org/download/

## Notes
- After 9 months this library has returned better and more useful.
- This library is very simple so it is not better than a logging library and it is derived from it.
- This library was created because I wanted a simple and easy logging library.

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
  - Change **level** number to display log in console (0 display all level).
  	```
  	  level=60
  	```
  - Change **file_level** number to set level in log file **with** --logfile (60 hide all level).
  	###### - This option work on --logfile
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
	
 - You can run the **test.py** file to see how it works.
 - You can use all logging functions from this lib (ex: easylogging.logging.**function**)
 
 - **formatter** :
    ###### - You can use all defaults logging formats.
  	```
	  formatter = %(asctime)s - %(name)s - %(levelname)s - %(message)s
	```
	###### - From logging formatter function :
	```
    Formatter instances are used to convert a LogRecord to text.
    Formatters need to know how a LogRecord is constructed. They are
    responsible for converting a LogRecord to (usually) a string which can
    be interpreted by either a human or an external system. The base Formatter
    allows a formatting string to be specified. If none is supplied, the
    the style-dependent default value, "%(message)s", "{message}", or
    "${message}", is used.
    The Formatter can be initialized with a format string which makes use of
    knowledge of the LogRecord attributes - e.g. the default value mentioned
    above makes use of the fact that the user's message and arguments are pre-
    formatted into a LogRecord's message attribute. Currently, the useful
    attributes in a LogRecord are described by:
    %(name)s            Name of the logger (logging channel)
    %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                        WARNING, ERROR, CRITICAL)
    %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                        "WARNING", "ERROR", "CRITICAL")
    %(pathname)s        Full pathname of the source file where the logging
                        call was issued (if available)
    %(filename)s        Filename portion of pathname
    %(module)s          Module (name portion of filename)
    %(lineno)d          Source line number where the logging call was issued
                        (if available)
    %(funcName)s        Function name
    %(created)f         Time when the LogRecord was created (time.time()
                        return value)
    %(asctime)s         Textual time when the LogRecord was created
    %(msecs)d           Millisecond portion of the creation time
    %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                        relative to the time the logging module was loaded
                        (typically at application startup time)
    %(thread)d          Thread ID (if available)
    %(threadName)s      Thread name (if available)
    %(process)d         Process ID (if available)
    %(message)s         The result of record.getMessage(), computed just as
                        the record is emitted
	```
## Changlog
### V 2.1.1
###### - Add Decorator @func_set(level).
	
	  Use @Yourlog.func_set(level) to set logger and handler level to function and ignore all level config in function.
	
##### - Fix Bug handler write all level and ignore file_level when using --logging with --logfile

### V 2.0.5 Some fixes:
###### - Make some variables private.

### V 2.0.1 Performance:
###### - Increase performance.

##
 - Level table :

    | Level  | Numeric value |
    | ------------- | ------------- |
    | CRITICAL  |  50  |
    | ERROR  |  40  |
    | WARNING  |  30  |
    | INFO  |  20  |
    | DEBUG  |  10  |
    | NOTSET  | 0  |
   


  
## LICENSE
```
Copyright 2019 ALI B OTHMAN(AI35), Inc.

easylogging2

   Licensed under the GNU License , you may not use this
   file except in compliance with the License.
   You may obtain a copy of the License at :

   https://github.com/AI35/easylogging2/blob/master/LICENSE
```
###### ALI .B .OTH - ORG : LinePY  
