from describe import load, ft_sum, ft_max, ft_mean, ft_min
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_r(main, comp, meanMain, meanComp):
    numMain = [x - meanMain for x in main]
    numComp = [y - meanComp for y in comp]
    numerator = ft_sum(x * y for x, y in zip(numMain, numComp))
    denMain = ft_sum((x - meanMain) ** 2 for x in main)
    denComp = ft_sum((y - meanComp) ** 2 for y in comp)
    denominator = (denMain * denComp) ** 0.5
    return numerator / denominator

def pearson(data: pd.DataFrame):
    columns = data.columns[6:]
    correlations = {}
    for featureMain in columns:
        for featureComp in columns:
            fm = data[featureMain]
            fc = data[featureComp]
            if (featureMain is not featureComp):
                r = get_r(fm.dropna(), fc.dropna(), ft_mean(fm.dropna()), ft_mean(fc.dropna()))
                correlations[(featureMain, featureComp)] = abs(r)
    return ft_max(correlations)

def main():
    try :
        data = load("datasets/dataset_train.csv")
        pearson(data)
        best_pair = pearson(data)
        x = data[best_pair[0]]
        y = data[best_pair[1]]
        plt.scatter(x, y, c="red")
        plt.legend()
        plt.show()
    except Exception as e:
        print(f"Error: {e}")    


if __name__ == "__main__":
    main()