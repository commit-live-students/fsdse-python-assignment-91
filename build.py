import pandas as pd


def solution(dic):
    """
    Enter your code here
    """
    df = pd.DataFrame(data=dic)
    return df

solution({'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]})
