import Ice
import sys
import os
import signal
import shutil


Ice.loadSlice('Runner.ice')
import Runner

path = os.path.dirname(os.path.realpath(__file__) )

WORK_DIRECTORY="%s/wrappers"%path

if not os.path.exists(WORK_DIRECTORY):
    os.makedirs(WORK_DIRECTORY)


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


class WrapperStorageI(Runner.WrapperStorage):

    def deleteWrapper(self, name, current):
        print("deleteWrapper " + name)

        wrapper_dir = WORK_DIRECTORY + "/" + name
        if os.path.exists(wrapper_dir):
            shutil.rmtree(wrapper_dir)


    def getWrapperList(self, current):
        print("getWrapperList \n")
        return os.listdir(WORK_DIRECTORY)


    def uploadWrapper(self, name, wrapper, current):
        print("uploadWrapper " + name)
        wrapper_dir = WORK_DIRECTORY + "/" + name
        if os.path.exists(wrapper_dir):
            raise Runner.WrapperExistsException()
        os.makedirs(wrapper_dir)

        wraper_file = wrapper_dir + "/" + name + ".py"
        with open(wraper_file, 'wb') as wf:
            wf.write(wrapper.wrapperCode)

        lib_file = wrapper_dir + "/" + wrapper.nativeLibraryName

        with open(lib_file, 'wb') as wf:
            wf.write(wrapper.nativeLibraryCode)

    def getWrapper(self, name, current):
        wrapper_dir = WORK_DIRECTORY + "/" + name
        if not os.path.exists(wrapper_dir):
            raise Runner.WrapperNotExistsException()
        nativelib = bytearray()
        libname = ""
        wrapper = bytearray()
        for f in os.listdir(wrapper_dir):
            if f.endswith(".py"):
                wrapper = bytes_from_file(wrapper_dir + "/" +f)
            if f.endswith(".so"):
                nativelib = bytes_from_file(wrapper_dir + "/" + f)
                libname = f
        return  Runner.Wrapper(wrapper, nativelib, libname)





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
    adapter = communicator.createObjectAdapterWithEndpoints("WrapperStorage", "default -h localhost -p 10000")
    adapter.add(WrapperStorageI(), Ice.stringToIdentity("wrapperStorage"))
    adapter.activate()
    communicator.waitForShutdown()



