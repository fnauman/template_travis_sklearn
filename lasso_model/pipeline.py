from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from lasso_model import preprocessors as pp

DROP_FEATURES = ['ZN', 'INDUS', 'CHAS']

# variables to log transform
NUMERICALS_LOG_VARS = ['B']

PIPELINE_NAME = 'lasso_regression'

price_pipe = Pipeline(
    [
       ('log_transformer',
            pp.LogTransformer(variables=NUMERICALS_LOG_VARS)),
        ('drop_features',
            pp.DropFeatures(variables_to_drop=DROP_FEATURES)),
        ('scaler', MinMaxScaler()),
        ('Linear_model', Lasso(alpha=0.001, random_state=123))
    ]
)
