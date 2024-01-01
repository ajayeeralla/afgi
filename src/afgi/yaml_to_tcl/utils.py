#!/usr/bin/env python3
# Path: src/afgi/yaml_to_tcl/utils.py
""" This module contains the Utils class that defines some utility functions.
"""
class Utils ():
    """ This class defines some utility functions.
    """
    def __init__(self, filelist):
        """ The constructor for Utils class.
        """
        self.filelist = filelist
        
    def tcl_filelist(self):
        """Convert a list of files to a TCL filelist.
        Args:
            filelist (list): A list of files.

        Returns:
        filelist (str): A file list in TCL format.
        """
        flist = "{ "
        for file in self.filelist:
            flist = flist + str(file) + " "
        flist = flist + "}"
        return flist
    def append_opts(self, opts):
        """Append options to a string.
        Example:
           1. opts = ["a"]
              append_opts(opts)
              "a"
           2. opts = ["a", "b"]
              append_opts(opts)
              "a+b"           
        """
        res = ""
        if opts != None and len(opts) > 1:
            for idx, opt in enumerate(opts):
                if idx == 0:
                    res = res + str(opt)
                else:
                    res = res + "+" + str(opt)
            return res
        elif opts != None and len(opts) == 1:
            res = res + str(opts[0])
            return res
        else:
            return res
   