#!/usr/bin/python3

"""
the interpreter for the airbnb project
"""

import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review

model_args = {
    "BaseModel": BaseModel,
    "User": User,
    "Amenity": Amenity,
    "Review": Review,
    "City": City,
    "State": State,
    "Place": Place
}

func_s = ["all", "destroy", "show", "count", "update"]


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    """Defines the interpreter for the project """
    def do_quit(self, arg):
        """quit command """
        return True

    def do_EOF(self, arg):
        """ quiting using EOF """
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ contains the create function """
        args = arg.split(' ')
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in model_args.keys():
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """shows the string representation of a model """
        args = []
        if arg != "":
            args = arg.split(" ")
        objects = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in model_args.keys():
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects.keys():
            print("** no instance found **")
        else:
            print(objects["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """ destroys an object """
        args = []
        if arg != "" or arg != ' ':
            args = arg.split(' ')
        print(args)   
        objects = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif args[0] not in model_args.keys():
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        else:
            del objects["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """ shows all instances if no class is specified
        but shows only instances of the specified class if one is specified
        """
        objects = storage.all()
        args = []
        if arg != "":
            args = arg.split(' ')
        print(args)
        if len(args) > 0 and args[0] not in model_args.keys():
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in objects.values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        args = []
        if arg != "":
            args = arg.split(' ')
        objects = storage.all()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) == 2:
            print("** instance id missing **")
        elif args[0] not in model_args.keys():
            print("** class doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in objects:
            print("** no instance found **")
        elif len(args) == 3:
            print("** attribute name missing **")
        elif len(args) == 4:
            print("** value missing **")
        else:
            obj = objects["{}.{}".format(args[0], args[1])]
            obj.__dict__[args[2]] = args[3]
            storage.save()
    
    def do_count(self, arg):
        
        """ counts instances of a class
        """
        count = 0
        objects = storage.all()
        args = []
        if arg != "":
            args = arg.split(' ')
        if len(args) == 0:
            print("** no class name **")
        if len(args) > 0 and args[0] not in model_args.keys():
            print("** class doesn't exist **")
        else:
            for obj in objects.values():
                if args[0] == obj.__class__.__name__:
                    count += 1
            print(count)

    def default(self, arg):
        pattern = "\w+\.\w+\(.*?\)"
        if  not re.match(pattern, arg):
            print("no format")
            return
        a = len(arg)
        class_name = ""
        point = 0
        for i in range(a-1):
            point +=1
            if arg[i] == ".":
                break
            else:
                class_name = class_name + arg[i]
        if class_name not in model_args.keys():
            print("class not found")
        func_name = ""
        for i in range(point, a):
            point +=1
            if arg[i] == '(':
                break
            else:
                func_name += arg[i]
        args = ""
        for i in range (point + 1, a-2):
            point +=1
            args += arg[i]
        if args == '':
            args += class_name
        else:
            args = class_name + " " + args
        print(args)
        eval("self.do_{}(\"{}\")".format(func_name, args))
        


if __name__ == '__main__':
    HBNBCommand().cmdloop()
