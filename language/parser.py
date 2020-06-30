# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc

space_start_pos=0


def p_program(p):
    'program : title clib title title'
    print('program')


def p_title(p):
    'title : TITLE COLON SPACE multiline EOL'
    print('title: \n' + p[4])
    global space_start_pos
    space_start_pos = 0

def p_clib(p):
    'clib : CLIB COLON SPACE WORD EOL'
    print('clib: ' + p[4])


def p_string_word(p):
    'string : WORD'
    global space_start_pos
    assert isinstance(p, yacc.YaccProduction)
    if space_start_pos == 0:
        space_start_pos = p.lexpos(1)
        print('! ' + str(space_start_pos))
    p[0] = p[1]


def p_string_singleline(p):
    'string : string SPACE WORD'
    p[0] = p[1] + p[2] + p[3]


def p_multiline_short(p):
    'multiline : string'
    p[0] = p[1]


def p_multiline_long(p):
    'multiline : multiline EOL SPACE string'
    global space_start_pos
    print('len p[3] ' + str(len(p[3])))
    print('space_start_pos ' + str(space_start_pos))
    if len(p[3]) < space_start_pos:
        p_error(p[3])
        return
    p[0] = p[1] + p[2] + p[3][space_start_pos:] + p[4]



#def p_sline(p):
#    '''sline : SPACE line'''
#    p[0] = p[1] + p[2]

def p_error(p):
    print('ERROR: ' + str(p))

