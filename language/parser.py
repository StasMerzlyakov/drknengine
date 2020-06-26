# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc

def p_desc(p):
    '''desc : TITLE COLON SPACE LINE EOL'''
    print('desc')

def p_clib(p):
    '''clib : CLIB COLON SPACE LINE EOL'''
    print('clib')

def p_program(p):
    '''program : desc clib'''
    print('program')

