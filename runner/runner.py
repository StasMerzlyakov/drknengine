import Ice
import sys
import os
import signal
import shutil


Ice.loadSlice('Runner.ice')
import Runner

path = os.path.dirname(os.path.realpath(__file__) )

import os
path = os.path.dirname(os.path.realpath(__file__))


LIBRARY_PATH="%s/libs"%path

if not os.path.exists(LIBRARY_PATH):
    os.makedirs(LIBRARY_PATH)

os.environ['LIBRARY_PATH'] = LIBRARY_PATH


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


class LibraryStorageI(Runner.LibraryStorage):

    def deleteLibrary(self, name, current):
        print("deleteLibrary " + name)

        lib_file_path = LIBRARY_PATH + "/lib%s.so"%name
        if os.path.exists(lib_file_path):
            os.remove(lib_file_path)
        else:
            raise Runner.LibraryNotExistsException()


    def getLibraryList(self, current):
        print("getLibraryList \n")
        resultlib = []
        for l in os.listdir(LIBRARY_PATH):
            if l.startswith("lib") and l.endswith(".so"):
                resultlib.append(l.replace(".so", "").replace("lib", ""))

        return resultlib


    def uploadLibrary(self, name, library, current):
        print("uploadLibrary " + name)
        lib_file_path = LIBRARY_PATH + "/lib%s.so"%name
        if os.path.exists(lib_file_path):
            raise Runner.LibraryExistsException()
        with open(lib_file_path, 'wb') as wf:
            wf.write(library)

    def getLibrary(self, name, current):
        print("getLibrary " + name)
        lib_file_path = LIBRARY_PATH + "/lib%s.so"%name
        if not os.path.exists(lib_file_path):
            raise Runner.LibraryNotExistsException()
        nativelib = bytes_from_file(lib_file_path)
        return nativelib


#
# Ice.initialize returns an initialized Ice communicator,
# the communicator is destroyed once it goes out of scope.
#
with Ice.initialize(sys.argv) as communicator:
    #
    # Install a signal handler to shutdown the communicator on Ctrl-C
    #
    signal.signal(signal.SIGINT, lambda signum, frame: communicator.shutdown())
    if hasattr(signal, 'SIGBREAK'):
        signal.signal(signal.SIGBREAK, lambda signum, frame: communicator.shutdown())
    adapter = communicator.createObjectAdapterWithEndpoints("LibraryStorage", "default -h localhost -p 10000")
    adapter.add(LibraryStorageI(), Ice.stringToIdentity("libraryStorage"))
    adapter.activate()
    communicator.waitForShutdown()



