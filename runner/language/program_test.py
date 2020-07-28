import os

LIBRARY_PATH='./tests'
os.environ['LIBRARY_PATH'] = LIBRARY_PATH


# LEXEM DEFINITIONS
from program_parser import *

# Build the parser
parser = yacc.yacc()

with open ("tests/schema1.drk", "r") as file:
    data=file.readlines()
    parser.parse(''.join(data))
    #print(result)

