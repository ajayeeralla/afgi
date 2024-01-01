#!/usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/tcl_gen_jg.py
"""This module contains a class "TclGenJg" which can be used to generate a TCL file for JG.
    The class takes a dictionary and a file name (for TCL file) as input and generates a TCL file for JG.
"""

class TclGenJg():
    def __init__(self, dic, output_file):
        self.dic = dic
        self.output_file = output_file
        pass