import pandas as pd
import sys
from describe import load
from typing import Any, List

def main():
    try:
        data = load("data_train.csv")
        calculate_discipline(data)
    except Exception as e:
        print(f"Error: {e}")    


if __name__ == "__main__":
    main()