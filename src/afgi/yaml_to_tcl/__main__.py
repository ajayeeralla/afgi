def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:v", ["help", "output="])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)  # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    output = None
    verbose = False
    for o, a in opts:
        if o == "-v":
            verbose = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-o", "--output"):
            output = a
        else:
            assert False, "unhandled option"
    # ...

if __name__ == "__main__":
    from afgi.gui import my_frame
    import wx
    import getopt, sys
    main()

def usage():
    print("Welcome to AFGI: Augmented Formal Graphical Interface!\n")
    print("Usage:")
    print("afgi [Optional] Mandatory parameters")
    print("\n")
    print("Mandatory:")
    print("-t, --tcl                   TCL file") 
    print("-c, --config                 Configuration required to locate (or generate) formal-friendly filelist")
    print("-m, --module                 Top module name of the design")
    print("-l, --link                   VLNV link of the design")
    print("-b, --bind_file              Bind file for binding DUT with a bus wrapper, generic, AXI, APB, or AHB")
    print("-v, --view                   View name for bootenv") 
    print("\n")
    print("Optional:")
    print("-h, --help                   Displays this message")
    print("-t, --test                   Formal test name")
    print("-V, --Version                Output version information")