from textSummarizer.config.confguration import ConfigurationManager
from textSummarizer.components.model_evaluation import ModelEvalution
from textSummarizer.Logging import logger

class ModelEvaluationPipeline():
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvalution(config=model_evaluation_config)
        model_evaluation.evaluate()