from ..core import *

def test_case_1():
    Bot = Mystat("zulmu_aa95", "Mjm54#ng")
    return Bot.get_auth()[0] == True


def test_case_2():
    Bot = Mystat("sfdsf", "Mjm5fasfsf4#ng")
    return Bot.get_auth()[0] == False


def test_case_3():
    Bot = Mystat("fergf", "Mjm54egrtghth#ng")
    return Bot.get_auth()[0] == False
