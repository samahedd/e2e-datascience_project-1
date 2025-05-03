from src.datascience_project_1.config.configuration import (ConfigurationManager)
from src.datascience_project_1.components.model_evaluation import ModelEvaluation
from src.datascience_project_1 import logger

STAGE_NAME="Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.log_into_mlflow()
