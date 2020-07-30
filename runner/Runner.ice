#pragma once

module Runner
{
    sequence<byte> ByteSeq;

    sequence<string> StringSeq;

    exception LibraryExistsException
    {
    }

    exception LibraryNotExistsException
    {
    }

    exception LibraryUploadException
    {
    }

    interface LibraryStorage
    {
        // Получить список загруженных библиотек
        StringSeq getLibraryList();

        // Выгрузить библиотеку из хранилища
        ByteSeq getLibrary(string name) throws LibraryNotExistsException;

        // Удалить библиотеку из хранилища
        void deleteLibrary(string name)  throws LibraryNotExistsException;

        // Залить библиотеку в хранилище
        void uploadLibrary(string name, ByteSeq library)
            throws LibraryExistsException, LibraryUploadException;
    }

    exception ScenarioExistsException
    {
    }

    exception ScenarioNotExistsException
    {
    }

    exception ScenarioUploadException
    {
    }


    interface ScenarioStorage
    {
        // Получить список сценариев
        StringSeq getScenarioList();

        // Выгрузить сценарий из хранилища
        ByteSeq getScenario(string name) throws ScenarioNotExistsException;

        // Удалить сценарий из хранилища
        void deleteScenario(string name)  throws ScenarioNotExistsException;

        // Залить сценарий в хранилище
        void uploadScenario(string name, ByteSeq library)
            throws ScenarioExistsException, ScenarioUploadException, LibraryNotExistsException;

        // Получить визуальное представление DRAKON-схемы
        ByteSeq getScenarioView(string name) throws ScenarioNotExistsException;
    }


    enum ParameterType { IN, OUT }

    struct ParameterInfo
    {
        // имя переменной
        string name;

        // ДРАКОН-тип переменой
        string type;

        // Тип входа
        ParameterType inout;
    }

    sequence<ParameterInfo> ParameterInfoSeq;

    struct ParameterValue
    {
        // имя переменной
        string name;

        // значение переменой
        string value;
    }


    sequence<ParameterValue> ParameterValueSeq;

    enum ProcessState { Running, Paused, Finished, Error }

    exception WrongParametersException
    {
    }

    exception ProcessNotExist
    {
    }

    interface ProcessInvoker
    {
        // Получить информацию о входных и выходных параметрах сценария.
        ParameterInfoSeq getScenarioParameters(string scenarioName) throws ScenarioNotExistsException;

        // Запуск процесса.
        string startProcess(ParameterValueSeq valueSeq, string scenarioName) throws ScenarioNotExistsException, WrongParametersException;

        // Получить состояине процесса
        ProcessState getProcessState(string processName) throws ProcessNotExist;

        // Получить значения параметров процесса
        ParameterValueSeq getProcessValues(string processName) throws ProcessNotExist;

    }


    interface RunnerService extends LibraryStorage, ScenarioStorage, ProcessInvoker
    {
    }


}
