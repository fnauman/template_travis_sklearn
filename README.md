# Template for sklearn packages that train, predict with testing, logging, versioning, CI included

[![Build Status](https://travis-ci.com/fnauman/template_travis_sklearn.svg?token=q5AfnMFdqgqeFvbQzPha&branch=master)](https://travis-ci.com/fnauman/template_ravis_sklearn)

## lasso_model

This is a template on how to structure `scikit-learn` projects for training and testing machine learning models for deployment. It is based on LASSO but can be easily adapted to other `scikit-learn` algorithms. The preprocessing similarly can be significantly enhanced.

Currently, this template includes:
 - Module/sub-module like structure to separate preprocessing, training, testing, etc.
 - Logging (note the logging in the course was not working)
 - Versioning
 - Testing (`pytest`)
 - Continuous Integration (`travis`)
 
## Usage
 - Step 0: Make sure the package requirement in `requirements.txt` is satisfied. This can be done in a number of ways. I usually just create a new conda environment and run `conda install pip` followed by `pip install -r requirements.txt`.
 - Step 1: Set the PYTHONPATH so that it can search for this module:
 `export PYTHONPATH=$PYTHONPATH:/user/repos/template_travis_sklearn/`
 where `/user/repos/` is the folder where you cloned this repo.
 `mkdir lasso_model/logs`
 - Step 2: Train the model by doing:
 `python template_travis_sklearn/lasso_model/train_pipeline.py`
 If this gives you an error, it is most likely because one or more of the packages are not installed since you did not follow step 0.
 - Step 3: Test the model works by doing: `pytest /user/repos/template_travis_sklearn`

You can view the log files in `lasso_model/logs/` that end with `.log` extension with a date.

## Directory structure
Note that since logs is empty, git does not create this folder so you have to create it by `mkdir lasso_model/logs`.
```
.
├── lasso_model
│   ├── config
│   │   ├── config.py
│   │   ├── __init__.py
│   │   └── logging_config.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── test.csv
│   │   └── train.csv
│   ├── __init__.py
│   ├── logs
│   ├── make_n_predict.py
│   ├── pipeline.py
│   ├── predict.py
│   ├── preprocessors.py
│   ├── processing
│   │   ├── data_management.py
│   │   ├── errors.py
│   │   ├── features.py
│   │   ├── __init__.py
│   │   ├── preprocessors.py
│   │   └── validation.py
│   ├── trained_models
│   │   └── __init__.py
│   ├── train_pipeline.py
│   └── VERSION
├── LICENSE
├── README.md
├── requirements.txt
└── tests
    ├── __init__.py
    └── test_predict.py
```
 
## TODO
 - Documentation 
 - Code coverage
 - Packaging (`setup.py`, `pip install ...`)

## Acknowledgements:
 - `scikit-learn` packaging: [Course by Soledad Galli, Christoper Samiullah](https://www.udemy.com/deployment-of-machine-learning-models/)
 - `travis` [template by Jake Vanderplas](https://github.com/jakevdp/travis-python-template)

## LICENCE/COPYRIGHT
This code is modified from the course cited above, the accompanying BSD-3 license requires this explicit copyright:

[LICENCE](https://github.com/trainindata/deploying-machine-learning-models/blob/master/LICENSE)

> Copyright (c) 2019, Soledad Galli and Christopher Samiullah. Deployment of Machine Learning Models, online course.
All rights reserved.
