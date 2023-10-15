#!/usr/bin/python3
""" Console class to run code in cmd module """
import cmd
from models import storage
import re


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand is a command-line interface for managing instances of various
    classes in a hypothetical system.

    Available Commands:
    - create: Create a new instance of a class.
    - show: Display information about a specific instance.
    - destroy: Remove a specific instance.
    - all: List all instances of a specific class or all classes.
    - count: Count the number of instances of a specific class.
    - update: Update attributes of a specific instance.

    Usage: Run the script and use the above commands to interact the system.
    """
    prompt = "(hbnb) "

    classes = ["BaseModel",
               "User",
               "State",
               "City",
               "Place",
               "Amenity",
               "Review"]

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def do_quit(self, args):
        """
        Quit the program.
        """
        return True

    def do_EOF(self, args):
        """
        End of file (Ctrl+D).
        """
        print("")
        return True

    def default(self, args):
        """
        Default behavior for cmd module when input is invalid.
        """
        arg_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        match = re.search(r"\.", args)
        if match is not None:
            arg_list = [args[:match.span()[0]], args[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_list[1])
            if match is not None:
                command = [arg_list[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in arg_dict.keys():
                    call = "{} {}".format(arg_list[0], command[1])
                    return arg_dict[command[0]](call)
        print("*** Unknown syntax: {}".format(args))
        return False

    def do_create(self, args):
        """
        Create a new instance of a class.
        Usage: create <class_name>
        """
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_list[0])().id)
            storage.save()

    def do_show(self, args):
        """
        Display information about a specific instance.
        Usage: show <class_name> <instance_id>
        """
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print('** instance id missing **')
        else:
            objdict = storage.all()
            id_number = args_list[1].strip('"\'')
            if f"{args_list[0]}.{id_number}" in objdict:
                print(objdict[f"{args_list[0]}.{id_number}"])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        """
        Remove a specific instance.
        Usage: destroy <class_name> <instance_id>
        """
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print('** instance id missing **')
        else:
            objdict = storage.all()
            id_number = args_list[1].strip('"\'')
            if f"{args_list[0]}.{id_number}" in objdict:
                del objdict[f"{args_list[0]}.{id_number}"]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
        """
        List all instances of a specific class or all classes.
        Usage: all [class_name]
        """
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            objdict = storage.all()
            all_instances = []
            for k, v in objdict.items():
                split_list = k.split('.')
                if args_list[0] in split_list:
                    all_instances.append(str(v))
            if len(objdict) == 0:
                print('** no instance found **')
            else:
                print(all_instances)

    def do_count(self, args):
        """
        Count the number of instances of a specific class.
        Usage: count <class_name>
        """
        args_list = args.split()
        count = 0
        objdict = storage.all()
        for k, v in objdict.items():
            split_list = k.split('.')
            if args_list[0] in split_list:
                count += 1
        print(count)

    def do_update(self, args):
        """
        Update attributes of a specific instance.
        Usage: update <class_name> <instance_id> <attribute_name>
        "<attribute_value>"
        """
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print('** instance id missing **')
        elif len(args_list) < 3:
            print('** attribute name missing **')
        elif len(args_list) < 4:
            print("** value missing **")
        else:
            objdict = storage.all()
            ar1 = args_list[1].strip("'\"")
            obj_key = args_list[0].strip("'\"") + '.' + ar1
            obj_key = obj_key.strip(',""')[:-1]
            print(obj_key)

            if obj_key in objdict:
                obj = objdict[obj_key]
                attr_name = args_list[2].strip("'\"")[:-2]
                attr_value = args_list[3].strip("'\"")
                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
