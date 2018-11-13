import os
import re

with os.popen('who', 'r') as reader:
    for r in reader:
        print(re.split(r'\s\s+|\t', r.strip()))
