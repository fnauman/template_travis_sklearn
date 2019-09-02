import pandas as pd
import pathlib

import lasso_model

pd.options.display.max_rows = 10
pd.options.display.max_columns = 10

PACKAGE_ROOT = pathlib.Path(lasso_model.__file__).resolve().parent
TRAINED_MODEL_DIR = PACKAGE_ROOT / 'trained_models'
DATASET_DIR = PACKAGE_ROOT / 'datasets'

TESTING_DATA_FILE = 'test.csv'
TRAINING_DATA_FILE = 'train.csv'
TARGET = 'target'


FEATURES = [
            'CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE',
            'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'
            ]

# Features to drop
DROP_FEATURES = ['ZN', 'INDUS', 'CHAS']

# Features to log transform
NUMERICALS_LOG_VARS = ['B']

PIPELINE_NAME = 'lasso_regression'
PIPELINE_SAVE_FILE = f'{PIPELINE_NAME}_output_v'

# used for differential testing
ACCEPTABLE_MODEL_DIFFERENCE = 0.05

LOG_DIR = PACKAGE_ROOT / 'logs'
