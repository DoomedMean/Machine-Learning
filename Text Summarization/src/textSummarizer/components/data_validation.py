import os
from textSummarizer.Logging import logger
from textSummarizer.entity import DataValidationConfig

class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_existance_files(self) -> bool:
        try:
            validate_status = None

            all_file = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))

            for file in all_file:
                if file not in self.config.All_Required_File:
                    validate_status = False
                    with open(self.config.Status_File, "w") as f:
                        f.write(f"Validation status: {validate_status}")
                else:
                    validate_status = True
                    with open(self.config.Status_File, "w") as f:
                        f.write(f"Validation status: {validate_status}")
            return validate_status
        except Exception as e:
            raise e