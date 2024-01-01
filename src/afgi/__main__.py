#!/usr/bin/env python3
# Path: src/afgi/__main__.py
""" This module is used to run the AFGI tool.
Example:
    1. afgi -g
    2. afgi -b -y <yaml_file> -o <output_file> --vcf
    3. afgi -b -t <tcl_file> --jg
"""

# usage manual
def usage():
    print("Welcome to AFGI: Augmented Formal Graphical Interface!\n")
    print("Usage:")
    print("afgi [Optional] Mandatory parameters")
    print("\n")
    print("Mandatory:")
    print("-g, --gui                   GUI mode")
    print("-b, --batch                 Batch mode")
    print("-y, --yaml                  YAML file")
    print("-o, --output                Output TCL file")
    print("-t, --tcl                   TCL file")
    print("--vcf                        VCF tool")
    print("--jg                         JasperGold tool")
    print("\n")

# main function
def main():
    """ This function is used to run the AFGI tool."""
    try:
        opts, args = getopt.getopt(sys.argv[1:], "y:t:hbgo:", ["vcf", "jg", "yaml=", "tcl=", "gui", "batch", "help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    tool = ""
    out_file = ""
    tcl_file = ""
    for o, a in opts:
        if o in ("-g", "--gui"):
         app = wx.App()
         fr = frame.MyFrame(parent=None, title='AFGI')
         fr.Show()
         app.MainLoop()
        elif o in ("-b", "--batch"):
         new_opts = [(x, _) for (x, _) in opts if x not in ("-b", "--batch")]
         tmp_opts = []
         for o, a in new_opts:
            if o in ("-y", "--yaml"):
             yaml_file = a
             tmp_opts = [(x, _) for (x, _) in new_opts if x not in ("-y", "--yaml")]
             for o, a in tmp_opts:
                if o in ("-o", "--output"):
                    out_file += a
                    import afgi.yaml_to_tcl.tcl_gen as TclGen 
                    TclGen.TclGen(yaml_file, out_file)
                    opts = [(x, _) for (x, _) in tmp_opts if x not in ("-o", "--output")]
                elif o in ("-t", "--tcl"):
                    tcl_file += a
                    opts = [(x, _) for (x, _) in tmp_opts if x not in ("-t", "--tcl")]
                else: 
                   pass
         for o, a in opts:
          if o in ("--vcf"):
           tool += "vcf"
          elif o in ("--jg"):
           tool += "jg"
          else: 
           print("Unknown tool")
         import afgi.run_tools.run as RunTool
         tool = "cat"
         run_obj = RunTool.RunTool(tool, out_file, [])
         print(run_obj.run())           
        else:
           pass
if __name__ == "__main__":
    from afgi.gui import frame
    import wx
    import getopt, sys
    main()

