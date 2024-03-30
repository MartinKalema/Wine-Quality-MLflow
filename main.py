import os
from wineQuality import logger
from wineQuality.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from wineQuality.pipeline.stage_02_data_validation import DataValidationPipeline
from wineQuality.pipeline.stage_03_data_transformation import DataTransformationPipeline
from wineQuality.pipeline.stage_04_model_training import ModelTrainingPipeline
from wineQuality.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline

os.environ["MLFLOW_TRACKING_URI"]="https://dagshub.com/kalema3502/Wine-Quality-MLflow.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"]="kalema3502"
os.environ["MLFLOW_TRACKING_PASSWORD"]="fb3845efcc3b2e46a4157b1d2c977a21e02dd16e"

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info("*********************************\n")
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n**********************************")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataValidationPipeline()
    obj.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"


try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = DataTransformationPipeline()
    obj.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model Training Stage"


try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e
    
STAGE_NAME = "Model Evaluation Stage"

try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(
        f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
except Exception as e:
    logger.exception(e)
    raise e