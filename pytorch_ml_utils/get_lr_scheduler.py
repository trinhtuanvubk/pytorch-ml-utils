import torch

def get_lr_scheduler(optimizer, scheduler_name, **kwargs):
    if scheduler_name=="CosineAnnealingLR":
        lr_scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, **kwargs)
    elif scheduler_name=="ExponentialLR":
        lr_scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, **kwargs)
    elif scheduler_name=="StepLR":
        lr_scheduler = torch.optim.lr_scheduler.StepLR(optimizer, **kwargs)
    elif scheduler_name=="LinearLR":
        lr_scheduler = torch.optim.lr_scheduler.LinearLR(optimizer, **kwargs)
    else:
        raise ValueError(f"The method '{scheduler_name}' is not supported")
    
    return lr_scheduler