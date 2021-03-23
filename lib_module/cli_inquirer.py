from lib_module.cli_decorator import *
from PyInquirer import prompt


def execute(Q_list, style=styleset):
    cli = prompt(Q_list, style=style)
    return cli


def chain_explorer(chain, chainFrom, target=None):
    cursor = chain
    when = True
    if target:
        target_list = target.split("-")
    while cursor[INDEX] != target:
        next_ = cursor[CHOICES][int(target_list.pop(0))]
        when = when and (chainFrom[cursor[NAME]] == next_[NAME])
        cursor = next_
        
    return when


def make_chain(chain, chainItem, chainCond=[]):
    Q = {
        INDEX: chainItem[INDEX],
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
        if EXIT in chainItem.keys():
            append_sep(Qlist)
            Qlist.append(EXIT)
        Q[CHOICES] = Qlist

    # checkbox Item인 경우, Qmark 선택 구간
    if chainItem[TYPE] == CHECKBOX:
        Q[QMARK] = "😃"

    if chainItem[INDEX] != ROOT:
        Q[WHEN] = lambda answers: chain_explorer(chain=chain, chainFrom= answers, target=chainItem[INDEX])
        

    # 최종 결정된 Q를 chain에 얹음
    chain.append(Q)

    # exit pattern 검사 2 : exit confirm Q 추가
    if EXIT in chainItem.keys():
        chain.append(
            {
                TYPE: CONFIRM,
                NAME: EXIT_COND,
                MESSAGE: "Do you want to exit from " + CLIENT_TITLE + "?",
                WHEN: lambda answers: answers[chainItem[NAME]] == EXIT,
            }
        )

    # recursive chain
    if len(chainItem[CHOICES]) > 0:

        for item in chainItem[CHOICES]:
            chainCond.append((chainItem[NAME], item[NAME]))

            make_chain(chain, item, chainCond)