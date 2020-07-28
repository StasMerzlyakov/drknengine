import sys
import os
import Ice

Ice.loadSlice('Runner.ice')
import Runner

path = os.path.dirname(os.path.realpath(__file__) )+ "/language/tests"

LIBRARY_NAME='test'
LIBRARY_PATH='%s/libtest.so'%path

SCRIPT_NAME='schema1'
SCRIPT_PATH='%s/schema1.drk'%path

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
    runnerService = Runner.RunnerServicePrx.checkedCast(communicator.stringToProxy("runner:default -h localhost -p 10000"))

    #assert len(runnerService.getLibraryList()) == 0

    #lib = bytes_from_file(LIBRARY_PATH)
    #runnerService.uploadLibrary(LIBRARY_NAME, lib)
    #assert LIBRARY_NAME in runnerService.getLibraryList()

    #lib2 = runnerService.getLibrary(LIBRARY_NAME)
    #assert lib == lib2
    #runnerService.deleteLibrary(LIBRARY_NAME)
    #print("LibraryStorage OK")

    #assert len(runnerService.getScenarioList()) == 0
    scenario = bytes_from_file(SCRIPT_PATH)
    runnerService.uploadScenario(SCRIPT_NAME, scenario)

    print(runnerService.getScenarioList())











