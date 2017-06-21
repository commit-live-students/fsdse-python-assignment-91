import pandas as pd
dic = {"X":[78,85,96,80,86], "Y":[84,94,89,83,86], "Z":[86,97,96,72,83]}

def solution(dict):
    ser = pd.DataFrame(dict.values(), index = dict.keys())
    return ser

solution(dic)
