
import load_yaml
import tcl_gen

def main():
    """Main function for the yaml_to_tcl package.
    
    Examples:
    
    
    """
    # Read the YAML file
    dic = load_yaml.load_yaml_file(sys.argv[1])
    
    # Translate the YAML file to TCL
    tcl = tcl_gen.tcl_gen(dic)
    
    # Print the TCL file
    print(tcl)


if __name__ == "__main__":
    import sys
    main()