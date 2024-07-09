import os
from textSummarizer.Logging import logger
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from textSummarizer.entity import DataTransformationConfig

class DataTransformer:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)

    def convert_to_feature(self, batch):
        input_encoding = self.tokenizer(batch['dialogue'], max_length = 1024, truncation = True)

        with self.tokenizer.as_target_tokenizer():
            target_encoding = self.tokenizer(batch['summary'], max_length = 128, truncation = True)
        
        return{
            'input_ids' : input_encoding['input_ids'],
            'attention_mask' : input_encoding['attention_mask'],
            'labels' : input_encoding['input_ids']
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        dataset_samsum_pt = dataset_samsum.map(self.convert_to_feature, batched= True)
        dataset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, "samsum_dataset"))