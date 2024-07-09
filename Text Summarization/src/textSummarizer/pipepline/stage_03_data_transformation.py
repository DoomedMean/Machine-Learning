from textSummarizer.config.confguration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformer
from textSummarizer.Logging import logger

class DataTransformerPipeline:
    def __init__(self):
        pass

    def main (self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformer(config=data_transformation_config)
        data_transformation.convert()