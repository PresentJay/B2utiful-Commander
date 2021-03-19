from lib_module.cli_decorator import *
from PyInquirer import prompt


def ChainQuestion_byChoice(chainFrom, QID, ChoiceValue):
    return chainFrom.get(QID) == ChoiceValue


def create_listQ(questionID, choicelist, message="blank", when=None):
    chainitem = {
        "type": "list",
        "name": questionID,
        "message": message,
        "choices": choicelist,
    }

    if when:
        chainitem["when"] = False
        for item in when:
            chainitem["when"] = lambda cli: chainitem["when"] or ChainQuestion_byChoice(
                cli, item.get("QID"), item.get("choice")
            )

    return chainitem


def create_confQ(questionID, message="blank", when=None):
    chainitem = {"type": "confirm", "name": questionID, "message": message}

    if when:
        chainitem["when"] = when

    return chainitem


def create_checkboxQ(questionID, choicelist=[], message="blank", when=None):
    pass


def execute(Q_list, style=styleset):
    cli = prompt(Q_list, style=style)
    return cli


def makeChain(chain, chainItem, chainFrom=None, chainCondition=None):
    qid = chain["name"]
    msg = chain["message"]
    if chainFrom:
        _when = lambda Q: Q[chain["name"]] == chainFrom
    
    if chainCondition:
        for cond in chainCondition:
            _when = _when and (lambda Q: Q[chain["name"] == ])
    
    if chain["type"] == "list":
        if chainFrom:
            
            item = create_listQ(questionID=qid, message=msg, when=lambda Q: Q[chainFrom] == )
        else:
            item = create_listQ(questionID=qid, message=msg)
    
    
    if chain["chainItems"]:
        for item in chain["chainItems"]:
            chain.append(item["name"])
    
    
    
    
    if chainFrom:
        for ctx in chainFrom["chainItems"]:
            