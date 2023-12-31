#!/usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/tcl_gen.py
""" This module contains the TclGen class that generates TCL files from YAML files.
"""
import os
from afgi.yaml_to_tcl.tcl_gen_jg import TclGenJg
from afgi.yaml_to_tcl.tcl_gen_vcf import TclGenVcf
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors 
import yaml

# TclGen class
class TclGen():
    """ This class is used to generate TCL files from YAML files. """
    def __init__(self, in_file, out_file):
        """ The constructor for TclGen class.
        """
        self.in_file = in_file
        self.out_file = out_file
        self.dic = self.load_yaml_file(self.in_file)
        print('The tool is: ', self.dic['tool'])
        if self.dic['tool'] == "VC-Formal":
                TclGenVcf(self.dic, self.out_file)
        elif self.dic['tool'] == "JasperGold":
                TclGenJg(self.dic, self.out_file)
        else:
            self.yaml_exception = YamlToTclErrors()
            raise YamlToTclErrorException(self.yaml_exception.tool_error())
        
    def load_yaml_file(self, input_file):
            """ This method is used to load the YAML file into a python object.
            """
            # Check if file exists
            if not os.path.isfile(input_file):
                raise FileNotFoundError(f'File {input_file} not found.')
            # Check if file is empty
            if os.stat(input_file).st_size == 0:
                raise YamlToTclErrorException(self.yaml_exception.empty_yaml_error())
            # Check if file is a valid YAML file
            try:
                with open(input_file, 'r') as stream:
                    dic = yaml.safe_load(stream)
                return dic
            except yaml.YAMLError as exc:
                print(exc)
