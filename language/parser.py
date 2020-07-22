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


CURRENT_ACTION = None

GLOBAL_VARIABLES = {}

C_METHOD_INFO = {'method1': {}, 'method2': {}, 'method3': {}, 'gett': {}, 'gett2' : {}}

ACTION_LIST = {}

START_SKEWER = None

# Данный список должен быть генерируемым на основе заголовочного h-файла
# TODO

def p_program(p):
    """program : title EOL native_library EOL variables EOL actions shelfs skewers"""


def p_description(p):
    """description : DESCRIPTION COLON SPACE string EOL"""
    # print("description\n")


def p_skewers(p):
    """skewers : SKEWERS COLON EOL skwrs"""


def p_skwrs(p):
    """skwrs : skewer EOL EOL
             | skewer EOL skwrs"""


def p_skewer(p):
    """skewer : SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string
              | SPACE WORD COLON EOL SPACE ITEMS COLON SPACE string SPACE END"""
    global ACTION_LIST
    ACTION_LIST[p[2]] = "skewer_" + p[2]
    print("def skewer_" + p[2] + "():")

    for act in p[9].split(" "):
        if act in ACTION_LIST:
            print("    " + ACTION_LIST[act] + "()")
        else:
            print("    skewer_" + act + "()")
    print()
    print()


def p_actions(p):
    """actions : ACTIONS COLON EOL EOL
               | ACTIONS COLON EOL acts"""


def p_shelfs(p):
    """shelfs : SHELFS COLON EOL EOL
              | SHELFS COLON EOL shlfs EOL"""


def p_shlfs(p):
    """shlfs : shelf EOL
             | shelf EOL shlfs"""


def p_acts(p):
    """acts : action EOL
            | action EOL acts"""


def p_shelf(p):
    """shelf : SPACE WORD COLON EOL SPACE DESCRIPTION COLON SPACE string SPACE ASSIGNMENT \
               SPACE string EOL SPACE EXPRESSION COLON SPACE WORD SPACE ASSIGNMENT SPACE string"""
    global ACTION_LIST
    ACTION_LIST[p[2]] = "shelf_" + p[2]
    print("def shelf_" + p[2] + "():" )
    print("    global " + p[19])
    print("    " + " ".join([p[19], "=", p[23]]))
    print()
    print()


def p_action(p):
    """action : SPACE WORD COLON EOL SPACE description SPACE cblock"""
    print("def action_" + p[2] + "():")
    global CURRENT_ACTION
    global ACTION_LIST
    ACTION_LIST[p[2]] = "action_" + p[2]
    for var in CURRENT_ACTION.get_variables():
        print("    global " + var)
    for method in CURRENT_ACTION.get_methods():
        print("    " + method)
    print()
    print()
    CURRENT_ACTION = None


def p_cblock(p):
    """cblock : CBLOCK COLON SPACE methods EOL"""


def p_methods(p):
    """methods : methoddef
               | methods EOL SPACE methoddef"""


def p_methoddef(p):
    """methoddef : string"""
    lst = p[1].split()
    global  C_METHOD_INFO
    global CURRENT_ACTION
    global GLOBAL_VARIABLES
    if CURRENT_ACTION is None:
        CURRENT_ACTION = ActionDefinition()
    if len(lst) == 1:
        # ожидаем только метод
        if not lst[0] in C_METHOD_INFO:
            print(" ".join(["METHOD", "'" + lst[0] + "'", "NOT FOUND IN LIBRARY"]))
            sys.exit(1)
        else:
            CURRENT_ACTION.push_method("".join(["dlib.",lst[0],"(",")"]))
        return
    first_arg = lst[0]
    if first_arg in C_METHOD_INFO:
        method_name = lst[0]
        for arg in lst[1:]:
            if arg in GLOBAL_VARIABLES:
                CURRENT_ACTION.push_variable(arg)
        args = ",".join(lst[1:])
        CURRENT_ACTION.push_method("".join(["dlib.",method_name, "(", args, ")"]))
        return
    elif first_arg in GLOBAL_VARIABLES:
        # Первый аргумент - глобальная переменная
        # добавляем переменную в список используемых переменных
        CURRENT_ACTION.push_variable(first_arg)

    method_name = lst[1]
    if method_name not in C_METHOD_INFO:
        print(" ".join(["METHOD", "'" + method_name + "'", "NOT FOUND IN LIBRARY"]))
        sys.exit(1)
    for arg in lst[2:]:
        if arg in GLOBAL_VARIABLES:
            CURRENT_ACTION.push_variable(arg)
    args = ",".join(lst[2:])
    CURRENT_ACTION.push_method(" ".join([first_arg, "=", "".join(["dlib.",method_name,"(",args,")"])]))


def p_variables(p):
    """variables : VARIABLES COLON vars EOL"""
    global GLOBAL_VARIABLES
    for var in GLOBAL_VARIABLES:
        varDef = GLOBAL_VARIABLES[var]
        assert isinstance(varDef, VarDefinition)
        print(var + " = None")
        if varDef.inout:
            print()
            # Добавляем метод установки глобальной переменной
            print("def set_"+var + "(val):")
            print("    global " + var )
            print("    " + var + " = val")
            print()
            print()
    print()
    print()


def p_vars(p):
    """vars :
            | var
            | vars EOL var"""


def p_inout(p):
    """inout : IN
             | OUT"""
    if p[1] == 'IN':
        p[0] = True
    else:
        p[0] = False


def p_vtype(p):
    """vtype : INT
             | BOOL """
    p[0] = p[1]


def p_var(p):
    """var : SPACE inout SPACE WORD SPACE vtype SPACE string"""
    # TODO - добавить проверки
    name = p[4]
    type = p[5]
    inout = p[2]
    description = p[8]
    GLOBAL_VARIABLES[name] = VarDefinition(type, inout, description)


def p_title(p):
    """title : TITLE COLON EOL SPACE description SPACE START_SKEWER COLON SPACE WORD EOL"""
    # print('title: \n' + p[4])
    global START_SKEWER
    START_SKEWER = "skewer_" + p[10]


def p_native_library(p):
    """native_library : NATIVE_LIBRARY COLON SPACE WORD EOL"""
    print("import ctypes.util")
    print("import os")
    print("import sys")
    print("")
    print("LIBRARY_PATH = os.environ[\"LIBRARY_PATH\"]")
    print("")
    print("path = os.path.dirname(LIBRARY_PATH)")
    print("dlib = None")
    print("")
    print("try:")
    print("    dlib = ctypes.CDLL(LIBRARY_PATH" + " + \"/lib%s.so\""%p[4] +")")

    print("except OSError:")
    print("    print(\"Unable to load library lib%s.so\")"%p[4])
    print("    sys.exit()")
    print("")
    print()


def p_string_word(p):
    """string : WORD"""
    p[0] = p[1]


def p_string_row(p):
    """string : string SPACE WORD"""
    p[0] = p[1] + p[2] + p[3]


# def p_sline(p):
#    '''sline : SPACE line'''
#    p[0] = p[1] + p[2]

def p_error(p):
    print('ERROR: ' + str(p))
