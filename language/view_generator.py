# LEXEM DEFINITIONS
from lexem import *

import ply.yacc as yacc
import sys


class VarDefinition:
    def __init__(self, type, inout, description):
        self.type = type
        self.inout = inout
        self.description = description


class ActionDefinition:
    def __init__(self):
        # список используемых глобальных переменных
        self.variables=[]
        # список вызываемых методов
        self.methods=[]

    def push_variable(self, name):
        """ Метод добавления переменных в список """
        if not name in self.variables:
            self.variables.append(name)

    def get_variables(self):
        """ Получение списка используемых глобальных переменных """
        for variable in self.variables:
            yield variable

    def push_method(self, method):
        self.methods.append(method)

    def get_methods(self):
        """ Получение списка методов блока """
        for method in self.methods:
            yield method


# Данный список должен быть генерируемым на основе заголовочного h-файла
# TODO

def p_program(p):
    """program : title EOL native_library EOL variables EOL actions shelfs end EOL skewers"""
    print('<svg xmlns="http://www.w3.org/2000/svg" version="1.1" xmlns:xlink="http://www.w3.org/1999/xlink" xmlns:svgjs="http://svgjs.com/svgjs" width="100%" height="100%">')
    print(p[11])
    print(p[1])
    print(p[7])
    print(p[8])
    print(p[9])
    print('</svg>')


def p_description(p):
    """description : DESCRIPTION COLON SPACE string EOL"""
    # print("description\n")


def p_skewers(p):
    """skewers : SKEWERS COLON EOL skwrs"""
    p[0] = p[4]


def p_skwrs(p):
    """skwrs : skewer EOL svg
             | skewer EOL svg skwrs"""
    if len(p) == 4:
        p[0] = p[3]
    else:
        p[0] = p[3] + p[4]


def p_svg(p):
    """svg : SPACE SVG COLON EOL svgdef EOL"""
    p[0] = p[5]


def p_svgdef(p):
    """svgdef : SPACE string EOL
              | SPACE string EOL svgdef"""
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[2] + '\n' + p[4]


def p_skewer(p):
    """skewer : SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string
              | SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string SPACE END"""


def p_actions_empty(p):
    """actions : ACTIONS COLON EOL EOL"""
    p[0] = ""



def p_action_full(p):
    """actions : ACTIONS COLON EOL acts"""
    p[0] = p[4]

def p_shelfs(p):
    """shelfs : SHELFS COLON EOL
              | SHELFS COLON EOL shlfs"""
    if len(p) == 4:
        p[0] = ""
    else:
        p[0] = p[4]


def p_shlfs(p):
    """shlfs : shelf EOL
             | shelf EOL shlfs"""
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[3]


def p_acts(p):
    """acts : action EOL
            | action EOL acts"""
    if len(p) == 3:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[3]


def p_shelf(p):
    """shelf : SPACE WORD COLON EOL SPACE DESCRIPTION COLON SPACE string SPACE ASSIGNMENT \
               SPACE string EOL SPACE EXPRESSION COLON SPACE WORD SPACE ASSIGNMENT SPACE string EOL svg"""
    p[0] = p[25]


def p_action(p):
    """action : SPACE WORD COLON EOL SPACE description SPACE cblock EOL svg"""
    p[0] = p[10]


def p_cblock(p):
    """cblock : CBLOCK COLON SPACE methods EOL"""


def p_methods(p):
    """methods : methoddef
               | methods EOL SPACE methoddef"""


def p_methoddef(p):
    """methoddef : string"""


def p_variables(p):
    """variables : VARIABLES COLON vars EOL"""


def p_vars(p):
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
    """title : TITLE COLON EOL SPACE description SPACE START_SKEWER COLON SPACE WORD EOL svg"""
    # print('title: \n' + p[4])
    p[0] = p[12]


def p_native_library(p):
    """native_library : NATIVE_LIBRARY COLON SPACE WORD EOL"""


def p_string_word(p):
    """string : WORD"""
    p[0] = p[1]


def p_string_row(p):
    """string : string SPACE WORD"""
    p[0] = p[1] + p[2] + p[3]


def p_end(p):
    """end : END COLON EOL svg"""
    p[0] = p[4]

# def p_sline(p):
#    '''sline : SPACE line'''
#    p[0] = p[1] + p[2]

def p_error(p):
    print('ERROR: ' + str(p))
