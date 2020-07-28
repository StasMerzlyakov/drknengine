import os
path = os.path.dirname(os.path.realpath(__file__))
os.environ['LIBRARY_PATH'] = path

from generated import set_I1, skewer_SK_1

if __name__=="__main__":
    set_I1(2)
    skewer_SK_1()
