"""This module contains functions to load a YAML file 
and check if it is valid.
Examples:
    $ python load_yaml.py <input_file>
"""
import yaml
import tcl_gen
import os
from errors import YamlToTclError

def load_yaml_file(input_file):
    """Check if a YAML file is valid.
    
    Args:
        input_file (str): A path to the YAML file to be loaded.

    Returns:
        A dictionary containing the YAML file content.

    Examples:
        >>> load_yaml_file('example.yaml')
        {'task: blah', 'tool': 'VC-Formal', 'appmode': 'FPV', 'task': 'verify', 'read_file': {'top': 'top', 'format': 'sv', 'filelist': 'filename'}, 'clock': {'name': 'clk', 'period': '10ns'}, 'reset': {'name': 'rst', 'sense': 'high'}}
    """
    # Check if file exists
    if not os.path.isfile(input_file):
        raise FileNotFoundError(f'File {input_file} not found.')
    
    # Check if file is empty
    if os.stat(input_file).st_size == 0:
        raise YamlToTclError.empty_yaml_error()

    # Check if file is a valid YAML file
    try:
        with open(input_file, 'r') as stream:
           dic = yaml.safe_load(stream)
           return tcl_gen.tcl_gen(dic)
    except yaml.YAMLError as exc:
        print(exc)


# if __name__ == "__main__":
#     import sys
#     print(load_yaml_file(sys.argv[1]))



