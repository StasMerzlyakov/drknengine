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
            throws ScenarioExistsException, ScenarioUploadException;

        // Получить визуальное представление DRAKON-схемы
        ByteSeq getScenarioView(string name) throws ScenarioNotExistsException;

    }

    interface RunnerService extends LibraryStorage, ScenarioStorage
    {
    }


}
