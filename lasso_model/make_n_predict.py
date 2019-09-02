from lasso_model.predict import make_prediction
from lasso_model.processing.data_management import load_dataset

test_data = load_dataset(file_name='test.csv')
results = make_prediction(input_data=test_data.to_json(orient='records'))

#print(f'Printing results: {results}')

from lasso_model.config import config

#print(config.DATASET_DIR)
#print(config.LOG_DIR)
