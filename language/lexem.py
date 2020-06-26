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

    'ASSIGNMENT', 'COLON', 'TYPE', 'CBLOCK', 'INOUT', 'NUMBER', 'EXPRESSION',

    # EXPRESSIONS
    'TRUE', 'FALSE', 'LPARENT', 'RPAREN',
    'EOL',
    'NAME',
    'SPACE',
    'LINE'
)

t_TITLE=r'TITLE'
t_CLIB=r'CLIB'
t_DESCRIPTION=r'DESCRIPTION'
t_VARIABLES=r'VARIABLES'
t_INT=r'INT'
t_BOOL=r'BOOL'
t_INOUT=r'IN|OUT'
t_ACTIONS=r'ACTIONS'
t_SHELFS=r'SHELFS'
t_SKEWERS=r'SKEWERS'
t_ASSIGNMENT=r':='
t_COLON=r':'
t_TYPE=r'TYPE'
t_CBLOCK=r'CBLOCK'
t_EOL = r'\n'
t_LINE = r'[^: \n][^\n]+'
t_EXPRESSION=r'EXPRESSION'
t_TRUE=r'TRUE'
t_FALSE=r'FALSE'
t_NUMBER = r'\d+'
t_SPACE = r'[ ]+'
t_NAME = r'[A-Z][A-Za-z0-9_@]*'






