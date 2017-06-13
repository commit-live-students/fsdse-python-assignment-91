import pandas as pd


def solution(dict):
    """
    Enter your code here
    """
    df = pd.DataFrame()
    df = df.append(dict, ignore_index=True)
    return df
