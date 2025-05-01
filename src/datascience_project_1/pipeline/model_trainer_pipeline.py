from src.datascience_project_1.config.configuration import (ConfigurationManager)
from src.datascience_project_1.components.data_trainer import ModelTrainer
from src.datascience_project_1 import logger
from pathlib import Path


STAGE_NAME="Model Trainer stage"


class ModelTrainerPipeline:
    def __init__(self):
        pass

    def initiate_model_trainer(self):

        try:
            config = ConfigurationManager()
            model_trainer_config = config.get_model_trainer_config()
            model_trainer = ModelTrainer(config=model_trainer_config)
            model_trainer.train()
        except Exception as e:
            raise e