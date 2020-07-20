import ctypes.util
import os
import sys

path = os.path.dirname(os.path.realpath(__file__))
dlib = None

try:
    dlib = ctypes.CDLL("%s/libtest.so"%path)
except OSError:
    print("Unable to load library libtest.so")
    sys.exit()

dlib.method1.argtypes = [ctypes.c_int, ]

dlib.method2.restype = ctypes.c_int
dlib.method2.argtypes = [ctypes.c_bool, ]
dlib.method3.argtypes = [ctypes.c_int, ]

