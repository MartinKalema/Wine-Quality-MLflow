import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "wineQuality"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/components/data_ingestion.py",
    f"src/{project_name}/components/model_training.py",
    f"src/{project_name}/components/model_evaluation.py",
    f"src/{project_name}/components/model_preparation.py",
    f"src/{project_name}/utilities/_init__.py",
    f"src/{project_name}/utilities/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration_manager.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/pipeline/stage_01_data_ingestion.py",
    f"src/{project_name}/pipeline/stage_02_model_preparation.py",
    f"src/{project_name}/pipeline/stage_03_model_training.py",
    f"src/{project_name}/pipeline/stage_04_model_evaluation.py",
    f"src/{project_name}/pipeline/stage_05_prediction.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/entity/entity_configuration.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "schema.yaml",
    "requirements.txt",
    "setup.py",
    "main.py",
    "research/trials.ipynb",
    "research/01_data_ingestion.ipynb",
    "research/02_base_model_preparation.ipynb",
    "research/03_model_training.ipynb",
    "research/04_model_evaluation.ipynb",
    "research/05_prediction.ipynb",
    "templates/index.html",
    "Dockerfile",
    "app.py",
    ".gitignore",
    "logs/logfile.log",
    "mlflow.py"


]

for filepath in list_of_files:
    filepath = Path(filepath)

    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory;{filedir} for the file {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")