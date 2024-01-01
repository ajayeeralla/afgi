#!/usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/apps/vcf/fpv.py
""" This module contains the main function which demonstrates the usage of yaml_to_tcl package.
Example:
    $ python3 -m afgi.yaml_to_tcl -y <yaml_file> -t <tcl_file>
    $ python3 -m afgi.yaml_to_tcl -y <yaml_file>
    $ python3 -m afgi.yaml_to_tcl -h
"""
def usage():
    print("Welcome to Yamltotcl: YAML to TCL converter!\n")
    print("Usage:")
    print("afgi.yaml_to_tcl [Mandatory] [Optional/Help] parameters")
    print("\n")
    print("Mandatory:")
    print("-t, --tcl                   TCL file") 
    print("\n")
    print("Optional:")
    print("-y, --yaml                  YAML file")
    print("\n")
    print("Help:")
    print("-h, --help                   Displays this message")
    print("\n")

def main():
    print("Welcome to Yamltotcl: YAML to TCL converter!\n")
    try:
        opts, args = getopt.getopt(sys.argv[1:], "y:t:h", ["help", "yaml=", "tcl="])
        if len(opts) == 0:
            usage()
            sys.exit()
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    yaml_file = None
    dirname = os.getcwd()
    print("Current working directory: " + dirname)
    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-t", "--tcl"):
            output = dirname + '/' + a
        elif o in ("-y", "--yaml"):
            yaml_file = dirname + '/' + a
        else:
            assert False, "unhandled option"
            usage()
    if yaml_file == None:
        usage()
        sys.exit()
    if output == None:
        """ If output file is not specified, then the output file will be the same as the input file with .tcl extension."""
        output = dirname + '/' + yaml_file.split('/')[-1].split('.')[0] + '.tcl'
    import afgi.yaml_to_tcl.tcl_gen as TclGen
    TclGen.TclGen(yaml_file, output)

if __name__ == "__main__":
    from afgi.yaml_to_tcl import TclGen
    import getopt, sys, os
    main()

