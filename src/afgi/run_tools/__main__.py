"""
This module is the main entry point for the run_fv_tools package.
Example:
    $ python -m afgi.run_fv_tools
    
"""

import run
def main():
    """ Main entry point for the run_fv_tools package
    Args:
        None
    Returns:
        Output of the tool to the console
    """
    run_obj = run.RunTool("ls", "", ['a', 'l'])
    print(run_obj.run())

if __name__ == "__main__":
    main()