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

SCENARIO_PATH="%s/scenario"%path

if not os.path.exists(SCENARIO_PATH):
    os.makedirs(SCENARIO_PATH)

os.environ['SCENARIO_PATH'] = SCENARIO_PATH

PROCESS_PATH="%s/process"%path

if not os.path.exists(PROCESS_PATH):
    os.makedirs(PROCESS_PATH)

os.environ['PROCESS_PATH'] = PROCESS_PATH


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

from program_generator import ProgramGenerator
from view_generator import ViewGenerator

class RunnerServiceI(Runner.RunnerService):

    # LibraryStorage functions
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


    # ScenarioStorage function
    def deleteScenario(self, name, current):
        print("deleteScenario " + name)

        scenario_file_path = SCENARIO_PATH + "/%s.drk"%name
        if os.path.exists(scenario_file_path):
            os.remove(scenario_file_path)
        else:
            raise Runner.ScenarioNotExistsException()


    def getScenarioList(self, current):
        print("getScenarioList \n")
        return os.listdir(SCENARIO_PATH)


    def getScenario(self, name, current):
        print("getScenario " + name)
        scenario_file_path = SCENARIO_PATH + "/%s.drk" % name
        if not os.path.exists(scenario_file_path):
            raise Runner.ScenarioNotExistsException()
        scenario = bytes_from_file(scenario_file_path)
        return scenario


    def uploadScenario(self, name, library, current):
        print("uploadScenarion " + name)

        scenario_dir_path = SCENARIO_PATH + "/%s" % name
        if os.path.exists(scenario_dir_path):
            raise Runner.ScenarioExistsException()

        try:
            os.makedirs(scenario_dir_path)

            scenario_file_path = scenario_dir_path + "/" + name + ".drk"
            with open(scenario_file_path, 'wb') as wf:
                wf.write(library)

            program_generator = ProgramGenerator()
            program_file_path = scenario_dir_path + "/" + name + ".py"
            program_generator.generate(scenario_file_path, program_file_path)

            view_generator = ViewGenerator()
            view_file_path = scenario_dir_path + "/" + name + ".html"
            view_generator.generate(scenario_file_path, view_file_path)


        except Exception as err:
            shutil.rmtree(scenario_dir_path)
            print(err)
            raise Runner.ScenarioUploadException()


    # TODO
    def getScenarioView(self, name, current):
        print("getScenarioView " + name)

        scenario_dir_path = SCENARIO_PATH + "/%s" % name
        if not os.path.exists(scenario_dir_path):
            raise Runner.ScenarioNotExistsException()

        view_file_path = scenario_dir_path + "/" + name + ".html"
        view = bytes_from_file(view_file_path)
        return view





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
    adapter = communicator.createObjectAdapterWithEndpoints("RunnerService", "default -h localhost -p 10000")
    adapter.add(RunnerServiceI(), Ice.stringToIdentity("runner"))
    adapter.activate()
    communicator.waitForShutdown()



