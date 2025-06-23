from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_training import Training
from cnnClassifier import logging, MyException
import sys

STAGE_NAME = "Model Training"

class ModelTraninigPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try:
        logging.info(f"******************************")
        logging.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
        obj = ModelTraninigPipeline()
        obj.main()
        logging.info(f">>>>>> stage: {STAGE_NAME} completed <<<<<<\n\nx=======================x")
    except Exception as e:
        raise MyException(e, sys) from e