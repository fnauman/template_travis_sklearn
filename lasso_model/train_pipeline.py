import numpy as np
from sklearn.model_selection import train_test_split

from lasso_model import pipeline
from lasso_model.processing.data_management import (
    load_dataset, save_pipeline)
from lasso_model.config import config

from lasso_model import __version__ as _version

#import logging
from lasso_model.config.logging_config import get_logger

_logger = get_logger(__name__)
#_logger = logging.getLogger(__name__)


def run_training() -> None:
    """Train the model."""

    # read training data
    data = load_dataset(file_name=config.TRAINING_DATA_FILE)

    # divide train and test
    X_train, X_test, y_train, y_test = train_test_split(
        data[config.FEATURES],
        data[config.TARGET],
        test_size=0.2,
        random_state=0)  # we are setting the seed here

    # transform the target
    y_train = np.log(y_train)
    y_test = np.log(y_test)

    pipeline.price_pipe.fit(X_train[config.FEATURES],
                            y_train)

    _logger.info(f'saving model version: {_version}')
    save_pipeline(pipeline_to_persist=pipeline.price_pipe)


if __name__ == '__main__':
    run_training()
