import numpy as np
import pandas as pd
import json
import os


class DataLoader:
    """A class for data loading and transforming data for the model"""

    def __init__(self, train_file, test_file, val_file):
        self.data_train = pd.read_csv(train_file, delimiter="\t")
        self.data_test = pd.read_csv(test_file, delimiter="\t")
        self.data_val = pd.read_csv(val_file, delimiter="\t")
        self.len_train = len(self.data_train)
        self.len_test = len(self.data_test)
        self.len_val = len(self.data_val)


configs = json.load(open('../config.json', 'r'))
data = DataLoader(
    configs['data']['train_filename'],
    configs['data']['test_filename'],
    configs['data']['val_filename']
)
print(data.data_val[:5])
