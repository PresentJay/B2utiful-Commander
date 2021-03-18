# Command line decorator code
import click
import six
from PyInquirer import Token, prompt, style_from_dict, Separator, ValidationError
from pyfiglet import figlet_format
from statics import *

try:
    import colorama

    colorama.init()
except ImportError:
    colorama = None

try:
    from termcolor import colored
except ImportError:
    colored = None
# # # #


""" Commandline Decorataion Line """

# define command-line colorset
styleset = style_from_dict(
    {
        Token.QuestionMark: "#fac731 bold",
        Token.Answer: "#4688f1 bold",
        Token.Instruction: "",  # default
        Token.Separator: "#cc5454",
        Token.Selected: "#0abf5b",  # default
        Token.Pointer: "#673ab7 bold",
        Token.Question: "",
    }
)


# log function : font/color/figuring(figlet module) available
def log(string, color, font=BASE_LOG_FONT, figlet=False):

    if colored:
        if figlet:
            six.print_(colored(figlet_format(string, font=font), color))  # figlet log
        else:
            six.print_(colored(string, color))  # original log
    else:
        six.print_(string)  # non-color log