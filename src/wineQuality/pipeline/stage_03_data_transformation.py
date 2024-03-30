
from wineQuality.components.data_transformation import DataTransformation
from wineQuality.config.configuration_manager import ConfigurationManager
from wineQuality import logger


STAGE_NAME = "Data Transformation Stage"


class DataTransformationPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            with open("artifacts/data_validation/status.txt", "r") as f:
                status = f.read().split(" ")[-1]
            
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_data()
            else:
                raise Exception("Your data schema is not valid")
        except Exception as e:
            raise e


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataTransformationPipeline()
        obj.main()
        logger.info(
            f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
