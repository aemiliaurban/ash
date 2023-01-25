import os

import pandas as pd

from .data_parser import csv_order_data_reader, csv_merge_data_reader

DATA_FOLDER = os.path.join(os.getcwd(), "ash", "common", "user_data")

INPUT_DATA_DENDROGRAM = {
    "merge_matrix": [
        [-15, -29],
        [-17, -26],
        [-14, -16],
        [-13, -32],
        [-35, -44],
        [-36, -46],
        [-7, -38],
        [-19, -41],
        [-48, 8],
        [-49, 1],
        [-50, 6],
        [-21, -30],
        [-37, 11],
        [-27, 2],
        [-4, -42],
        [3, 14],
        [-12, 16],
        [-34, -45],
        [-22, -28],
        [-3, -31],
        [-20, 20],
        [-6, -43],
        [5, 7],
        [-1, -18],
        [-8, 24],
        [-47, 13],
        [4, 19],
        [17, 23],
        [-23, 10],
        [-25, 15],
        [-24, -40],
        [12, 26],
        [-10, 22],
        [25, 27],
        [30, 33],
        [-2, 31],
        [18, 29],
        [-5, 21],
        [-39, 32],
        [9, 37],
        [34, 36],
        [38, 41],
        [-9, -33],
        [-11, 40],
        [35, 39],
        [28, 44],
        [42, 43],
        [45, 46],
        [47, 48],
    ],
    "joining_height": [
        5.25,
        14.7,
        15.44,
        38.9,
        44.06,
        54.1,
        64.44,
        72.89,
        101.8125,
        102.8625,
        109.625,
        131.25,
        136.822222222222,
        151.875,
        159.12,
        160.086666666667,
        167.6752,
        170.17,
        176.82,
        193.1,
        190.715,
        210.28,
        236.925,
        238.84,
        225.62,
        240.6425,
        295.21,
        308.700694444444,
        337.116666666667,
        390.25,
        448.05,
        456.0037,
        523.35,
        548.434722222222,
        600.795555555556,
        677.6525,
        716.013125,
        745.138888888889,
        777.528163265306,
        869.483333333333,
        1145.09072562358,
        1404.590025,
        1484.4,
        1489.80074074074,
        1647.63166666667,
        2647.1272,
        5332.82265306122,
        7556.2752244898,
        22574.945527141,
    ],
    "order": [
        4,
        19,
        2,
        30,
        7,
        0,
        17,
        12,
        31,
        21,
        27,
        1,
        23,
        39,
        8,
        32,
        24,
        3,
        41,
        9,
        5,
        42,
        38,
        20,
        29,
        46,
        36,
        49,
        35,
        45,
        11,
        13,
        15,
        26,
        16,
        25,
        34,
        43,
        6,
        37,
        10,
        47,
        18,
        40,
        33,
        44,
        22,
        48,
        14,
        28,
    ],
    "labels": [
        "Alabama",
        "Alaska",
        "Arizona",
        "Arkansas",
        "California",
        "Colorado",
        "Connecticut",
        "Delaware",
        "Florida",
        "Georgia",
        "Hawaii",
        "Idaho",
        "Illinois",
        "Indiana",
        "Iowa",
        "Kansas",
        "Kentucky",
        "Louisiana",
        "Maine",
        "Maryland",
        "Massachusetts",
        "Michigan",
        "Minnesota",
        "Mississippi",
        "Missouri",
        "Montana",
        "Nebraska",
        "Nevada",
        "New Hampshire",
        "New Jersey",
        "New Mexico",
        "New York",
        "North Carolina",
        "North Dakota",
        "Ohio",
        "Oklahoma",
        "Oregon",
        "Pennsylvania",
        "Rhode Island",
        "South Carolina",
        "South Dakota",
        "Tennessee",
        "Texas",
        "Utah",
        "Vermont",
        "Virginia",
        "Washington",
        "West Virginia",
        "Wisconsin",
        "Wyoming",
    ],
}

# us_arrests = pd.read_csv(os.path.join(DATA_FOLDER, "USArrests.csv"))
# STATES = us_arrests["Unnamed: 0"]
# US_ARRESTS = us_arrests.drop(["Unnamed: 0"], axis=1)

FLOW_CYTOMETRY = pd.read_csv(os.path.join(DATA_FOLDER, "levine32-som24x24.csv"))
ROWS = [i for i in range(len(FLOW_CYTOMETRY.index))]

MERGE_MATRIX_RAW = pd.read_csv(os.path.join(DATA_FOLDER, "levine32-merge.csv"))
MERGE_MATRIX_V1 = MERGE_MATRIX_RAW["V1"].values.tolist()
MERGE_MATRIX_V2 = MERGE_MATRIX_RAW["V2"].values.tolist()
MERGE_MATRIX = [list(x) for x in zip(MERGE_MATRIX_V1, MERGE_MATRIX_V2)]

JOINING_HEIGHT = pd.read_csv(
    os.path.join(DATA_FOLDER, "levine32-heights.csv")
)["x"].values.tolist()

ORDER_RAW = pd.read_csv(os.path.join(DATA_FOLDER, "levine32-order.csv"))["x"].values.tolist()
ORDER = [x - 1 for x in ORDER_RAW]

INPUT_FLOW_DATA_DENDROGRAM = {
    "merge_matrix": MERGE_MATRIX,
    "joining_height": JOINING_HEIGHT,
    "order": ORDER,
    "labels": ROWS,
}