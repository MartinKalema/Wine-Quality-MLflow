
from wineQuality.components.data_validation import DataValidation
from wineQuality.config.configuration_manager import ConfigurationManager
from wineQuality import logger


STAGE_NAME = "Data Ingestion Stage"


class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> {STAGE_NAME} started <<<<<<")
        obj = DataValidationPipeline()
        obj.main()
        logger.info(
            f">>>>>> {STAGE_NAME} completed <<<<<<<\n")
    except Exception as e:
        logger.exception(e)
        raise e
