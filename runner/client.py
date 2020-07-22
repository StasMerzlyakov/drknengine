import sys
import os
import Ice

Ice.loadSlice('Runner.ice')
import Runner

path = os.path.dirname(os.path.realpath(__file__) )+ "/../language/tests/"

LIBRARY_NAME='test'
LIBRARY_PATH='%s/libtest.so'%path


def bytes_from_file(filename, chunksize=8192):
    frame = bytearray()
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(chunksize)
            if chunk:
                frame.extend(chunk)
            else:
                break
    return frame



with Ice.initialize(sys.argv) as communicator:
    libraryStorage = Runner.LibraryStoragePrx.checkedCast(communicator.stringToProxy("libraryStorage:default -h localhost -p 10000"))
    lib = bytes_from_file(LIBRARY_PATH)
    libraryStorage.uploadLibrary(LIBRARY_NAME, lib)
    print(libraryStorage.getLibraryList())

    lib2 = libraryStorage.getLibrary(LIBRARY_NAME)
    assert lib == lib2
    libraryStorage.deleteLibrary(LIBRARY_NAME)












