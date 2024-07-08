from textSummarizer.pipepline.stage_01_data_ingestion import DataIngestionPipeline
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