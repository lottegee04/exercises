# Write your code here
import re
def is_valid_time(string):
    return re.fullmatch(r'[0-9][0-9]:[0-9][0-9]:[0-9][0-9](\.[0-9][0-9][0-9])?',string)