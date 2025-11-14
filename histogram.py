from describe import get_var, get_mean
import pandas as pd

def histogram(data: pd.DataFrame) -> float:
    columns = data.columns[6:]
    tmp = get_var(get_mean(data[columns[0]].dropna()))
    for i in range(len(columns)):
        n = get_var(get_mean(data[tmp].dropna()))
        tmp = n if n < tmp else tmp
    return tmp