import logging
import sys


class WebDrLogger:
    def __init__(self, name):
        self.name = name
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stderr)
        formatter = logging.Formatter('\n%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def info(self, info):
        self.logger.info(info)
