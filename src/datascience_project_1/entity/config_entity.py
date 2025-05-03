from dataclasses import dataclass
from pathlib import Path

@dataclass ## we dont define any methods only defining variables
class DataIngestionconfig:
  root_dir: Path
  source_url: str           ### those are the inputs to data ingestion pipeline  
  local_data_file:  Path
  unzip_dir: Path

@dataclass
class DataValidationConfig:
    root_dir: Path
    unzip_data_dir: Path
    STATUS_FILE: str ## str not path because we will use this value to create the file and write to it True or False later
    all_schema: dir ## Contains all schemas from schema.yaml
  

@dataclass
class DataTransformationConfig:
    root_dir: Path
    data_path: Path


@dataclass
class ModelTrainerConfig:
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float ## because we are going to apply elastic net model
    l1_ratio: float
    target_column: str 

@dataclass
class ModelEvaluationConfig:
    root_dir: Path
    test_data_path: Path
    model_path: Path
    metric_file_name: Path
    all_params: dict
    target_column: str
    mlflow_uri: str

