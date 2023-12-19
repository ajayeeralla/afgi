""" This module contains the custom errors for the yaml-to-tcl package. 
Examples:
    $ python3 errors.py

Exports: 
    classes: YamlToTclErrorException, YamlToTclErrors
"""

class YamlToTclErrorException(Exception):
    """A class to define the custom exception for the yaml-to-tcl package. 
    This class inherits from the Exception class.
    
    Attributes:
        message (str): The error message.
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class YamlToTclErrors:
   """A class to define the custom errors for the yaml-to-tcl package.
   
   Attributes:
       None
       
    Methods:
        empty_yaml_error: A method to define the error message for empty yaml file.
        invalid_yaml_error: A method to define the error message for invalid yaml file.
        tool_error: A method to define the error message for invalid tool name.
        tool_name_error: A method to define the error message for invalid tool name.
        appmode_error: A method to define the error message for invalid appmode name.
        read_file_error: A method to define the error message for invalid read_file name.
        read_file_top_error: A method to define the error message for invalid top module name.
        read_file_format_error: A method to define the error message for invalid RTL format.
        read_file_filelist_error: A method to define the error message for invalid RTL filelist.
        clock_error: A method to define the error message for invalid clock name.
        clock_name_error: A method to define the error message for invalid clock name.
        clock_period_error: A method to define the error message for invalid clock period.
        reset_error: A method to define the error message for invalid reset name.
        reset_name_error: A method to define the error message for invalid reset name.
        reset_sense_error: A method to define the error message for invalid reset sense.
    """
   def __init__(self):
       """Constructor for the YamlToTclErrors class."""
       pass
   def empty_yaml_error (self):
        """ A method to define the error message for empty yaml file."""
        return "Empty Yaml file passed!!"
   
   def invalid_yaml_error (self):
        """ A method to define the error message for invalid yaml file."""
        return "Invalid YAML file passed!!"
   
   def tool_error (self):
        """ A method to define the error message for invalid tool name."""
        return "Tool value None!"
   
   def tool_name_error (self):
        """ A method to define the error message for invalid tool name."""
        return "Unsupported tool name!"
   
   def appmode_error(self):
        """ A method to define the error message for invalid appmode name."""
        return "Tool appmode value None!"
   
   def read_file_error(self):
        """ A method to define the error message for invalid read_file name."""
        return "read_file value None!"
   
   def read_file_top_error (self):
        """ A method to define the error message for invalid top module name."""
        return "RTL top module value None!"
   
   def read_file_format_error (self):
        """ A method to define the error message for invalid RTL format."""
        return "RTL format value None!"
   
   def read_file_filelist_error (self):
        """ A method to define the error message for invalid RTL filelist."""
        return "RTL filelist value None!"
   
   def clock_error (self):
        """ A method to define the error message for invalid clock name."""
        return "Clock value None!"
   
   def clock_name_error (self):
        """ A method to define the error message for invalid clock name."""
        return "Clock name value None!"
   
   def clock_period_error (self):
        """ A method to define the error message for invalid clock period."""
        return "Clock period value None!"
   
   def reset_error (self):
        """ A method to define the error message for invalid reset name."""
        return "Reset value None!"
   
   def reset_name_error (self):
        """ A method to define the error message for invalid reset name."""
        return "Reset name value None!"
   
   def reset_sense_error (self):
        """ A method to define the error message for invalid reset sense."""
        return "Reset sense value None!"
    