# LEXEM DEFINITIONS
from prm_parser import *

# Build the parser
parser = yacc.yacc()

with open ("tests/schema1.drk", "r") as file:
    data=file.readlines()
    parser.parse(''.join(data))


