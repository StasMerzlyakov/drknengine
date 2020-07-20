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

    exception WrapperExistsException
    {
    }

    exception WrapperNotExistsException
    {
    }

    exception WrapperUploadException
    {
    }

    interface WrapperStorage
    {
        StringSeq getWrapperList();      // получить список загруженных пакетов
        Wrapper getWrapper(string name) throws WrapperNotExistsException; // выгрузить пакет из хранилища
        void deleteWrapper(string name);        // удалить пакет из хранилища
        void uploadWrapper(string name, Wrapper wrapper) // залить пакет в хранилище
            throws WrapperExistsException, WrapperUploadException;
    }
}
