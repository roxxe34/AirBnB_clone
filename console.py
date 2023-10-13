import cmd
import json

from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import FileStorage
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    classes = ["BaseModel", "User"]

    def do_quit(self, args):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, args):
        """end of file"""
        return True

    def do_create(self, args):
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            print(eval(args_list[0])().id)
            storage.save()

    def do_show(self, args):
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print('** instance id missing **')
        else:
            objdict = storage.all()
            id_number = args_list[1]
            if f"{args_list[0]}.{id_number}" in objdict:
                print(objdict[f"{args_list[0]}.{id_number}"])
            else:
                print('** no instance found **')

    def do_destroy(self, args):
        args_list = args.split()
        if len(args_list) < 1:
            print('** class name missing **')
        elif args_list[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args_list) < 2:
            print('** instance id missing **')
        else:
            objdict = storage.all()
            id_number = args_list[1]
            if f"{args_list[0]}.{id_number}" in objdict:
                del objdict[f"{args_list[0]}.{id_number}"]
                storage.save()
            else:
                print('** no instance found **')

    def do_all(self, args):
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

    def do_update(self, args):
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
            obj_key = args_list[0] + '.' + args_list[1]  # Assuming the format is "ClassName.InstanceID"

            if obj_key in objdict:
                obj = objdict[obj_key]
                attr_name = args_list[2]
                attr_value = args_list[3]

                setattr(obj, attr_name, attr_value)
                storage.save()
            else:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
