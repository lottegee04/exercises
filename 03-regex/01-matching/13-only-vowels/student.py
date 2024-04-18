# Write your code here
import re

def only_vowels(string):
    return re.fullmatch(r'(a|e|i|o|u)*' , string)