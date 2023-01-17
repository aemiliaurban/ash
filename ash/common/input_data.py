import os

import pandas as pd

INPUT_DATA_DENDROGRAM = {
    "merge_matrix": [
        [-1, -8],
        [-3, -5],
        [-6, -10],
        [-4, 3],
        [1, 4],
        [-2, 2],
        [-9, 6],
        [5, 7],
        [-7, 8],
    ],
    "joining_height": [
        282.45,
        537.97,
        629.66,
        844.635,
        1347.43916666667,
        1968.0425,
        3422.88555555556,
        6094.602725,
        19984.8865432099,
    ],
    "order": [6, 0, 7, 3, 5, 9, 8, 1, 2, 4],
    #    "order": [7, 1, 8, 4, 6, 1, 0, 9, 2, 3, 5],
    "labels": [
        "Alabama",  # 0
        "Alaska",  # 1
        "Arizona",  # 2
        "Arkansas",  # 3
        "California",  # 4
        "Colorado",  # 5
        "Connecticut",  # 6
        "Delaware",  # 7
        "Florida",  # 8
        "Georgia",  # 9
    ],
}

us_arrests = pd.read_csv(f"/Users/niki/diplomka/ash/ash/user_data/USArrests.csv")
us_arrests = us_arrests.head(10)
STATES = us_arrests["Unnamed: 0"]
US_ARRESTS = us_arrests.drop(["Unnamed: 0"], axis=1)