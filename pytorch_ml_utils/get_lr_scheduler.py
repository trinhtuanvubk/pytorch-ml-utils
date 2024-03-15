import torch

def get_lr_scheduler(optimizer, scheduler_name, **kwargs):
    if scheduler_name=="CosineAnnealingLR":
        lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, **kwargs)
    elif scheduler_name=="ExponentialLR":
        lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, **kwargs)
    return lr_scheduler