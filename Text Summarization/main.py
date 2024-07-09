from textSummarizer.pipepline.stage_01_data_ingestion import DataIngestionPipeline
from textSummarizer.pipepline.stage_02_data_validation import DataValidationPipeline
from textSummarizer.pipepline.stage_03_data_transformation import DataTransformerPipeline
from textSummarizer.pipepline.stage_04_model_trainer import ModelTrainerPipeline
from textSummarizer.pipepline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummarizer.Logging import logger

Stage_Name = "Data Ingestion Stage"
try:
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Started <<<<<<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Validation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Started <<<<<<<<<<")
    data_validation = DataValidationPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Data Transformation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Started <<<<<<<<<<")
    data_transformation = DataTransformerPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Trainer Stage"
try:
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Started <<<<<<<<<<")
    model_trainer = ModelTrainerPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

Stage_Name = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Started <<<<<<<<<<")
    model_evaluation = ModelEvaluationPipeline()
    model_evaluation.main()
    logger.info(f">>>>>>>>>> Stage {Stage_Name} Completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e