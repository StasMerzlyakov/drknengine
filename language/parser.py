# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc


def p_program(p):
    '''program : desc clib'''
    print('program')


def p_desc(p):
    '''desc : TITLE COLON SPACE line EOL'''
    print('title: ' + p[4])


def p_clib(p):
    '''clib : CLIB COLON SPACE WORD EOL'''
    print('clib: ' + p[4])


def p_line_short(p):
    '''line : WORD'''
    p[0] = p[1]


def p_line_long(p):
    '''line : WORD sline'''
    p[0] = p[1] + p[2]


def p_sline(p):
    '''sline : SPACE line'''
    p[0] = p[1] + p[2]


def p_error(p):
    print('ERROR: ' + str(p))

