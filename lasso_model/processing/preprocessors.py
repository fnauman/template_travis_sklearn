"Custom preprocessing steps by subclassing sklearn classes"

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin

class DropFeatures(BaseEstimator, TransformerMixin):

    def __init__(self, variables_to_drop=None):
        self.variables = variables_to_drop # no need to convert this to a list

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # encode labels
        X = X.copy()
        X = X.drop(self.variables, axis=1)

        return X
