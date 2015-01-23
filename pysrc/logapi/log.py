#!/usr/bin/python
#coding: utf-8

import logging
import logging.handlers

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

rh=logging.handlers.TimedRotatingFileHandler('../../log/xingzuo','D')
logger.addHandler(rh)

debug=logger.debug
info=logger.info
warn=logger.warn
error=logger.error
critical=logger.critical


