#!/usr/bin/env python3
# Path: src/afgi/run_tools/__main__.py
""" This module contains the main function which demonstrates the usability of run_tools package.
Example:
    $ python3 -m afgi.yaml_to_tcl -y <yaml_file> -t <tcl_file>
    $ python3 -m afgi.yaml_to_tcl -y <yaml_file>
    $ python3 -m afgi.yaml_to_tcl -h
"""
def usage():
    print("Welcome to Run run_tools package!\n")
    print("Usage:")
    print("afgi.run_tools [Mandatory] [Optional/Help] parameters")
    print("\n")
    print("Mandatory:")
    print("-c, -command                   Command to run") 
    print("\n")
    print("Optional:")
    print("-s, -script                 Script file to run")
    print("-o, -options               Options to run the command")
    print("\n")
    print("Help:")
    print("-h, --help                   Displays this message")
    print("\n")

def main():
    print("Welcome to Run run_tools package!\n")
    command = ""
    script = ""
    options = []
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('command', help='Command to run')
    parser.add_argument('-s', '--script', type=str, help='Script file to run')
    parser.add_argument('-o', '--options', action= 'append', help='Options to run the command')
    args = parser.parse_args()
    command = command + args.command
    if args.script is not None:
        script = script + args.script
    if args.options is not None:
        options = options + args.options
    run = RunTool(command, script, options)  
    run.run()
    
if __name__ == "__main__":
    from afgi.run_tools.run import RunTool
    main()

