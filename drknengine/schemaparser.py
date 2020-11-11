#!/usr/bin/env python3

#
# Парсер xml файлов по схеме Drakon.xsd
# позволяет добавлять различные функции для обработки событий распознавания объектов xml
#

from lxml import etree


def __parse_image_size(elem):
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


def __parse_action(elem):
    """
    Функция обработки Action
    :param elem:  Элемент Action
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}Action'
    result = {}

    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}X':
            result['x'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}Y':
            result['y'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisX':
            result['width'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisY':
            result['height'] = int(child.text)
    return result

def __parse_title(elem):
    """
    Функция обработки Title
    :param elem:  Элемент Title
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}Title'
    result = {}

    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}X':
            result['x'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}Y':
            result['y'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisX':
            result['width'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisY':
            result['height'] = int(child.text)
    return result


def __parse_end(elem):
    """
    Функция обработки End
    :param elem:  Элемент End
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}End'
    result = {}

    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}X':
            result['x'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}Y':
            result['y'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisX':
            result['width'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}AxisY':
            result['height'] = int(child.text)
    return result


def __parse_vertical_line(elem):
    """
    Функция обработки VerticalLine
    :param elem:  Элемент VerticalLine
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}VerticalLine'
    result = {}

    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}X':
            result['x'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}Y':
            result['y'] = int(child.text)
        if child.tag == '{http://su.ztech/drakon}Width':
            result['width'] = int(child.text)
    return result


def __parse_elements(elem):
    """
    Функция обработки
    :param elem:  Элемент Elements
    :return:
    """
    assert elem.tag == '{http://su.ztech/drakon}Elements'
    result = []

    # Сначала проходимся по линиям. В результате элементы в svg файле окажутся сверху линий
    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}VerticalLine':
            obj = __parse_vertical_line(child)
            result.append('<line x1="{}" y1="{}" x2="{}" y2="{}" stroke="black" class="line"/>'
                          .format(obj['x'], obj['y'], obj['x'], obj['y'] + obj['width']))


    for child in elem.getchildren():
        if child.tag == '{http://su.ztech/drakon}Action':
            obj = __parse_action(child)
            result.append('<rect x="{}" y="{}" width="{}" height="{}" class="action"/>'
                          .format(obj['x'], obj['y'], obj['width'], obj['height']))

        if child.tag == '{http://su.ztech/drakon}Title':
            obj = __parse_title(child)
            result.append('<rect x="{}" y="{}" width="{}" height="{}" rx="25" ry="25" class="title"/>'
                          .format(obj['x'], obj['y'], obj['width'], obj['height']))

        if child.tag == '{http://su.ztech/drakon}End':
            obj = __parse_end(child)
            result.append('<rect x="{}" y="{}" width="{}" height="{}" rx="15" ry="15" class="title"/>'
                          .format(obj['x'], obj['y'], obj['width'], obj['height']))


        # if child.tag == '{http://su.ztech/drakon}Height':
        #    result['Height'] = child.text + dim
        # if child.tag == '{http://su.ztech/drakon}Width':
        #    result['Width'] = child.text + dim

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
            size_info = __parse_image_size(appt)
            result_list.append('     height="' + size_info['Height'] + '" width="' + size_info['Height'] + '">')

            result_list.append('    <defs>')
            result_list.append('        <style type = "text/css" > <![CDATA[')
            result_list.append('            .action { fill: white; stroke: black; stroke-width: 2 }')
            result_list.append('            .title { fill: white; stroke: black; stroke-width: 2 }')
            result_list.append('            .end { fill: white; stroke: black; stroke-width: 2 }')
            result_list.append('            ]]>')
            result_list.append('        </style>')
            result_list.append('    </defs>')

        if appt.tag == '{http://su.ztech/drakon}Elements':
            elements = __parse_elements(appt)
            [result_list.append('    ' + el) for el in elements]
    result_list.append('</svg>')
    return '\n'.join(result_list)
