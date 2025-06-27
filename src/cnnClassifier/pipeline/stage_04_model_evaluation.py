from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.model_evaluation import ModelEvaluation
from cnnClassifier import logging, MyException
import sys

STAGE_NAME = "Evaluation Stage"


class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_evaluation_config()
        evaluation = ModelEvaluation(config=evaluation_config)
        evaluation.evaluate()
        # evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logging.info(f"******************************")
        logging.info(f">>>>>> stage: {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationPipeline()
        obj.main()
        logging.info(
            f">>>>>> stage: {STAGE_NAME} completed <<<<<<\n\nx=======================x"
        )
    except Exception as e:
        raise MyException(e, sys) from e
