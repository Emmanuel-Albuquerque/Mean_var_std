import numpy as np

def calculate(lista):
    if len(lista) != 9:
        raise ValueError('List must contain nine numbers.') 
    else:
        b = np.array(lista).reshape(3,3)
        
    calculations = {
        "mean": [(b.mean(axis=0).tolist()), (b.mean(axis=1).tolist()), b.mean()],
        "variance": [(b.var(axis=0).tolist()), (b.var(axis=1).tolist()), b.var()],
        "standard deviation": [(b.std(axis=0).tolist()), (b.std(axis=1).tolist()), b.std()],
        "max": [(b.max(axis=0).tolist()), (b.max(axis=1).tolist()), b.max()],
        "min": [(b.min(axis=0).tolist()), (b.min(axis=1).tolist()), b.min()],
        "sum": [(b.sum(axis=0).tolist()), (b.sum(axis=1).tolist()), b.sum()],
    }

    return calculations