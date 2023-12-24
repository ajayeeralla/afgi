class Utils ():
    def __init__(self, filelist):
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
   