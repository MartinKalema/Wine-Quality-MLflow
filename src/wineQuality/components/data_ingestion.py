import os
from pathlib import Path
import zipfile
import urllib.request as request
from wineQuality import logger
from wineQuality.entity.entity_configuration import DataIngestionConfig
from wineQuality.utils.common import get_size

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initialize DataIngestion object with the provided configuration.

        Args:
            config (DataIngestionConfig): Configuration object for data ingestion.
        """
        self.config = config

    def download_file(self):
        """Fetch data from a URL.
        
        Raises:
            Exception: If an error occurs during the download process.
        """
        try:
            if not os.path.exists(self.config.local_data_file):
                filename, headers = request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} download! with the following info \n{headers}")
            else:
                logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

        except Exception as e:
            raise e
        
    def extract_zip_file(self):
        """Extract a zip file.

            This method extracts the contents of a zip file specified in the configuration
            to the directory specified in the configuration.

            Raises:
                Exception: If an error occurs during the extraction process.
            """
        try:
            unzip_path = self.config.unzip_dir
            os.makedirs(unzip_path, exist_ok=True)

            with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
                zip_ref.extractall(unzip_path)

            logger.info(f"Extracted zip file into: {unzip_path}")

        except Exception as e:
            logger.error(f"Error extracting zip file: {self.config.local_data_file}")
            raise e
        