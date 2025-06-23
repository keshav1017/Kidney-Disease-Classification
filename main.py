from cnnClassifier import logging, MyException
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stage_02_prepare_base_mode import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stage_03_model_training import ModelTraninigPipeline
import sys

STAGE_NAME = "Data Ingestion"
try:
    logging.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n==========================================================================================================================================\n")
except Exception as e:
    raise MyException(e, sys) from e 


STAGE_NAME = "Prepare Base Model"
try:
    logging.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logging.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\n==========================================================================================================================================\n")
except Exception as e:
    raise MyException(e, sys) from e


STAGE_NAME = "Model Training"
try:
    logging.info(f">>>>>> Stage: {STAGE_NAME} started <<<<<<")
    obj = ModelTraninigPipeline()
    obj.main()
    logging.info(f">>>>>> Stage: {STAGE_NAME} completed <<<<<<\n\n==========================================================================================================================================\n")
except Exception as e:
    raise MyException(e, sys) from e