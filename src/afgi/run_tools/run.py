""" This module contains the RunTool class which is used to run any tool 
with the given arguments
\b
class RunTool:
    Attributes:
        tool (str): tool name
        script (str): script name
        args (list strings): list of arguments
\b
    Methods:
        get_opts(self): get the options of the tool
        run(self): run formal verification tool on the given script
"""
import os


class RunTool:
    """ RunTool class
    Attributes:
        tool (str): tool name
        script (str): script name
        args (list strings): list of arguments
    """
    def __init__(self, tool, script, args):
        self.tool = tool
        self.script = script
        self.args = args

    def get_opts(self):
       """A method to get the options of the tool
        Args:
              None
        Returns: 
            opts (str): tool options with prefix '-' if not present separated by space  
       """
       opts = ""
       for arg in self.args:
            if arg.startswith('-'):
                opts = opts + ' ' + arg
            else:
                opts = opts + ' ' +'-' + arg
       return opts

    # Run formal verification tool on the given script
    def run(self):
        """ A method to run a tool on the given script with the given arguments
        Args:
            None
        Returns:
            output (str): output of the tool to the console
        """

        # run tool
        return os.system(self.tool + ' ' + self.get_opts() + ' ' + self.script)