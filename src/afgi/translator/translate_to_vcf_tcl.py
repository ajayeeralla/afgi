import os


def translate(f):
        path = 'C:\\Users\\aeeralla\\Documents\\Formal-Assist\\files\\tcl'
        if not os.path.exists(path):
            os.makedirs(path)
        filename = 'vcf.tcl'
        path=os.path.join(path, filename)
        file = open(path, 'w+') 
        
        shebang = "#! /usr/bin/tclsh \n\n"
        
        app_mode = f['appmode']['value']
        if app_mode == None:
            app_mode = f['appmode']['default']
        set_app_mode = "set_app_mode "+ app_mode +"\n\n"

        design = f['read_file']['top']
        format = f['read_file']['top']
        filelist = f['read_file']['filelist']
        other_opts = "-assert svaext -lca"
        
        read_file = "read_file -top "+ str(design) + " -format "+str(format)+ " -sva -vcs \"-f " + str(filelist) +"\" "+ other_opts +"\n\n"

        clock = f['clock']['name']
        period = f['clock']['period']['value']
        if period == None:
            period = f['clock']['period']['default']
        create_clock = "create_clock -name "+str(clock)+" -period "+str(period)+"\n\n"

        rst = f['reset']['name']
        sense = f['reset']['sense']['value']
        if sense == None:
            sense = f['reset']['sense']['default']
        create_reset = "create_reset -name "+str(rst)+" -sense "+str(sense)+"\n\n"

        sim_run = "sim_run -stable \nsim_save_reset \n\n"
        
        check_mode = f['check-mode']['value']
        if check_mode == None:
            check_fv = "check_fv"
        else: 
            check_fv = "check_fv -block"

        file.writelines([shebang, set_app_mode, read_file, create_clock, create_reset, sim_run, check_fv])
        file.close()
        return(path)
