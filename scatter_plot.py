from describe import load, get_min, get_max, get_var, get_std, get_mean
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_r(main, comp, meanMain, meanComp):
    numMain = [x - meanMain for x in main]
    numComp = [y - meanComp for y in comp]
    numerator = sum(x * y for x, y in zip(numMain, numComp))
    denMain = sum((x - meanMain) ** 2 for x in main)
    denComp = sum((y - meanComp) ** 2 for y in comp)
    denominator = (denMain * denComp) ** 0.5
    return numerator / denominator

def pearson(data: pd.DataFrame):
    columns = data.columns[6:]
    features = {}
    for featureMain in columns:
        for featureComp in columns:
            fm = data[featureMain]
            fc = data[featureComp]
            if (featureMain is not featureComp):
                r = get_r(fm.dropna(), fc.dropna(), get_mean(fm.dropna()), get_mean(fc.dropna()))
                print(r)

    


def main():
    try :
        data = load("datasets/dataset_train.csv")
        pearson(data)
        #scatter = scatter_plot(data)
        #scatterRange = np.linspace(get_min(scatter.values()), get_max(scatter.values()))
        #plt.scatter(data["Herbology"], data["Defense Against the Dark Arts"], c= "Red")
        #plt.xlabel("Herbology")
        #plt.ylabel("Defense Against the Dark Arts")
        #plt.show()
    except Exception as e:
        print(f"Error: {e}")    


if __name__ == "__main__":
    main()