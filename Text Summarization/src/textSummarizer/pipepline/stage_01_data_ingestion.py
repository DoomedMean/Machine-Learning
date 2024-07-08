from textSummarizer.config.confguration import ConfigurationManager
from textSummarizer.components.data_ingestion import DataIngestion
from textSummarizer.Logging import logger

class DataIngestionPipeline:
    def __init__(seld):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.dowload_file()
        data_ingestion.extract_zip_file()
