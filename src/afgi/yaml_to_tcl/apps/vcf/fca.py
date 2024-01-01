#! /usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/apps/vcf/fca.py
""" This module contains "FCA" (derived from FPV) class which is used to generate TCL file for VCF FCA appmode."""
import datetime
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors
from afgi.yaml_to_tcl.utils import Utils
from afgi.yaml_to_tcl.apps.vcf.fpv import FPV

class FCA(FPV):
    """ This class is used to generate TCL file for VCF FCA appmode. It uses the FPV class as a base class."""
    def read_sim_db(self, sim_db, cov_dut):
        """ This method adds commands to read the simulation coverage database."""
        self.output_file.writelines("read_cov_db -cov_input "+sim_db+" -cov_dut "+cov_dut+"\n\n")
      
    def read_file(self):
        """ This method redifines the read_file method of the FPV class to add the FCA specific options."""
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
        cov_opts = read_file['cov-opts']
        if cov_opts == None:
            raise YamlToTclErrorException(self.yaml_exception.read_file_cov_opts_error())   
        util = Utils(filelist)
        cov_opts = " -cov" + util.append_opts(cov_opts)                        
        other_opts = "-assert svaext -lca"
        tcl_fl = Utils(filelist)
        read_file = "read_file -top "+ str(top_module) + cov_opts +" -format "+str(format)+ " -sva -vcs \"-f " + str(tcl_fl.tcl_filelist())+"\" "+ other_opts +"\n\n"
        self.output_file.writelines(read_file)

    def read_cert_fault_db(self, cert_db):
        self.output_file.writelines("read_fault_db -name "+cert_db+"\n")
        self.output_file.writelines("save_fault_db -name "+cert_db+"\n\n")

    