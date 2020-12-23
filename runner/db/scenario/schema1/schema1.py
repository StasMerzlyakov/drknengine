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


def action_A_1():
    global I1
    global B3
    dlib.method1(I1)
    i = dlib.method2(B3.value)
    dlib.method3(i)


def action_A_2():
    global I2
    dlib.method1(I2.value)


def action_A_3():
    dlib.gett()
    dlib.gett2()


def shelf_S_1():
    global B3
    B3.value = False


def shelf_S_2():
    global I2
    I2.value = 50


def shelf_S_3():
    global B3
    B3.value = True


def skewer_SK_1():
    import time
    time.sleep(10)

    shelf_S_2()
    shelf_S_3()
    action_A_1()
    action_A_2()
    action_A_3()
    shelf_S_1()
    print("schema1 finished")

def start():
    skewer_SK_1()



