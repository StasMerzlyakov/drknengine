# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc


def p_program(p):
    """program : title clib description variables"""
    print('program')


def p_description(p):
    """description : DESCRIPTION COLON SPACE multiline EOL"""
    print("description\n")


def p_variables(p):
    """variables : VARIABLES COLON vars EOL"""


def p_vars_empty(p):
    """vars :
            | var
            | vars EOL var"""


def p_inout(p):
    """inout : IN
             | OUT"""


def p_vtype(p):
    """vtype : INT
             | BOOL """


def p_var(p):
    """var : SPACE inout SPACE WORD SPACE vtype SPACE string"""


def p_title(p):
    """title : TITLE COLON SPACE string EOL"""
    print('title: \n' + p[4])


def p_clib(p):
    """clib : CLIB COLON SPACE WORD EOL"""
    print('clib: ' + p[4])


def p_string_word(p):
    """string : WORD"""
    p[0] = p[1]


def p_string_row(p):
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

