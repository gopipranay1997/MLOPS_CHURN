FROM jupyter/scipy-notebook

RUN pip install joblib


USER root
RUN apt-get update && apt-get install -y jq

RUN mkdir model raw_data processed_data results


ENV RAW_DATA_DIR=/home/jovyan/raw_data
ENV PROCESSED_DATA_DIR=/home/jovyan/processed_data
ENV MODEL_DIR=/home/jovyan/model
ENV RESULTS_DIR=/home/jovyan/results
ENV RAW_DATA_FILE=Churn_Prediction.csv


COPY Churn_Prediction.csv ./raw_data/Churn_Prediction.csv
COPY preprocessing_churn.py ./preprocessing_churn.py
COPY train_churn.py ./train_churn.py
COPY test_churn.py ./test_churn.py
