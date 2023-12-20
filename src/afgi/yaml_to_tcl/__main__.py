
"""yaml_to_tcl.__main__: executed when yaml_to_tcl directory is called 
as script."""

def main():
    """Main function for the yaml_to_tcl package.
    
    Examples:
        $ python3 -m yaml_to_tcl <input_file>
    
    """
    # Read the YAML file
    # Translate the YAML file to TCL
    tcl = tcl_gen(sys.argv[1])
    
    # Print the TCL file
    print(tcl)


if __name__ == "__main__":
    import sys
    from yaml_to_tcl.tcl_gen import tcl_gen
    main()