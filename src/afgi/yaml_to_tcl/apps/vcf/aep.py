#! /usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/apps/vcf/aep.py
""" This module contains "AEP" (derived from FPV) class which is used to generate TCL file for VCF AEP appmode."""
import datetime
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors
from afgi.yaml_to_tcl.utils import Utils
from afgi.yaml_to_tcl.apps.vcf.fpv import FPV

class AEP(FPV):
    """ This class is used to generate TCL file for VCF AEP appmode. It uses the FPV class as a base class."""
    def read_file(self):
        """ This method redifines the read_file method of the FPV class to add the AEP specific options."""
        read_file = self.dic['read_file']

        if read_file == None:
            raise YamlToTclErrorException(self.yaml_exception.read_file_error())
        # Top module
        top_module = read_file['top']
        if top_module == None:
            raise YamlToTclErrorException(self.yaml_exception.read_file_top_error())
        
        format = read_file['format']
        
        # Format of the RTL: sverilog or verilog
        if format == None:
            raise YamlToTclErrorException(self.yaml_exception.read_file_format_error())
        
        # Filelist: list of RTL files
        filelist = read_file['filelist']
        if filelist == None:
            raise YamlToTclErrorException(self.yaml_exception.read_file_filelist_error())
        
        # Tool specivic options
        tool_opts = ""
        if  read_file['app-opts'] != None:
            util = Utils(filelist)
            aep_opts = read_file['app-opts']['aep']
            if aep_opts['aep'] != None:
                tool_opts = tool_opts + " -aep " + util.append_opts(aep_opts['aep'])
            if aep_opts['cov'] != None:
                tool_opts = tool_opts + " -cov " + util.append_opts(aep_opts['cov'])

        other_opts = "-assert svaext -lca"
        tcl_fl = Utils(filelist)
        read_file = "read_file -top "+ str(top_module) + tool_opts +" -format "+str(format)+ " -sva -vcs \"-f " + str(tcl_fl.tcl_filelist())+"\" "+ other_opts +"\n\n"
        self.output_file.writelines(read_file)

    

    