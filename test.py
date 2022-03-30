from easylogging2 import logname

__author__  = "Ali B Othman"
__version__ = "2.1.1"
__date__ = "30 March 2022"
__about__ = "Simple test file for easylogging"

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

print('########### TEST Decorators ###########')

@l.func_set(30)
def test_func(x, y):
	print(x + y + 5)
	l.debug('debug in test_func')
	l.info('info in test_func')
	l.warning('Warning in test_func')
	l.critical('Stopped in test_func!!')
	print(x + y)

test_func(1,2)

print('########### TEST CRITICAL 2 ###########')
l.critical('Stopped !!')
print('########### TEST WARNING ###########')
l.warning('Warning')