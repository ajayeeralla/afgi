
from errors import YamlToTclError
import tcl_gen_jg
import tcl_gen_vcf

def tcl_gen(dic):
        """Generate TCL file (for either VCF or JG) from YAML configuration.
            Args:
                dic (dict): A dictionary containing the YAML file content.
            Returns:
                A TCL file generated.

            Examples:
                >>> translate({'task': 'verify', 'tool': 'VC-Formal', 'appmode': 'FPV', 'read_file': {'top': 'top', 'format': 'sv', 'filelist': 'filename'}, 'clock': {'name': 'clk', 'period': '10ns'}, 'reset': {'name': 'rst', 'sense': 'high'}})
                #! /usr/bin/tclsh 
                #Generated on 2020-09-29 15:50:23.765123
                
                set_app_mode FPV
                
                read_file -top top -format sv -sva -vcs "-f filename" -assert svaext -lca
                
                set_clock -name clk -period 10ns
                
                set_reset -name rst -sense high
        """
        tool = dic['tool'] 
        if tool == None:
            raise YamlToTclError.tool_error() 
        if tool == 'VC-Formal':
            return tcl_gen_vcf.tcl_gen(dic, './output')
        elif tool == 'JasperGold':
            return tcl_gen_jg(dic)
        else: 
            raise YamlToTclError.tool_name_error()