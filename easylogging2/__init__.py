import logging
import sys, os
from configparser import ConfigParser
from time import strftime, gmtime

__author__  = "Ali B Othman"
__version__ = "2.1.1"
__date__ = "30 March 2022"
__about__ = "Simple logging library for python3"

class logname:
    def __init__(self, name=__file__):
        self.__name = name
        self.__lname = name.split("\\")[-1]
        self.__Dir = os.path.join(os.path.dirname(os.path.abspath(self.__name)), 'logs')
        self.__logFile = 'Log %s.log' % (strftime("%Y-%m-%d %Hh-%Mm-%Ss", gmtime()))
        self.__Dirfilelog = os.path.join(self.__Dir, self.__logFile)
        self.__logger = logging.getLogger(__name__)
        self.__logger_file = logging.getLogger(__name__+' ')
        self.__FileStart = True
        self.Setup_configuration()
        self.run()

    def Setup_configuration(self):
        self.config = ConfigParser(allow_no_value=True)
        self.config1 = ConfigParser(allow_no_value=True)
        self.config.optionxform = str
        self.config1.read('logging.conf')
        if not os.path.exists('logging.conf') or not self.config1.has_section(self.getname()) :
            self.config.add_section(self.getname())

            self.config.set(self.getname(), '''\n;.......................................
;Change number to enable logger in console *(0, 10, 20, 30, 40, 50, 60)* without --logging
;This option will enable console log without --logging\n''')
            self.config.set(self.getname(), 'level', '60')

            self.config.set(self.getname(), '''\n;.......................................
;Change number to set *log level (0, 10, 20, 30, 40, 50, 60)* with --logfile (Level for log file)\n''')
            self.config.set(self.getname(), 'file_level', '0')

            self.config.set(self.getname(), '''\n;.......................................
;Show Error info (easylogging.error(msg, exc_info))
;True or False or None,
; * (None) means that exc_info takes the value entered from the user, example: easylogging.error(msg, exc_info=True)\n''')
            self.config.set(self.getname(), 'exc_info', 'None')

            self.config.set(self.getname(), '''\n;.......................................
;Log Formatter
;You can use all defaults logging formats\n''')
            self.config.set(self.getname(), 'formatter', '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            self.config.set(self.getname(), '''\n;#######################################''')

            with open("logging.conf","a+") as configfile:
                self.config.write(configfile)
        self.config.read('logging.conf')
        self.prop = self.config.get(self.getname(), 'file_level')
        self.prop = int(self.prop)

        self.level = self.config.get(self.getname(), 'level')
        self.level=int(self.level)

        self.exc = self.config.get(self.getname(), 'exc_info')
        try:
            if os.path.exists('logging.conf'): 
                self.formated = self.config.get(self.getname(), 'formatter', raw=True)
            else:
                self.formated = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        except:
            self.formated = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        logging.basicConfig(level = logging.DEBUG, format=self.formated)
        try:
            if '--logfile' in sys.argv:
                if not os.path.exists('logs'):
                    os.makedirs('logs')
                handler = logging.FileHandler(self.__Dirfilelog)
                handler.setLevel(logging.DEBUG)
                formatter = logging.Formatter(self.formated)
                handler.setFormatter(formatter)
                if self.__FileStart:
                    self.__logger_file.addHandler(handler)
                    self.__FileStart = False
            else:
                self.__logger_file.setLevel(60)
        except:
            print('Error..')
        self.__logger_file.propagate = False
###################################################################
    def warning(self, msg):
        self.__logger.warning(self.getname()+' : '+ str(msg))
        if '--logfile' in sys.argv:
            self.__logger_file.warning(self.getname()+' : '+ str(msg))
    def debug(self, msg):
        self.__logger.debug(self.getname()+' : '+ str(msg))
        if '--logfile' in sys.argv:
            self.__logger_file.debug(self.getname()+' : '+ str(msg))

    def info(self, msg, *args, **kwargs):
        self.__logger.info(self.getname()+' : '+ str(msg), *args, **kwargs)
        if '--logfile' in sys.argv:
            self.__logger_file.info(self.getname()+' : '+ str(msg), *args, **kwargs)

    def critical(self, msg):
        self.__logger.critical(self.getname()+' : '+ str(msg))
        if '--logfile' in sys.argv:
            self.__logger_file.critical(self.getname()+' : '+ str(msg))
    def error(self, msg, exc_info = False):
        if self.exc == 'True':
            self.__logger.error(self.getname()+' : '+ str(msg), exc_info = True)
            if '--logfile' in sys.argv:
                self.__logger_file.error(self.getname()+' : '+ str(msg), exc_info = True)
        elif self.exc == 'False':
            self.__logger.error(self.getname()+' : '+ str(msg), exc_info = False)
            if '--logfile' in sys.argv:
                self.__logger_file.error(self.getname()+' : '+ str(msg), exc_info = False)
        else:
            self.__logger.error(self.getname()+' : '+ str(msg), exc_info = exc_info)
            if '--logfile' in sys.argv:
                self.__logger_file.error(self.getname()+' : '+ str(msg), exc_info = exc_info)


###################################################################
    def getname(self):
        return self.__lname
###################################################################
    def run(self):
        try:
            if '--logfile' not in sys.argv:
                self.__logger_file.setLevel(60)
            else:
                self.__logger_file.setLevel(self.prop)

            if '--logging' in sys.argv:
                self.__logger.setLevel(logging.DEBUG)
            else:
                self.__logger.setLevel(self.level)
        except:
            print('Error...')

    def func_set(self, level):
        if '--logfile' in sys.argv:
            self.__logger_file.setLevel(level)
        self.__logger.setLevel(level)
        def Inner(func):
            def wrapper(*args, **kwargs):
                func(*args, **kwargs)
                self.run()
            return wrapper
        return Inner