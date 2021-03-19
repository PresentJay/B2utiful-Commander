from lib_module.cli_decorator import *
from PyInquirer import prompt


def ChainQuestion_byChoice(chainFrom, QID, ChoiceValue):
    return chainFrom.get(QID) == ChoiceValue


def create_listQ(questionID, choicelist, message="blank", when=None):
    chainitem = {
        "type": "list",
        "name": questionID,
        "choices": choicelist,
    }

    chainitem["message"] = message

    if when:
        chainitem["when"] = False
        for item in when:
            chainitem["when"] = lambda cli: chainitem["when"] or ChainQuestion_byChoice(
                cli, item.get("QID"), item.get("choice")
            )

    return chainitem


def create_confQ(questionID, message="blank", when=None):
    chainitem = {
        "type": "confirm",
        "name": questionID,
    }

    chainitem["message"] = message

    if when:
        chainitem["when"] = when

    return chainitem


def execute(Q_list, style=styleset):
    cli = prompt(Q_list, style=style)
    return cli
