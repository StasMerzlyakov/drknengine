#
# Модуль запуска процессов
#

import ctypes
import string
import random

from multiprocessing import Process, Value
import importlib.util

# Таблица с данным по процессам
# Ключ - имя процесса, значение - спсисок значений выходных переменных

PROCESS_INFO_MAP = {}

CTYPES_MAP = {
    'INT': ctypes.c_int,
    'BOOL': ctypes.c_bool
}

PYTYPES_MAP = {
    'INT': int,
    'BOOL': bool
}


class ProcessNotFound(Exception):
    pass


def get_random_string():
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(8))
    return result_str


def get_process_parameters(processName):
    result = {}
    if processName in PROCESS_INFO_MAP:
        process_info = PROCESS_INFO_MAP[processName]
        for k, v in process_info:
            result[k] = v.value
    else:
        raise ProcessNotFound()
    return result


def start_process(scenarioName, scenario_dir_path, valueMap):
    assert isinstance(scenarioName, str)
    global PYTYPES_MAP
    global CTYPES_MAP
    global PROCESS_INFO_MAP
    # valueSeq
    #    string name;
    #    string value;

    # создаем имя процесса и по совместительству - имя модуля
    processName = "_".join([scenarioName, get_random_string()])

    scenario_py_path = scenario_dir_path + "/" + scenarioName + ".py"

    spec = importlib.util.spec_from_file_location(processName, scenario_py_path)
    mod = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(mod)

    # Загрузка параметров сценария
    prm_file_path = scenario_dir_path + "/" + scenarioName + ".prm"
    outParameters = {}
    global PROCESS_INFO
    with open(prm_file_path) as prm:
        for line in prm:
            name, type, inout = line.strip().split(' ')

            if inout == 'IN':
                # входящие аргументы устанавливаем непосредственно
                value = valueMap[name].value
                setattr(mod, name, PYTYPES_MAP[type](value))
            else:
                # исходящие параметры устанавливаем через multiprocessing.Value
                val = Value(CTYPES_MAP[type])
                outParameters[name] = val
                setattr(mod, name, val)

    PROCESS_INFO_MAP[processName] = outParameters

    # начинаем с первого
    fn = getattr(mod, "start")
    p = Process(target=fn, daemon=True)
    p.start()
    return processName
