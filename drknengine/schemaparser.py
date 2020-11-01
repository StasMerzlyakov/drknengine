#!/usr/bin/env python3

#
# Парсер xml файлов по схеме Drakon.xsd
# позволяет добавлять различные функции для обработки событий распознавания объектов xml
#

from lxml import etree


def parse_xml(xmlfile):
    """
    Парсинг XML
    """
    with open(xmlfile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)

    for appt in root.getchildren():
        for elem in appt.getchildren():
            if not elem.text:
                text = "None"
            else:
                text = elem.text

            print(elem.tag + " => " + text)


