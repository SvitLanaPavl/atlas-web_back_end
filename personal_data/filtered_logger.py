#!/usr/bin/env python3
'''Filtered Logger'''
import re
from typing import List
import logging


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
