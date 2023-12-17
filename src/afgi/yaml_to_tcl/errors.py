""" This module contains the custom errors for the yaml-to-tcl package. """

class YamlToTclError(Exception):
    """Base class for exceptions in this module."""
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def empty_yaml_error (self):
        return "Empty Yaml file passed!!"
    
    def invalid_yaml_error (self):
        return "Invalid YAML file passed!!"
    
    def tool_error (self):
        return "Tool value None!"
    
    def tool_name_error (self):
        return "Unsupported tool name!"
    
    def appmode_error (self):
        return "Tool appmode value None!"
    
    def read_file_error(self):
        return "read_file value None!"
    
    def read_file_top_error (self):
        return "RTL top module value None!"

    def read_file_format_error (self):
        return "RTL format value None!"
    
    def read_file_filelist_error (self):
        return "RTL filelist value None!"
    
    def clock_error (self):
        return "Clock value None!"
    
    def clock_name_error (self):
        return "Clock name value None!"
    
    def clock_period_error (self):
        return "Clock period value None!"
    
    def reset_error (self):
        return "Reset value None!"
    
    def reset_name_error (self):
        return "Reset name value None!"
    
    def reset_sense_error (self):
        return "Reset sense value None!"
    