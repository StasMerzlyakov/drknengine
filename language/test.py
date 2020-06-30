
# LEXEM DEFINITIONS
from parser import *

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Build the parser
parser = yacc.yacc()


with open ("tests/schema1.drk", "r") as file:
    data=file.readlines()
    parser.parse(''.join(data))
    #print(result)

