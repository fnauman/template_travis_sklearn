from sklearn.linear_model import Lasso
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler

from lasso_model.processing import preprocessors as pp
from lasso_model.processing import features

from lasso_model.config import config

#import logging
from lasso_model.config.logging_config import get_logger

_logger = get_logger(__name__)
#_logger = logging.getLogger(__name__)


price_pipe = Pipeline(
    [
       ('log_transformer',
            features.LogTransformer(variables=config.NUMERICALS_LOG_VARS)),
        ('drop_features',
            pp.DropFeatures(variables_to_drop=config.DROP_FEATURES)),
        ('scaler', MinMaxScaler()),
        ('Linear_model', Lasso(alpha=0.001, random_state=123))
    ]
)
