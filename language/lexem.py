# -------------------------------------------------------
# DRAKON Engine definition language
# lexem.py
# ------------------------------------------------------- 
tokens = (
    'TITLE', 'CLIB', 'DESCRIPTION',
    # VARIABLES
    'VARIABLES', 'INTOUT', 'INT', 'BOOL',
    
    # DRAKON 
    'ACTIONS', 'SHELFS', 'SKEWERS',

    'ASSIGNMENT', 'COLON', 'TYPE', 'CBLOCK', 'IN', 'OUT', 'NUMBER', 'EXPRESSION', 'ID'

    # EXPRESSIONS
    'TRUE', 'FALSE', 'LPARENT', 'RPAREN',
    'EOL',
    'SPACE',
    'WORD'
)

reserved = {
    'TITLE' : 'TITLE',
    'CLIB' : 'CLIB',
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
    'CBLOCK':'CBLOCK',
    'EXPRESSION':'EXPRESSION',
    'TRUE':'TRUE',
    'FALSE':'FALSE'
}


t_ASSIGNMENT=r':='
t_COLON=r':'
# контектно зависимые значения
#t_NUMBER = r'\d+'
#t_ID = r'[A-Z][A-Za-z0-9_@]*'
t_SPACE = r'[ ]+'
t_EOL = r'\n'

def t_WORD(t):
    r'[^: \n]+'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t







