from errors import YamlToTclErrors, YamlToTclErrorException
import os
import tcl_gen_jg
import tcl_gen_vcf
import yaml


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
        yaml_exception = YamlToTclErrors()
        raise YamlToTclErrorException(yaml_exception.empty_yaml_error())

    # Check if file is a valid YAML file
    try:
        with open(input_file, 'r') as stream:
           dic = yaml.safe_load(stream)
           return dic
    except yaml.YAMLError as exc:
        print(exc)

def tcl_gen(input_file):
        """Generate TCL file (for either VCF or JG) from YAML configuration.
            Args:
                input_file :  A YAML file containing the configuration for either the VC Formal tool or the JasperGold tool.    
            Returns:
                A TCL file generated.

            Examples:
                >>> translate({'task': 'verify', 'tool': 'VC-Formal', 'appmode': 'FPV', 'read_file': {'top': 'top', 'format': 'sv', 'filelist': 'filename'}, 'clock': {'name': 'clk', 'period': '10ns'}, 'reset': {'name': 'rst', 'sense': 'high'}})
                #! /usr/bin/tclsh 
                # Generated on 2023-08-01 12:00:00.000000
                # verify
                set_app_mode FPV
                
                read_file -top top -format sv -sva -vcs "-f filename" -assert svaext -lca
                
                set_clock -name clk -period 10ns
                
                set_reset -name rst -sense high
        """
        dic = load_yaml_file(input_file)
        tool = dic['tool'] 
        yaml_exception = YamlToTclErrors()

        if tool == None:
            raise YamlToTclErrorException(yaml_exception.tool_error())
        if tool == 'VC-Formal':
            return tcl_gen_vcf.tcl_gen(dic)
        elif tool == 'JasperGold':
            return tcl_gen_jg(dic)
        else: 
            raise YamlToTclErrorException(yaml_exception.tool_name_error())