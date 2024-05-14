#!/usr/bin/env python3
'''Filtered Logger'''
import re
from typing import List
import logging
import mysql.connector
import os


def filter_datum(
        fields: List[str],
        redaction: str,
        message: str,
        separator: str
        ) -> str:
    '''Returns the log message obfuscated'''
    pattern = '|'.join(re.escape(field) for field in fields)
    return re.sub(f'({pattern})=(.*?){re.escape(separator)}',
                  f'\\1={redaction}{separator}', message)


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''Constructor'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        '''Filter values in incoming logs'''
        original_msg = record.msg
        record.msg = filter_datum(
            self.fields, self.REDACTION, original_msg, self.SEPARATOR)
        formatted = super().format(record)
        record.msg = original_msg
        return formatted


PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')
DATA_FILE = 'user_data.csv'


def get_logger() -> logging.Logger:
    '''Returns logging.Logger object'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logging.basicConfig(filename=DATA_FILE, level=logging.INFO)
    logger.propagate = False
    stream = logging.StreamHandler()
    formatter = RedactingFormatter(PII_FIELDS)
    stream.setFormatter(formatter)
    logger.addHandler(stream)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Returns connector to the database'''
    db_username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    db_password = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    db_host = os.getenv('PERSONAL_DATA_DB_HOST')
    db_name = os.getenv('PERSONAL_DATA_DB_NAME')
    return mysql.connector.connect(user=db_username, password=db_password,
                                   host=db_host,
                                   database=db_name)
