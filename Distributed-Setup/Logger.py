import logging
logger = logging.getLogger('__name__'
                           '')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.WARN)

# create a file handler
fh = logging.FileHandler('program.log')
fh.setLevel(logging.INFO)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s',datefmt='%m/%d/%Y %I:%M:%S %p')

# add formatter to ch
ch.setFormatter(formatter)
fh.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)