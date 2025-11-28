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
        "Mean": [ft_mean(data[tmp].dropna()) for tmp in feature],
        "Std": [ft_std(ft_var(data[tmp].dropna(), ft_mean(data[tmp].dropna()))) for tmp in feature],
        "Min": [ft_min(data[tmp].dropna()) for tmp in feature],
        "25%": [ft_25_percentile(data[tmp].dropna()) for tmp in feature],
        "50%": [ft_50_percentile(data[tmp].dropna()) for tmp in feature],
        "75%": [ft_75_percentile(data[tmp].dropna()) for tmp in feature],
        "Max": [ft_max(data[tmp].dropna()) for tmp in feature]
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


def ft_sorted(args: Any):
    lst = list(args)
    sortedLst = []
    while lst:
        min = lst[0]
        if len(lst) > 1:
            for x in lst[1:]:
                if x < min:
                    min = x
        sortedLst.append(min)
        lst.remove(min)
    return sortedLst


def ft_sum(args: Any):
    """Return the arithmetic sum of all numeric values in args."""
    result = 0
    for x in args:
        result += x
    return result


def ft_mean(args: Any):
    """Return the arithmetic mean of all numeric values in args."""
    return (ft_sum(x for x in args) / len(args))


def ft_median(args: Any):
    """Return the median value from the sorted numeric list args."""
    args = sorted(args)
    length = len(args) % 2
    if length == 1:
        return args[len(args) // 2]
    else:
        previous = args[(len(args) // 2) - 1]
        next = args[(len(args) // 2)]
        return ((previous + next) / 2)


def ft_25_percentile(args: Any):
    """Return the first and third quartiles from the sorted list args."""
    args = sorted(args)
    return (args[(int)(len(args) * 0.25)])


def ft_50_percentile(args: Any):
    args = sorted(args)
    return (args[(int)(len(args) * 0.50)])


def ft_75_percentile(args: Any):
    args = sorted(args)
    return (args[(int)(len(args) * 0.75)])


def ft_max(args: Any):
    args = ft_sorted(args)
    return (args[len(args) - 1])


def ft_min(args: Any):
    args = ft_sorted(args)
    return (args[0])


def ft_var(args: Any, mean: float):
    """Return the variance of args given its mean."""
    return ft_sum(((x - mean) ** 2 for x in args)) / len(args)


def ft_std(variance: float):
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
