#!/usr/bin/env python3

import unittest
import os

from drknengine import schemaparser


class SchemaParserTestSuite(unittest.TestCase):
    """Advanced test cases."""

    def test_generate_view_1(self):
        xml_path = os.path.join(os.path.dirname(__file__), 'test_files/file_1.xml')
        with open(xml_path, 'rb') as xml_file:
            input_xml = xml_file.read()
        output_xml = schemaparser.generate_view(input_xml)
        self.assertIsNotNone(output_xml)
        result_path = os.path.join(os.path.dirname(__file__), '../svg.xml')

        with open(result_path, 'w') as result_file:
            result_file.write(output_xml)

