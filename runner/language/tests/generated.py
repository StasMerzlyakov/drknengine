import ctypes.util
import os
import sys

LIBRARY_PATH = os.environ["LIBRARY_PATH"]

path = os.path.dirname(LIBRARY_PATH)
dlib = None

try:
    dlib = ctypes.CDLL(LIBRARY_PATH + "/libtest.so")
except OSError:
    print("Unable to load library libtest.so")
    sys.exit()


B3 = None
I2 = None
I1 = None

def set_I1(val):
    global I1
    I1 = val




def action_A_1():
    global I1
    global B3
    dlib.method1(I1)
    i = dlib.method2(B3)
    dlib.method3(i)


def action_A_2():
    global I2
    dlib.method1(I2)


def action_A_3():
    dlib.gett()
    dlib.gett2()


def shelf_S_1():
    global B3
    B3 = True


def shelf_S_2():
    global I2
    I2 = 50


def shelf_S_3():
    global B3
    B3 = False


def skewer_SK_1():
    shelf_S_2()
    shelf_S_3()
    action_A_1()
    action_A_2()
    action_A_3()
    shelf_S_1()


