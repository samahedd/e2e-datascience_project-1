from src.datascience_project_1.config.configuration import (ConfigurationManager)
from src.datascience_project_1.components.data_ingestion import (DataIngestion)
from src.datascience_project_1 import logger

STAGE_NAME="Data ingestion stage"

class DataIngestionTrainingPipeline():
    def __init__(self):
        pass
    def initiate_data_ingestion(self):
        config=ConfigurationManager()
        data_ingestion_config=config.get_dataingestion_config()
        data_ingstion=DataIngestion(config=data_ingestion_config)
        data_ingstion.download_file()
        data_ingstion.extract_zip_file()

if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataIngestionTrainingPipeline()
        obj.initiate_data_ingestion()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e