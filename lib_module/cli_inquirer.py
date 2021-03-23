from lib_module.cli_decorator import *
from PyInquirer import prompt


def execute(Q_list, style=styleset):
    cli = prompt(Q_list, style=style)
    return cli


def when_chain(condition_list, chainFrom):
    retval = True
    for item in condition_list:
        retval = retval and (chainFrom[item[0]] == item[1])
    return retval


def make_chain(chain, chainItem, chainCond=[]):
    Q = {
        NAME: chainItem[NAME],
        TYPE: chainItem[TYPE],
        MESSAGE: chainItem[MESSAGE],
    }

    # list Item인 경우, choices를 제공
    if chainItem[TYPE] in (LIST, CHECKBOX):
        Qlist = []

        # choices 연결 검사
        # 있는 경우 name list 전달
        if len(chainItem[CHOICES]) > 0:
            for item in chainItem[CHOICES]:
                Qlist.append(item[NAME])

        # exit pattern 검사 1 : menu separation
        if chainItem[EXIT]:
            append_sep(Qlist)
            Qlist.append(EXIT)
        Q[CHOICES] = Qlist

    # checkbox Item인 경우, Qmark 선택 구간
    if chainItem[TYPE] == CHECKBOX:
        Q[QMARK] = "😃"

    if ROOT not in chainItem.keys():
        Q[WHEN] = lambda answers: when_chain(chainCond, answers)

    # if ROOT in chainItem.keys():
    #     chainCond = lambda answers: True
    # else:
    #     Q[WHEN] = lambda answers: chainCond

    # 최종 결정된 Q를 chain에 얹음
    chain.append(Q)

    # exit pattern 검사 2 : exit confirm Q 추가
    if EXIT in chainItem.keys():
        chain.append(
            {
                TYPE: "confirm",
                NAME: "exit_confirm",
                MESSAGE: "Do you want to exit from Client?",
                WHEN: lambda answers: answers[chainItem[NAME]] == EXIT,
            }
        )

    # recursive chain
    if len(chainItem[CHOICES]) > 0:

        for item in chainItem[CHOICES]:
            if not chainItem[ROOT]:
                chainCond.append((chainItem[NAME], item[NAME]))

            make_chain(chain, item, chainCond)