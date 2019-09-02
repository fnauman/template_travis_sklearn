import numpy as np
import pandas as pd

from lasso_model.processing.data_management import load_pipeline
from lasso_model.config import config
from lasso_model.processing.validation import validate_inputs
from lasso_model import __version__ as _version

#import logging
from lasso_model.config.logging_config import get_logger

_logger = get_logger(__name__)
#_logger = logging.getLogger(__name__)

pipeline_file_name = f'{config.PIPELINE_SAVE_FILE}{_version}.joblib'
_price_pipe = load_pipeline(file_name=pipeline_file_name)


def make_prediction(*, input_data) -> dict:
    """Make a prediction using the saved model pipeline."""

    data = pd.read_json(input_data)
    validated_data = validate_inputs(input_data=data)
    prediction = _price_pipe.predict(validated_data[config.FEATURES])
    output = np.exp(prediction)

    results = {'predictions': output, 'version': _version}

    _logger.info(
        f'Making predictions with model version: {_version} '
        f'Inputs: {validated_data} '
        f'Predictions: {results}')

    return results
