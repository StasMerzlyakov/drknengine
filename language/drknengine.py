# -------------------------------------------------------
# DRAKON Engine definition language
# drknengine.py
# ------------------------------------------------------- 
import lex

tokens = (

    'TITLE', 'CLIB', 'DESCRIPTION', 'VAR'

    # PROPERTIES TYPES
    'INT', 'BOOL', 'FLOAT'
    
    # DRAKON ICONS
    'ACTION', 'SHELF'

    'ASSIGNMENT', 'COLON', 'ID', 'TYPE', 'CBLOCK', 'DESCRIPTION', 
    'ICONNAME', 'SHARP', 'LPARENT', 'RPAREN',
    'EOL',
    'NAME',
    'LINE'

)

t_TITLE=r'TITLE'
t_CLIB=r'CLIB'
t_DESCRIPTION=r'DESC'
t_VAR=r'VAR'
t_INT=r'INT'
t_BOOL=r'BOOL'
t_FLOAT=r'FLOAT'
t_ACTION=r'ACTION'
t_SHELF=r'SHELF'
t_ASSIGNMENT=r'ASSIGNMENT'
t_COLON=r':'
t_ID=r'ID'
t_TYPE=r'TYPE'
t_CBLOCK=r'CBLOCK'
t_DESCRIPTION=r'DESCRIPTION'
t_ICONNAME=r'ICONNAME'
t_SHARP=r'#'
t_NAME=r'NAME'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_EOL = r'\n'
t_NAME = r'[A-Za-z_@][A-Za-z0-9_@]*'
t_LINE = r'[^\n]'





