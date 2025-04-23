## for generic project structure
import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')
project_name="datascience_project_1"

list_of_files=[
    ".gthub/workflows/.gitkeep" ,
    f"src/{project_name}/__init__.py",  ## so we can package our project
    f"src/{project_name}/components/__init__.py", ## this path has the pipeline components and we need to use it as package as well(anywhere)
    f"src/{project_name}/utils/__init__.py",  ## this folder for genric funtionality, for funtions used across the project
    f"src/{project_name}/utils/common.py", ## all the funtionality that common to diffrent components we are going to define
    f"src/{project_name}/config/__init__.py", ## 
    f"src/{project_name}/config/configuration.py", 
    f"src/{project_name}/pipeline/__init__.py", ## info about diffrent pipelines we are gonna use(training, prediction)
    f"src/{project_name}/entity/__init__.py", ## 
    f"src/{project_name}/entity/config_entity.py", ## 
    f"src/{project_name}/constants/__init__.py", 
    "config/config.yaml", ## all configs
    "params.yaml", # parameters for training model
    "schema.yaml",
    "main.py" , 
    "Dockerfile" , 
    "setup.py", ## to deploy the entire project as a package
    "research/research.ipynb",
    "templates/index.html" # because we are using flask
]

for file_path in list_of_files:
    file_path=Path(file_path)
    filedir,finame=os.path.split(file_path) # split file name from its path


    if filedir !="":  ## create the folder if it isnt exist already
        os.makedirs(filedir,exist_ok=True)
        logging.info(f'Creating dir: {filedir} for file: {finame}')


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path) ==0):
        with open(file_path,"w") as f:
            pass
            logging.info(f"creating empty file {file_path}")
    else:
        logging.info(f"{file_path} is already exist")



