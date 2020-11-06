#!/usr/bin/env python3

#
# Парсер xml файлов по схеме Drakon.xsd
# позволяет добавлять различные функции для обработки событий распознавания объектов xml
#

from lxml import etree


def __parse_ImageSize(elem):
    """
    Функция обработки
    :param elem:  Элемент ImageSize
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}ImageSize'
    result = {}

    # размерность
    dim = 'px'
    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}Dimension':
            dim = child.text
        if child.tag == '{http://su.ztech/drakon}Height':
            result['Height'] = child.text + dim
        if child.tag == '{http://su.ztech/drakon}Width':
            result['Width'] = child.text + dim

    return result


def generate_view(xml):
    """
    Функция генерации SVG изображения по xml, созданному по схеме Drakon.xsd
    :param xml: строка с xml
    :return: кусок кода, представляющий собой http страницу
    """
    result_list = list()
    result_list.append('<?xml version="1.0" encoding="UTF-8" standalone="no"?>')
    result_list.append('<svg version = "1.1" ')
    result_list.append('     xmlns="http://www.w3.org/2000/svg"')
    root = etree.fromstring(xml)

    for appt in root.getchildren():
        if appt.tag == '{http://su.ztech/drakon}ImageSize':
            size_info = __parse_ImageSize(appt)
            result_list.append('     height="' + size_info['Height'] + '" width="' + size_info['Height'] + '">')

    result_list.append('</svg>')
    return '\n'.join(result_list)
