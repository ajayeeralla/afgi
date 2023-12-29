import datetime
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors
from afgi.yaml_to_tcl.apps.vcf.fpv import FPV
from afgi.yaml_to_tcl.apps.vcf.aep import AEP
from afgi.yaml_to_tcl.apps.vcf.frv import FRV
import yaml
import os


class TclGenVcf():
    
        def __init__(self, dic, out_file):  
            self.dic = dic
            self.out_file = out_file
            self.yaml_exception = YamlToTclErrors()
        # output file name
            file = open(self.out_file, 'w+') 
            self.out_file = file
            self.prelude()
        # check if appmode is non empty
            app_mode = self.dic['appmode']
            if app_mode == None:
                raise YamlToTclErrorException(self.yaml_exception.appmode_error())
            set_app_mode = "set_app_mode "+ app_mode +"\n\n"
            self.out_file.writelines(set_app_mode)
            if app_mode == "FPV":
                fpv = FPV(self.dic, self.out_file)
                fpv.set_vars()
                fpv.blackbox()
                fpv.read_file()
                fpv.clock()
                fpv.reset()
            elif app_mode == "AEP":
                aep = AEP(self.dic, self.out_file)
                aep.set_vars()
                aep.blackbox()
                aep.read_file()
                aep.clock()
                aep.reset()
            elif app_mode == "FRV":
                frv = FRV(self.dic, self.out_file)
                frv.set_vars()
                frv.blackbox()
                frv.frv_load()
                frv.read_file()
                frv.clock()
                frv.reset()
            else:
                 raise YamlToTclErrorException(self.yaml_exception.appmode_error())
            self.check_fv()
            self.out_file.close()
            print('The TCL file {} generated!!'.format(self.out_file.name))
            
        
        def prelude(self):
            shebang = "#! /usr/bin/tclsh \n"
            now = "# Generated for VCF on "+str(datetime.datetime.now())+"\n"
            task = self.dic['task']
            prelude = shebang + now + "# " + task + "\n\n"
            self.out_file.writelines(prelude)
        
        def check_fv(self):
            check_mode = self.dic['check-mode']
            check_fv = "check_fv " + check_mode + "\n\n"
            self.out_file.writelines(check_fv)
        
        