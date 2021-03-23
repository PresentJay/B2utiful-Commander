# Command line decorator code
import six
from PyInquirer import Token, style_from_dict, Separator
from pyfiglet import figlet_format
from lib_module.statics import *

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


def clear_Terminal():
    print(u"{}[2J{}[;H".format(chr(27), chr(27)), end="")


def append_sep(chainFrom):
    chainFrom.append(Separator("\n - - - - - - - - - - - - - - - - - - - \n"))


""" Commandline ataion Line """

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


"""Colorize text.

    Available text colors:
        red, green, yellow, blue, magenta, cyan, white.

    Available text highlights:
        on_red, on_green, on_yellow, on_blue, on_magenta, on_cyan, on_white.

    Available attributes:
        bold, dark, underline, blink, reverse, concealed.

    Example:
        colored('Hello, World!', 'red', 'on_grey', ['blue', 'blink'])
        colored('Hello, World!', 'green')
"""


# log function : font/color/figuring(figlet module) available
def log(string="", color="blue", font=BASE_LOG_FONT, figlet=False, coloredList=None):

    if coloredList:
        six.print_(coloredList)
    else:
        if colored:
            if figlet:
                # figlet log
                six.print_(colored(figlet_format(string, font=font), color))
            else:
                six.print_(colored(string, color))  # original log
        else:
            six.print_(string)  # non-color log


def getColoredTexts(textColorArgs):
    text = ""
    for item in textColorArgs:
        text += colored(item["string"], item["color"])
    return text
