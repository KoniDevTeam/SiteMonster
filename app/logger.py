"""Logging methods"""
import logging
import platform

from api import files


def init_log(sess_name):
    logging.basicConfig(format=u'%(filename)s[LINE:%(lineno)d]# %(levelname)-8s [%(asctime)s]  %(message)s',
                        level=logging.DEBUG)
    logging.basicConfig(format=u'%(levelname)-8s [%(asctime)s] %(message)s',
                        level=logging.DEBUG, filename=files.get_data_folder() + 'latest-' + sess_name + '.log')


def log_pc_info():
    logging.info("Machine - " + platform.machine())
    logging.info("System - " + platform.system())
    logging.info("System release - " + platform.release())
    logging.info("System version - " + platform.version())
    logging.info("CPU - " + platform.processor())
    logging.info("uname - " + str(platform.uname()))