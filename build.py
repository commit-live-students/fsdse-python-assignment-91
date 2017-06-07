import pandas as pd

dic = {'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}


def solution(dic):
    """
    Enter your code here
    """
    df = pd.DataFrame(dic, columns=dic.keys())
    return df
