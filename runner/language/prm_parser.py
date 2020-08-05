# LEXEM DEFINITIONS
from language.lexem import *

import ply.yacc as yacc
import sys

def p_program(p):
    """program : title EOL native_library EOL variables EOL actions shelfs end EOL skewers"""


def p_description(p):
    """description : DESCRIPTION COLON SPACE string EOL"""
    # print("description\n")


def p_skewers(p):
    """skewers : SKEWERS COLON EOL skwrs"""


def p_skwrs(p):
    """skwrs : skewer EOL svg
             | skewer EOL svg skwrs"""


def p_svg(p):
    """svg : SPACE SVG COLON EOL svgdef EOL"""


def p_svgdef(p):
    """svgdef : SPACE string EOL
              | SPACE string EOL svgdef"""


def p_skewer(p):
    """skewer : SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string
              | SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string SPACE END"""


def p_actions_empty(p):
    """actions : ACTIONS COLON EOL EOL"""


def p_action_full(p):
    """actions : ACTIONS COLON EOL acts"""


def p_shelfs(p):
    """shelfs : SHELFS COLON EOL
              | SHELFS COLON EOL shlfs"""


def p_shlfs(p):
    """shlfs : shelf EOL
             | shelf EOL shlfs"""


def p_acts(p):
    """acts : action EOL
            | action EOL acts"""


def p_shelf(p):
    """shelf : SPACE WORD COLON EOL SPACE DESCRIPTION COLON SPACE string SPACE ASSIGNMENT \
               SPACE string EOL SPACE EXPRESSION COLON SPACE WORD SPACE ASSIGNMENT SPACE string EOL svg"""


def p_action(p):
    """action : SPACE WORD COLON EOL SPACE description SPACE cblock EOL svg"""


def p_cblock(p):
    """cblock : CBLOCK COLON SPACE methods EOL"""


def p_methods(p):
    """methods : methoddef
               | methods EOL SPACE methoddef"""


def p_methoddef(p):
    """methoddef : string"""


def p_variables(p):
    """variables : VARIABLES COLON vars EOL"""
    p[0] = p[3]


def p_vars(p):
    """vars :
            | var
            | vars EOL var"""

def p_inout(p):
    """inout : IN
             | OUT"""
    p[0] = p[1]


def p_vtype(p):
    """vtype : INT
             | BOOL """
    p[0] = p[1]


def p_var(p):
    """var : SPACE inout SPACE WORD SPACE vtype SPACE string"""
    print(" ".join([p[4], p[6],p[2]]))


def p_title(p):
    """title : TITLE COLON EOL SPACE description SPACE START_SKEWER COLON SPACE WORD EOL svg"""


def p_native_library(p):
    """native_library : NATIVE_LIBRARY COLON SPACE WORD EOL"""


def p_string_word(p):
    """string : WORD"""


def p_string_row(p):
    """string : string SPACE WORD"""


def p_end(p):
    """end : END COLON EOL svg"""


def p_error(p):
    print('ERROR: ' + str(p))
