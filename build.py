def solution(dict):
    import pandas as pd
    """
    Enter your code here
    """
    df1 = pd.DataFrame.from_dict(dict,orient='columns',dtype=None)
    return df1 
