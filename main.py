from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.components.data_validation import datavalidation
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)

        data_ingestion = DataIngestion(dataingestionconfig)

        logging.info("Initiate the data ingestion")

        dataingestionartifact = data_ingestion.initiate_data_ingestion()

        print(dataingestionartifact)
        logging.info("data ingestion completed ")
        data_validation_config=DataValidationConfig(trainingpipelineconfig)
        data_validation=datavalidation(dataingestionartifact,data_validation_config)
        logging.info("Initiate the data validation")
        data_vlidation_artifact= data_validation.initiate_data_validation()
        logging.info(" data validation completed ")
        print(data_vlidation_artifact)
        

    except Exception as e:
        raise NetworkSecurityException(e, sys)