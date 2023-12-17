import os
import datetime
from errors import YamlToTclError




def tcl_gen (input_dic, output_file):
        """Generate TCL file (for VC Formal tool) from YAML configuration.

        Args:
            f (filename): A YAML file containing the configuration for the VC Formal tool.
            output_dir (str): A path to the directory where the TCL file will be generated.

        Returns:
            A path to the output (TCL) file generated.
        """
        basename = os.path.basename(output_file)
        basename_wo_ext = os.path.splitext(basename)[0]
        outfile = output_dir + '/' + basename_wo_ext + '.tcl'

        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
         
        file = open(outfile, 'w+') 

        shebang = "#! /usr/bin/tclsh \n"
        now = "#Generated on "+str(datetime.datetime.now())+"\n\n"
        task = input_dic['task']

        if input_dic['tool'] == None:
            raise YamlToTclError.tool_error()

        app_mode = input_dic['appmode']
        if app_mode == None:
            raise YamlToTclError.appmode_error()
            
        set_app_mode = "set_app_mode "+ app_mode +"\n\n"

        if input_dic['read_file'] == None:
            raise YamlToTclError.read_file_error()
        
        top_module = input_dic['read_file']['top']
        if top_module == None:
            raise YamlToTclError.read_file_top_error()
        
        format = input_dic['read_file']['top']
        
        if format == None:
            raise YamlToTclError.read_file_format_error()
        
        filelist = input_dic['read_file']['filelist']
        if filelist == None:
            raise YamlToTclError.read_file_filelist_error()
        
        other_opts = "-assert svaext -lca"
    
        read_file = "read_file -top "+ str(top_module) + " -format "+str(format)+ " -sva -vcs \"-f " + str(filelist) +"\" "+ other_opts +"\n\n"

        clock = input_dic['clock']

        if clock == None:
            raise YamlToTclError.clock_error()
        
        clock_name = input_dic['clock']['name']
        
        if clock_name == None:
            raise YamlToTclError.clock_name_error()
        
        period = input_dic['clock']['period']
        
        if period == None:
            period = input_dic['clock']['period']

        create_clock = "create_clock -name "+str(clock)+" -period "+str(period)+"\n\n"

        rst = input_dic['reset']['name']
        sense = input_dic['reset']['sense']

        if sense == None:
            sense = input_dic['reset']['sense']
        
        create_reset = "create_reset -name "+str(rst)+" -sense "+str(sense)+"\n\n"
        sim_run = "sim_run -stable \nsim_save_reset \n\n"
        
        check_mode = input_dic['check-mode']
        check_fv = "check_fv " + check_mode + "\n\n"

        outfile.writelines([shebang, now, set_app_mode, read_file, create_clock, create_reset, sim_run, check_fv])
        outfile.close()
        return(outfile)
