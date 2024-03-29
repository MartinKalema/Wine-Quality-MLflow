import os
from wineQuality import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from wineQuality.entity.entity_configuration import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig) -> None:
        self.config = config

    def split_data(self):
        data = pd.read_csv(self.config.data_path)

        train,test = train_test_split(data)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Split data into training and test sets")
        logger.info(f"Training set: {train.shape}")
        logger.info(f"Testing set: {test.shape}")