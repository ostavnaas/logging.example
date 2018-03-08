import logging
import logging.handlers


class log:
    def __init__(self):
        formt = '%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
        formatter = logging.Formatter(formt)

        ch = logging.StreamHandler()
        ch.setLevel(logging.ERROR)
        ch.setFormatter(formatter)

        fh = logging.handlers.RotatingFileHandler('./my_app.log')
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)

        logger = logging.getLogger('app_name')
        # This must be lower than other handlers, otherwise it will cut of the
        # handlers
        logger.setLevel(logging.INFO)
        logger.addHandler(ch)
        logger.addHandler(fh)
