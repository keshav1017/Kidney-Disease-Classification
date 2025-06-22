import os
import sys
import yaml
from cnnClassifier import logging
from cnnClassifier import MyException
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any, List
import base64

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Reads a yaml file and returns.

    Args:
        path_to_yaml (str): path to the yaml file.
    
    Returns:
        ConfigBox: box object containing the yaml file contents.
    """
    try:
        with open(path_to_yaml) as file:
            content = yaml.safe_load(file)
            logging.info(f"yaml file: {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except Exception as e:
        raise MyException(e, sys) from e

@ensure_annotations
def create_directories(path_to_dir: list, verbose: bool=True):
    """
    Creates list of directories

    Args:
        path_to_dir (list): list of path of directories
    """
    for path in path_to_dir:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logging.info(f"Created directory at: {path}")

@ensure_annotations
def save_json(path: Path, data: dict):
    """
    Save the json data.

    Args:
        path (Path): path to json file.
        data (dict): data to be saved in json file.
    """

    with open(path, 'w') as f:
        json.dump(data, f)
    
    logging.info(f"json file saved at {path}")

@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json files data

    Args:
        path (Path): path to json file
    
    Returns:
        ConfigBox: data as class attributes of dict
    """

    with open(path) as f:
        content = json.load(f)
    
    logging.info(f"json file loaded successfully from : {path}")
    return ConfigBox(content)

@ensure_annotations
def save_bin(data: Any, path: Path):
    """
    Saves binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logging.info(f"binary file saved at: {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
    load binary data

    Args:
        path (Path): path to binary file
    
    Returns:
        Any: object stored in the file
    """
    data = joblib.load(path)
    logging.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file
    
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"

def decodeImage(imgstring, filename: Path) -> None:
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImageIntoBase64(croppedImagePath: Path):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())