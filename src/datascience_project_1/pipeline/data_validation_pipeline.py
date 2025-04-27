from src.datascience_project_1.config.configuration import (ConfigurationManager)
from src.datascience_project_1.components.data_validation import DataValiadtion
from src.datascience_project_1 import logger

STAGE_NAME="Data validation stage"

class DataValidationTrainingPipeline():
    def __init__(self):
        pass
    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValiadtion(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.initiate_data_validation()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e