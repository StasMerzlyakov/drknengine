# -------------------------------------------------------
# DRAKON Engine definition language
# lexem.py
# ------------------------------------------------------- 

tokens = (
    'TITLE', 'NATIVE_LIBRARY', 'DESCRIPTION',
    # VARIABLES
    'VARIABLES', 'INTOUT', 'INT', 'BOOL',

    # DRAKON 
    'ACTIONS', 'SHELFS', 'SKEWERS', 'ITEMS',

    'ASSIGNMENT', 'COLON', 'TYPE', 'CBLOCK', 'IN', 'OUT', 'NUMBER', 'EXPRESSION', 'ID', 'START_SKEWER', 'END',

    # EXPRESSIONS
    'EOL',
    'SPACE',
    'WORD',
    'SVG'

)

reserved = {
    'END': 'END',
    'START_SKEWER' :'START_SKEWER',
    'TITLE' : 'TITLE',
    'NATIVE_LIBRARY' : 'NATIVE_LIBRARY',
    'DESCRIPTION' : 'DESCRIPTION',
    'VARIABLES' : 'VARIABLES',
    'INT': 'INT',
    'BOOL': 'BOOL',
    'IN': 'IN',
    'OUT': 'OUT',
    'ACTIONS': 'ACTIONS',
    'SHELFS': 'SHELFS',
    'SKEWERS': 'SKEWERS',
    'TYPE': 'TYPE',
    'ITEMS':'ITEMS',
    'CBLOCK':'CBLOCK',
    'EXPRESSION':'EXPRESSION',
    'SVG':'SVG'
}


t_ASSIGNMENT=r':='
t_COLON=r':'
# контектно зависимые значения
#t_NUMBER = r'\d+'
#t_ID = r'[A-Z][A-Za-z0-9_@]*'
t_SPACE = r'[ ]+'
t_EOL=r'\n'


def t_WORD(t):
    r'[^: \n]+'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
import ply.lex as lex
lexer = lex.lex()

setattr(lexer, 'prvlinepos', 0)




