# Write your code here
import re

def ten_or_more_abc(string):
    return re.fullmatch(r'(abc){10,}', string)