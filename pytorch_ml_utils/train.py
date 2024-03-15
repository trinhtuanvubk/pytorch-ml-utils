import os


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