import pandas as pd
import sys
from typing import Any, List

def load(path: str) -> pd.DataFrame:
    try:
        data = pd.read_csv(path)
        return data

    except Exception as e:
        print(e)

def calculate_discipline(data: pd.DataFrame) -> None:
    feature = data.columns[6:]
    stats = {
        "Count": [len(data[tmp]) for tmp in feature],
        "Mean": [get_mean(data[tmp].dropna()) for tmp in feature],
        "Std": [get_std(get_var(data[tmp].dropna(), get_mean(data[tmp].dropna()))) for tmp in feature],
        "Min": [get_min(data[tmp].dropna()) for tmp in feature],
        "25%": [get_25_percentile(data[tmp].dropna()) for tmp in feature],
        "50%": [get_50_percentile(data[tmp].dropna()) for tmp in feature],
        "75%": [get_75_percentile(data[tmp].dropna()) for tmp in feature],
        "Max": [get_max(data[tmp].dropna()) for tmp in feature]
    }
    for i in range(0, len(feature), 8):
        tmp = feature[i:i+8]

        print(f"{'':<10}", end="")
        for c in tmp:
            print(f"{(c[:8] + ('.' if len(c) > 8 else '')):<{15}}", end="")
        print()

        for stat, values in stats.items():
            print(f"{stat:<10}", end="")
            for v in values[i:i+8]:
                print(f"{v:<{15}.6f}", end="")
            print()
        print()
    print()


def get_mean(args: Any) -> float:
    """Return the arithmetic mean of all numeric values in args."""
    return (sum(x for x in args) / len(args))


def get_median(args: Any) -> float:
    """Return the median value from the sorted numeric list args."""
    args = sorted(args)
    length = len(args) % 2
    if length == 1:
        return args[len(args) // 2]
    else:
        previous = args[(len(args) // 2) - 1]
        next = args[(len(args) // 2)]
        return ((previous + next) / 2)


def get_25_percentile(args: Any) -> float:
    """Return the first and third quartiles from the sorted list args."""
    args = sorted(args)
    return (args[(int)(len(args) * 0.25)])

def get_50_percentile(args: Any) -> float:
    args = sorted(args)
    return (args[(int)(len(args) * 0.50)])

def get_75_percentile(args: Any) -> float:
    args = sorted(args)
    return (args[(int)(len(args) * 0.75)])

def get_max(args: Any) -> float:
    args = sorted(args)
    return (args[len(args) - 1])

def get_min(args: Any) -> float:
    args = sorted(args)
    return (args[0])

def get_var(args: Any, mean: float) -> float:
    """Return the variance of args given its mean."""
    return sum(((x - mean) ** 2 for x in args)) / len(args)


def get_std(variance: float):
    """Return the standard deviation from the given variance."""
    return variance ** 0.5

def main():
    try:
        data = load("data_train.csv")
        calculate_discipline(data)
    except Exception as e:
        print(f"Error: {e}")    

if __name__ == "__main__":
    main()
