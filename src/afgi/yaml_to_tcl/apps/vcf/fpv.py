
import datetime
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors
from afgi.yaml_to_tcl.utils import Utils

class FPV():
    def __init__(self, dic, file):
        self.dic = dic
        self.output_file = file
        self.yaml_exception = YamlToTclErrors()

    def set_vars(self):
        vars = self.dic['vars']
        for var in vars:
            set_var = "set_app_var "+str(var)+" true\n"
            self.output_file.writelines(set_var)
        self.output_file.writelines("\n")
        
    def blackbox(self):
        blackboxes = ""
        if self.dic['blackbox'] != None:
            modules = self.dic['blackbox']['modules']
            tcl_fl = Utils(modules)
            if modules != None:
                blackboxes = blackboxes + "set_blackbox -designs "+str(tcl_fl.tcl_filelist())+"\n"
            cells = self.dic['blackbox']['cells']
            if cells != None:
                blackboxes = blackboxes + "set_blackbox -cells "+str(tcl_fl.tcl_filelist())+"\n\n"           
        self.output_file.writelines(blackboxes) 
    
    def read_file(self):
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
        
        other_opts = "-assert svaext -lca"
        tcl_fl = Utils(filelist)
        read_file = "read_file -top "+ str(top_module) + " -format "+str(format)+ " -sva -vcs \"-f " + str(tcl_fl.tcl_filelist())+"\" "+ other_opts +"\n\n"
        self.output_file.writelines(read_file)
    
    def clock(self):
        clock = self.dic['clock']

        if clock == None:
            raise YamlToTclErrorException(self.yaml_exception.clock_error())
        
        clock_name = clock['name']
        
        if clock_name == None:
            raise YamlToTclErrorException(self.yaml_exception.clock_name_error())
        
        clock_period = clock['period']
        
        if clock_period == None:
            raise YamlToTclErrorException(self.yaml_exception.clock_period_error())
        
        set_clock = "set_clock -name "+str(clock_name)+" -period "+str(clock_period)+"\n\n"
        self.output_file.writelines(set_clock)
    
    def reset(self):
        rst = self.dic['reset']

        if rst == None:
            raise YamlToTclErrorException(self.yaml_exception.reset_error())

        rst_name = rst['name']

        if rst_name == None:
            raise YamlToTclErrorException(self.yaml_exception.reset_name_error())
        
        rst_sense = rst['sense']

        if rst_sense == None:
            raise YamlToTclErrorException(self.yaml_exception.reset_sense_error())
        
        set_reset = "set_reset -name "+str(rst_name)+" -sense "+str(rst_sense)+"\n\n"
      

    