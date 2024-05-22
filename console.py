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

    def do_create(self, args):
        """ contains the create function """ 
        model_args = {
            "BaseModel": BaseModel
        }
        if len(args) < 2:
            print("** class name missing **")
        elif args[2] not in model_args.keys:
            print("** class doesn't exist **")
        else:
            print(eval(modelargs[args[1]]().id))
            storage.save()



if __name__ == '__main__':
    HBNBCommand().cmdloop()
