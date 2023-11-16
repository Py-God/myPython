import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Some debugging details')
 2022-06-19 04:21:52,658 - DEBUG - Some debugging details
logging.info('The logging module is working.')
 2022-06-19 04:22:24,820 - INFO - The logging module is working.
logging.warning('An error message is about to be logged')
 2022-06-19 04:22:52,359 - WARNING - An error message is about to be logged
logging.error('An error has occured')
 2022-06-19 04:23:10,156 - ERROR - An error has occured
logging.critical('The program is unable to recover!')
 2022-06-19 04:23:38,463 - CRITICAL - The program is unable to recover!
