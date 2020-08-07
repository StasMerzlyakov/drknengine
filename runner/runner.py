import Ice
import sys
import os
import signal
import shutil

Ice.loadSlice('Runner.ice')
import Runner

import process_invoker

path = os.path.dirname(os.path.realpath(__file__) ) + "/db"

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
from prm_generator import PrmGenerator
from language.program_parser import LibraryNotFoundException


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
        scenario_dir_path = SCENARIO_PATH + "/%s" % name
        if os.path.exists(scenario_dir_path):
            shutil.rmtree(scenario_dir_path)
            raise Runner.LibraryNotExistsException()
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

    def startProcess(self, scenarioName, valueSeq, current):
        print("startProcess " + scenarioName)
        scenario_dir_path = SCENARIO_PATH + "/%s" % scenarioName
        return process_invoker.start_process(scenarioName, scenario_dir_path, valueSeq)

    def getProcessValues(self, processName, current):
        if processName in process_invoker.PROCESS_INFO_MAP:
            result = {}
            for key in list(process_invoker.PROCESS_INFO_MAP[processName]):
                v = process_invoker.PROCESS_INFO_MAP[processName][key]
                result[key] = Runner.ParameterValue(str(v.value))
            return result
        else:
            raise Runner.ProcessNotExist()


    def uploadScenario(self, name, library, current):
        print("uploadScenarion " + name)

        scenario_dir_path = SCENARIO_PATH + "/%s" % name

        print(scenario_dir_path)

        if os.path.exists(scenario_dir_path):
            raise Runner.ScenarioExistsException()

        try:
            os.makedirs(scenario_dir_path)

            scenario_file_path = scenario_dir_path + "/" + name + ".drk"
            with open(scenario_file_path, 'wb') as wf:
                wf.write(library)

            print(scenario_file_path)

            program_generator = ProgramGenerator()
            program_file_path = scenario_dir_path + "/" + name + ".py"
            program_generator.generate(scenario_file_path, program_file_path)

            view_generator = ViewGenerator()
            view_file_path = scenario_dir_path + "/" + name + ".html"
            view_generator.generate(scenario_file_path, view_file_path)

            prm_generator = PrmGenerator()
            prm_file_path = scenario_dir_path + "/" + name + ".prm"
            prm_generator.generate(scenario_file_path, prm_file_path)

        except LibraryNotFoundException as lexp:
            print("Требуемая для сценария блиотека %s не найдена "%str(lexp))
            shutil.rmtree(scenario_dir_path)
            raise Runner.LibraryNotExistsException()
        except Exception as err:
            shutil.rmtree(scenario_dir_path)
            print("Исключение : " + str(err))
            raise Runner.ScenarioUploadException()


    def getScenarioView(self, name, current):
        print("getScenarioView " + name)

        scenario_dir_path = SCENARIO_PATH + "/%s" % name
        if not os.path.exists(scenario_dir_path):
            raise Runner.ScenarioNotExistsException()

        view_file_path = scenario_dir_path + "/" + name + ".html"
        view = bytes_from_file(view_file_path)
        return view


    def getScenarioParameters(self, name, current):
        print("getScenarioParameters " + name)

        scenario_dir_path = SCENARIO_PATH + "/%s" % name
        if not os.path.exists(scenario_dir_path):
            raise Runner.ScenarioNotExistsException()

        prm_file_path = scenario_dir_path + "/" + name + ".prm"
        resultList = []
        with open(prm_file_path) as prm:
            for line in prm:
                name, type, inout = line.split(' ')
                if inout == 'IN':
                    inout = Runner.ParameterType.IN
                else:
                    inout = Runner.ParameterType.OUT
                resultList.append(Runner.ParameterInfo(name, type, inout))
        return resultList





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



