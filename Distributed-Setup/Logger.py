import logging
from colorlog import ColoredFormatter,getLogger
#logger = logging.getLogger('__name__')
logger = getLogger()
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

col_formatter = ColoredFormatter(
        "%(cyan)s%(asctime)s %(log_color)s%(levelname)-8s%(reset)s %(blue)s%(message)s",
        datefmt='%I:%M:%S %p',
        reset=True,
        log_colors={
                'DEBUG':    'cyan',
                'INFO':     'green',
                'WARNING':  'yellow',
                'ERROR':    'red',
                'CRITICAL': 'red',
        }
)
ch.setFormatter(col_formatter)

# add ch to logger
logger.addHandler(ch)
logger.addHandler(fh)
