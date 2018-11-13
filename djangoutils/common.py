# -*- coding: utf-8 -*-

import string
import random
import zipfile
import os
import logging

logger = logging.getLogger(__name__)


def generate_random_string(length, digit=True, uppercase=True, lowercase=True,
                           sign=False):
    available_chars = ''
    if digit:
        available_chars += string.digits
    if uppercase:
        available_chars += string.ascii_uppercase
    if lowercase:
        available_chars += string.ascii_lowercase
    if sign:
        available_chars += string.printable[62:94]

    return ''.join((random.choice(available_chars) for i in range(length)))


def generate_zip_file(src, dest):
    try:
        f = zipfile.ZipFile(dest, 'w', zipfile.ZIP_DEFLATED)
        for dirpath, dirnames, filenames in os.walk(src):
            for filename in filenames:
                print(dirpath)
                f.write(os.path.join(dirpath, filename))
        f.close()
        return True
    except Exception as zip_error:
        logging.error(zip_error)
        return False

if __name__ == '__main__':
    print(generate_zip_file("D:\WorkSpace\op-red-line.zip", "D:\op-red-line.zip"))