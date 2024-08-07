# -*- coding: utf-8 -*-

"""
    Python log functions
    
"""

import logging

log_level = logging.DEBUG


def configure_logging(log: logging, file_name: str, log_format: str, logger_name: str) -> logging.Logger:
    """
    Utility function for setting up the logger. This will return a uniform logger across different scripts.
    :param log: pass the imported log module into this function to control the scope
    :param file_name: name of the log file to write out to
    :param log_format: log file output format string
    :param logger_name: name of the process writing to the log file (helps when multiple scripts write to the same file)
    :return: logger object
    """
    # Set the output log file
    log_path_and_file: str = f'{file_name}'

    # create logger object
    logger = log.getLogger(logger_name)

    # set the log level
    logger.setLevel(log_level)

    # create formatter object
    formatter = log.Formatter(log_format)

    # create file handler object, format it with formatter, and attach to logger
    fh = log.FileHandler(log_path_and_file)

    # set level again?
    fh.setLevel(log_level)

    # set the formatting for the log file
    fh.setFormatter(formatter)

    # attach the file to the logger object
    logger.addHandler(fh)
    logger.addHandler(log.StreamHandler())  # this is so it prints to console as well?

    return logger
