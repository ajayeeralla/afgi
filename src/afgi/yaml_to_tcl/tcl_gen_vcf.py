"""Generate TCL file (for VC Formal tool) from YAML configuration.
   The YAML file should contain the following fields:
  # Task name
    task: This task is used to run Formal Verification on the design.

    # Tool name
    tool: VC-Formal

    # Application mode for the Formal tool
    appmode: FPV

    blackbox:
    modules:
        - add.v
        - sub.v
    cells:
        - add0
        - sub0
    
    read_file:
    top: adder
    format: verilog
    filelist: 
        - adder.v
        - adder_tb.v
        - mult.v

    clock:
    name: clk
    period: 10

    reset: 
    name: rst 
    sense: high
    
    check-mode: block


  Examples:
    >>> tcl_gen({'task': 'verify', 'tool': 'VC-Formal', 'appmode': 'FPV', 'read_file': {'top': 'top', 'format': 'sv', 'filelist': 'filename'}, 'clock': {'name': 'clk', 'period': '10ns'}, 'reset': {'name': 'rst', 'sense': 'high'}}) 
    #! /usr/bin/tclsh
    # Generated on 2023-12-18 19:57:42.641326
    # This task is used to run Formal Verification on the design.

    set_app_mode FPV
    
    set_blackbox -designs { add.v sub.v }
    set_blackbox -cells { add0 sub0 }
    read_file -top top -format sv -sva -vcs "-f filename" -assert svaext -lca
    
    create_clock -name clk -period 10
    create_reset -name rst -sense high

    sim_run -stable
    sim_save_reset

    check_fv block
  """

import datetime
from afgi.yaml_to_tcl.errors import YamlToTclErrorException, YamlToTclErrors


def to_tcl_filelist(filelist):
    """Convert a list of files to a TCL filelist.

    Args:
        filelist (list): A list of files.

    Returns:
       filelist (str): A file list in TCL format.
    """
    flist = "{ "
    for file in filelist:
        flist = flist + str(file) + " "
    flist = flist + "}"
    return flist
   
def tcl_vcf (input_dic):
        """Generate TCL file (for VC Formal tool) from dictionary object built from YAML configuration.

        Args:
            input_dic (dict): A dictionary object built from YAML configuration.
           
        Returns:
            filename (str): A TCL file generated.
        """ 
        
        # output file name
    
        filename = 'tcl_for_vcf.tcl'
         
        file = open(filename, 'w+') 

        shebang = "#! /usr/bin/tclsh \n"
        now = "# Generated on "+str(datetime.datetime.now())+"\n"
        task = input_dic['task']

        prelude = shebang + now + "# " + task + "\n\n"

        yaml_exception = YamlToTclErrors()
        # check if appmode is non empty
        app_mode = input_dic['appmode']
        if app_mode == None:
            raise YamlToTclErrorException(yaml_exception.appmode_error())
            
        set_app_mode = "set_app_mode "+ app_mode +"\n\n"

        # check if there are modules to be blackboxed
        blackboxes = ""
        if input_dic['blackbox'] != None:
            modules = input_dic['blackbox']['modules']
            if modules != None:
                blackboxes = blackboxes + "set_blackbox -designs "+str(to_tcl_filelist(modules))+"\n"
            cells = input_dic['blackbox']['cells']
            if cells != None:
                blackboxes = blackboxes + "set_blackbox -cells "+str(to_tcl_filelist(cells))+"\n"           

        # check if read_file is non empty
        read_file = input_dic['read_file']

        if read_file == None:
            raise YamlToTclErrorException(yaml_exception.read_file_error())
        # Top module
        top_module = read_file['top']
        if top_module == None:
            raise YamlToTclErrorException(yaml_exception.read_file_top_error())
        
        format = read_file['format']
        
        # Format of the RTL: sverilog or verilog
        if format == None:
            raise YamlToTclErrorException(yaml_exception.read_file_format_error())
        
        # Filelist: list of RTL files
        filelist = read_file['filelist']
        if filelist == None:
            raise YamlToTclErrorException(yaml_exception.read_file_filelist_error())
        
        other_opts = "-assert svaext -lca"
        
        read_file = "read_file -top "+ str(top_module) + " -format "+str(format)+ " -sva -vcs \"-f " + str(to_tcl_filelist(filelist))+"\" "+ other_opts +"\n\n"

        # check if clock is non empty
        clock = input_dic['clock']

        if clock == None:
            raise YamlToTclErrorException(yaml_exception.clock_error())
        
        clock_name = clock['name']
        
        if clock_name == None:
            raise YamlToTclErrorException(yaml_exception.clock_name_error())
        
        period = clock['period']
        
        if period == None:
            raise YamlToTclErrorException(yaml_exception.clock_period_error())
 
        create_clock = "create_clock -name "+str(clock_name)+" -period "+str(period)+"\n\n"
        # check if reset is non empty
        rst = input_dic['reset']

        if rst == None:
            raise YamlToTclErrorException(yaml_exception.reset_error())

        rst_name = rst['name']

        if rst_name == None:
            raise YamlToTclErrorException(yaml_exception.reset_name_error())
        
        sense = rst['sense']

        if sense == None:
            raise YamlToTclErrorException(yaml_exception.reset_sense_error())
        
        create_reset = "create_reset -name "+str(rst_name)+" -sense "+str(sense)+"\n\n"
        sim_run = "sim_run -stable \nsim_save_reset \n\n"
        
        check_mode = input_dic['check-mode']
        check_fv = "check_fv " + check_mode + "\n\n"

        file.writelines([prelude, set_app_mode, blackboxes, read_file, create_clock, create_reset, sim_run, check_fv])
        file.close()
        return(filename)
