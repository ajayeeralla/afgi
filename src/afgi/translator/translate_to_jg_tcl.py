
def translate(f):
    # with open(f'{filename}.yaml','r') as f:
        file = open("jg.tcl", "w+")
        l1 = "#! /usr/bin/tclsh"
        l2 = "set_app_mode "+f['appmode']['value']
        file.writelines(l1)
        file.close()
        return(file)
