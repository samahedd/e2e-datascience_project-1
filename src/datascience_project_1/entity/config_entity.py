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

    