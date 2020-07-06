
# LEXEM DEFINITIONS
from parser import *

# Build the parser
parser = yacc.yacc()


with open ("tests/schema2.drk", "r") as file:
    data=file.readlines()
    parser.parse(''.join(data))
    #print(result)

