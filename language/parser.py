# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc

def p_program(p):
    """program : title clib"""
    print('program')


def p_title(p):
    """title : TITLE COLON SPACE multiline EOL"""
    print('title: \n' + p[4])


def p_clib(p):
    """clib : CLIB COLON SPACE WORD EOL"""
    print('clib: ' + p[4])


def p_string_word(p):
    """string : WORD"""
    p[0] = p[1]


def p_string_singleline(p):
    """string : string SPACE WORD"""
    p[0] = p[1] + p[2] + p[3]


def p_multiline_short(p):
    """multiline : string"""
    p[0] = p[1]


def p_multiline_splong(p):
    """multiline : multiline EOL SPACE string"""
    p[0] = p[1] + p[2] + p[3] + p[4]


def p_multiline_long(p):
    """multiline : multiline EOL string"""
    p[0] = p[1] + p[2] + p[3]



#def p_sline(p):
#    '''sline : SPACE line'''
#    p[0] = p[1] + p[2]

def p_error(p):
    print('ERROR: ' + str(p))

