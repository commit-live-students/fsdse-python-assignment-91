import pandas as pd

def solution(dict):
    d=pd.DataFrame(dict,columns=dict.keys())
    return d

dict={'X':[78,85,96,80,86], 'Y':[84,94,89,83,86],'Z':[86,97,96,72,83]}
print(solution(dict))
