#!/usr/bin/python3

""" 
the interpreter for the airbnb project
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Defines the interpreter for the project """
    def do_quit(self, arg):
        """quit command """
        return True
    
    def do_EOF(self, arg):
        """ quiting using EOF """
        return True
    
    def emptyline(self, arg):
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
