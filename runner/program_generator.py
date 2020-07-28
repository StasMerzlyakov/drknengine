# Build the parser
import sys

from language.program_parser import *

class ProgramGenerator:
    def __init__(self):
        pass

    def generate(self, script_path, program_path):
        original_stdout = sys.stdout
        try:
            with open(program_path, 'w') as f:
                sys.stdout = f
                parser = yacc.yacc()

                with open(script_path, "r") as file:
                    data = file.readlines()
                    parser.parse(''.join(data))
        finally:
            sys.stdout = original_stdout

