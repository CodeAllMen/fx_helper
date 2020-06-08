"""
Create by yy on 2020/3/10
"""
import logging

__all__ = ["Log"]

from tool_yy import debug


class Log(object):
    def __init__(self, file_name, is_debug):
        self.debug = is_debug
        logging.basicConfig(filename=file_name, level=logging.INFO,
                            format="%(asctime)s %(levelname)s: %(message)s",
                            datefmt='%Y-%m-%d %H:%M:%S %a')

    def error(self, msg, *args):
        if self.debug:
            debug(msg)
        logging.error(msg, *args)

    def info(self, msg, *args):
        if self.debug:
            debug(msg)
        logging.info(msg, *args)

    def warning(self, msg, *args):
        if self.debug:
            debug(msg)
        logging.warning(msg, *args)

    def warn(self, msg, *args):
        if self.debug:
            debug(msg)
        logging.warn(msg, *args)
