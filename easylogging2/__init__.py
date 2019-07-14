# Created By : Ali B Othman
# V 2.0.1
# Simple logging lib for python

import logging
import sys, os
from configparser import ConfigParser
from time import strftime, gmtime

class logname:
    def __init__(self, name=__file__, formatt = None):
        self.name = name
        self.formatt = formatt
        self.lname = name.split("\\")[-1]
        self.Dir = os.path.join(os.path.dirname(os.path.abspath(self.name)), 'logs')
        self.logFile = 'Log %s.log' % (strftime("%Y-%m-%d %Hh-%Mm-%Ss", gmtime()))
        self.Dirfilelog = os.path.join(self.Dir, self.logFile)
        self.logger = logging.getLogger(__name__)
        self.FileStart = True
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
;Change number to enable *log level (0, 10, 20, 30, 40, 50)* without --logging or --logfile
;This option will enable console log without --logging\n''')
            self.config.set(self.getname(), 'level', '50')

            self.config.set(self.getname(), '''\n;.......................................
;Change number to set *log level (0, 10, 20, 30, 40, 50)* with --logfile (Level for log file)
;This option work on --logfile without use --logging (if use --logging file write all level)\n''')
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
###################################################################
    def warning(self, msg):
        self.logger.warning(self.getname()+' : '+ str(msg))
    def debug(self, msg):
        self.logger.debug(self.getname()+' : '+ str(msg))
    def info(self, msg, *args, **kwargs):
        self.logger.info(self.getname()+' : '+ str(msg), *args, **kwargs)
    def critical(self, msg):
        self.logger.critical(self.getname()+' : '+ str(msg))
    def error(self, msg, exc_info = False):
        if self.exc == 'True':
            self.logger.error(self.getname()+' : '+ str(msg), exc_info = True)
        elif self.exc == 'False':
            self.logger.error(self.getname()+' : '+ str(msg), exc_info = False)
        else:
            self.logger.error(self.getname()+' : '+ str(msg), exc_info = exc_info)


###################################################################
    def getname(self):
        return self.lname
###################################################################
    def run(self):
        logging.disable(self.level)
        if self.level < 50:
            self.logger.propagate = True
        else:
            self.logger.propagate = False

        try:
            if '--logfile' in sys.argv:
                if not os.path.exists('logs'):
                    os.makedirs('logs')
                handler = logging.FileHandler(self.Dirfilelog)
                handler.setLevel(logging.DEBUG)
                formatter = logging.Formatter(self.formated)
                handler.setFormatter(formatter)
                if self.FileStart:
                    self.logger.addHandler(handler)
                    self.FileStart = False
                logging.disable(self.prop)


        except:
            print('Error...')

        try:
            if '--logging' in sys.argv:
                logging.disable(0)
                self.logger.propagate = True
        except:
            print('Error...')

