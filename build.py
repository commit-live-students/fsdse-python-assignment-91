import pandas as pd



def solution(dict_input) :
    df = pd.DataFrame.from_dict(dict_input)
    return df

solution({"X":[78,85,96,80,86], "Y":[84,94,89,83,86],"Z":[86,97,96,72,83]})
