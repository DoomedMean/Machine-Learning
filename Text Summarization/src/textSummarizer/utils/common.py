import os
import yaml
from pathlib import Path
from textSummarizer.Logging import logger
from box import ConfigBox
from box.exception import BoxValueError
from ensure import ensure_annotation


@ensure_annotation
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """read yaml file and returns

    Args:
        path_to_yaml(str): Path

    Raised:
        ValueError: if yaml file is empty
        e: empty file

    Return:
        ConfigBox: ConfigBox type
    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} Load Successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
@ensure_annotation
def create_dirs(path_to_dirs:list, verbose = True):
    """Create list of dirs

    Args:
        path_to_dirs(list): list of directories
        ignore_log (bool, optional): ignore multiple dirs is to be created, defaults is False

    """
    for path in path_to_dirs:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Create direectory at {path}")

@ensure_annotation
def get_size(path: Path) -> str:
    """ get size on kB

    Args:
        path (Path): path to file
    Return:
    str: size in kB

    """
    size_in_kB= round(os.path.getsize(path)/1024) 
    return f"~ {size_in_kB} kB"