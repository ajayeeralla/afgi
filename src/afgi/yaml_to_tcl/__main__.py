
# import load_yaml
import tcl_gen

def main():
    """Main function for the yaml_to_tcl package.
    
    Examples:
        $ python3 -m yaml_to_tcl <input_file>
    
    """
    # Read the YAML file
    # Translate the YAML file to TCL
    tcl = tcl_gen.tcl_gen(sys.argv[1])
    
    # Print the TCL file
    print(tcl)


if __name__ == "__main__":
    import sys
    main()