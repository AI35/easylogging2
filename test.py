# Created By : Ali B Othman
# Test V 2.0.1
# Simple Test File

from easylogging2 import logname

########## very important ############
l = logname(__file__)
######################################
print('########### TEST DEBUG ###########')
l.debug('logs debug done')
print('########### TEST INFO ###########')
l.info('Start log')
print('########### TEST WARNING ###########')
l.warning('Warning')
print('########### TEST CRITICAL ###########')
l.critical('Stopped !!')
print('########### TEST INPUT int ###########')
l.info(1)
print('########### TEST INPUT float ###########')
l.debug(3.4)

print('########### TEST ERROR 1 ###########')
try:
	Test_Error
except Exception :
	l.error('**Error : exc_info = True**', exc_info = True)

print('########### TEST ERROR 2 ###########')
try:
	Test_Error
except Exception :
	l.error('**Error : exc_info = False**', exc_info = False)
