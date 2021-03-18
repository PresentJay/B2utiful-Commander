from cli_decorator import *


def ChainQuestion_byChoice(chainFrom, QID, ChoiceValue):
    return chainFrom.get(QID).lower() == ChoiceValue.lower()


def create_listQ(questionID, choicelist, message="", when=None, default=None):
    chainitem = {
        "type": "list",
        "name": questionID,
        "choices": choicelist,
    }

    if message:
        chainitem["message"] = message

    if when:
        chainitem["when"] = False
        for item in when:
            chainitem["when"] = lambda cli: chainitem["when"] or ChainQuestion_byChoice(
                cli, item.get("QID"), item.get("choice")
            )

    return chainitem


def create_confQ(questionID, message="", when=None):
    chainitem = {
        "type": "confirm",
        "name": questionID,
    }

    if when:
        chainitem["when"] = False
        for item in when:
            chainitem["when"] = lambda cli: chainitem["when"] or ChainQuestion_byChoice(
                cli, item.get("QID"), item.get("choice")
            )

    return chainitem


def execute(Q_list, style=styleset):
    cli = prompt(Q_list, style)
    return cli