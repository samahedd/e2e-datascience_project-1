from dataclasses import dataclass
from pathlib import Path

@dataclass ## we dont define any methods only defining variables
class DataIngestionconfig:
  root_dir: Path
  source_url: str           ### those are the inputs to data ingestion pipeline  
  local_data_file:  Path
  unzip_dir: Path