# End to End Data Science Project

### Workflows--ML Pipeline

1. Data Ingestion : done with the commit "Refactor data ingestion step from Jupyter notebook to modular programming"
2. Data Validation
3. Data Transformation-- Feature Engineering,Data Preprocessing
4. Model Trainer
5. Model Evaluation- MLFLOW,Dagshub

## Workflows

1. Update config.yaml: important config we require(data source...)
2. Update schema.yaml: for data validation(check the schema and validate it)
3. Update params.yaml: for specific pamameters
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline : 2 pipelines training and predection 
8. Update the main.py