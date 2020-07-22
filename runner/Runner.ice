#pragma once

module Runner
{
    sequence<byte> ByteSeq;

    sequence<string> StringSeq;

    struct Wrapper
    {
        ByteSeq wrapperCode;        // python-код обертки ctypes
        ByteSeq nativeLibraryCode;  // код нативной библиотеки
        string nativeLibraryName;          // имя файла, под которым должна быть сохранена нативная библиотека
    }

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

        // Залить пакет в хранилище
        void uploadLibrary(string name, ByteSeq library)
            throws LibraryExistsException, LibraryUploadException;
    }
}
