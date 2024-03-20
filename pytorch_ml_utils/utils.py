import os
import sys
import math
import requests

import torch
import numpy as np
import requests
from tqdm import tqdm
from loguru import logger
from PIL import Image

def seed_everything(seed_value):
    np.random.seed(seed_value)
    torch.manual_seed(seed_value)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = True

def is_link(s):
    return s is not None and s.startswith('http')

def download_with_progressbar(url, save_path):
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        total_size_in_bytes = int(response.headers.get('content-length', 1))
        block_size = 1024  # 1 Kibibyte
        progress_bar = tqdm(
            total=total_size_in_bytes, unit='iB', unit_scale=True)
        with open(save_path, 'wb') as file:
            for data in response.iter_content(block_size):
                progress_bar.update(len(data))
                file.write(data)
        progress_bar.close()
    else:
        logger.error("Something went wrong while downloading models")
        sys.exit(0)


def get_pretrain_folder(pretrain_dir):
    folder = f'./ckpt/{pretrain_dir}/checkpoints'
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder

def get_ckpt_folder(ckpt_dir):
    folder = f'./ckpt/{ckpt_dir}/checkpoints'
    if not os.path.exists(folder):
        os.makedirs(folder)
    return folder