# Build the parser
import sys

from language.prm_parser import *

class PrmGenerator:
    def __init__(self):
        pass

    def generate(self, script_path, view_file_path):
        original_stdout = sys.stdout
        try:
            with open(view_file_path, 'w') as f:
                sys.stdout = f
                parser = yacc.yacc()

                with open(script_path, "r") as file:
                    data = file.readlines()
                    parser.parse(''.join(data))
        finally:
            sys.stdout = original_stdout

