from cnnClassifier import logging, MyException
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
import sys

STAGE_NAME = "Data Ingestion"

try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\nx===================x")
except Exception as e:
    raise MyException(e, sys) from e 