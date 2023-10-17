#!/usr/bin/python3
"""
Contains a class for command interpreter
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    Class containing entry point
    of command interpreter
    """
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Quit command to exit the program"""
        exit()

    def do_EOF(self, line):
        """EOF command to exit the program"""
        exit()

    def emptyline(line):
        """
        Empty line + ENTER shouldn’t execute anything
        """
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
