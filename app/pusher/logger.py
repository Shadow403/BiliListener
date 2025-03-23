import logging
from blivedm.log import logger

class InterceptHandler(logging.Handler):
    def emit(self, record):
        # Retrieve context where the logging call occurred, this happens to be in the 6th frame upward
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelno, record.getMessage())

logger_name_list = [name for name in logging.root.manager.loggerDict]
# logger_name_list = [name for name in logging.root.manager.loggerDict if '.' not in name]

for logger_name in logger_name_list:
    logging.getLogger(logger_name).setLevel(10)
    logging.getLogger(logger_name).handlers = []
    if '.' not in logger_name:
        logging.getLogger(logger_name).addHandler(InterceptHandler())
