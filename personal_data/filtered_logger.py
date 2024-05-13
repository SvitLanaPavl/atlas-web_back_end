#!/usr/bin/env python3
'''Filtered Logger'''
import re


def filter_datum(fields, redaction, message, separator):
    '''Returns the log message obfuscated'''
    return re.sub(f'{'|'.join(re.escape(field) for
                              field in fields)}{separator}',
                  f'{redaction}{separator}', message)
