import sys
import os
import Ice

Ice.loadSlice('Runner.ice')
import Runner

path = os.path.dirname(os.path.realpath(__file__) )+ "/../language/tests/"


WRAPPER_NAME='test_wrapper'
WRAPPER_PATH='%s/test_wrapper.py'
LIBRARY_NAME='libtest.so'
LIBRARY_PATH='%s/libtest.so'


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
    wrapperStorage = Runner.WrapperStoragePrx.checkedCast(communicator.stringToProxy("wrapperStorage:default -h localhost -p 10000"))

    wrapperInfo  = Runner.Wrapper(bytes_from_file(WRAPPER_PATH%path), bytes_from_file(LIBRARY_PATH%path), LIBRARY_NAME)
    wrapperStorage.uploadWrapper(WRAPPER_NAME, wrapperInfo)
    print(wrapperStorage.getWrapperList())

    wrapperInfo2 = wrapperStorage.getWrapper(WRAPPER_NAME)
    assert wrapperInfo.wrapperCode == wrapperInfo2.wrapperCode
    assert wrapperInfo.nativeLibraryCode == wrapperInfo2.nativeLibraryCode
    assert wrapperInfo.nativeLibraryName == wrapperInfo2.nativeLibraryName

    wrapperStorage.deleteWrapper('test_wrapper')












