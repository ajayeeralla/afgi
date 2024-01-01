#!/usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/apps/vcf/frv.py
""" This module is used to generate TCL file for VCF FRV appmode.
"""
from afgi.yaml_to_tcl.apps.vcf.fpv import FPV
class FRV(FPV):
    """ This class is used to generate TCL file for VCF FRV appmode. It uses the FPV class as a base class."""
    def frv_load(self):
        """ This method is used to load the IP-XACT file.
        """
        ipxact_file = self.dic['ipxact']
        self.output_file.writelines("frv_load -ipxact "+ipxact_file+" -auto_load\n\n")

