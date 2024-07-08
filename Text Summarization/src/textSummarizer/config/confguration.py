from textSummarizer.constants import *
from textSummarizer.utils.common import read_yaml, create_dirs
from textSummarizer.entity import DataIngestionConfig, DataValidationConfig

class ConfigurationManager:
    def __init__(
        self,
        config_filepath = Config_File_Path,
        params_filepath = Params_File_Path):
        print(config_filepath)
        print(params_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_dirs([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_dirs([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir= config.root_dir,
            source_url= config.source_url,
            local_data_file= config.local_data_file,
            unzip_dir= config.unzip_dir
        )
        return data_ingestion_config
    
    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation

        create_dirs([config.root_dir])
        
        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            Status_File= config.Status_File,
            All_Required_File=config.All_Required_File
        )

        return data_validation_config