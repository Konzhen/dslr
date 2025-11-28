from describe import load, ft_min, ft_std, ft_var, ft_mean
import sys
import pandas as pd

def histogram(data: pd.DataFrame):
    columns = data.columns[6:]
    houses = data.groupby("Hogwarts House")
    homogeneous_houses = {}
    for house, data_house in houses:
        row = []
        for feature in columns:
            value = ft_std(ft_var(data_house[feature].dropna(), ft_mean(data_house[feature].dropna())))
            row.append(value)
        value = ft_std(ft_var(row, ft_mean(row)))
        homogeneous_houses[house] = value
    print(f"The house with the most homogeneous score is: {ft_min(homogeneous_houses)}")

def main():
    try :
        data = load("datasets/dataset_train.csv")
        histogram(data)
    except Exception as e:
        print(f"Error: {e}")    


if __name__ == "__main__":
    main()