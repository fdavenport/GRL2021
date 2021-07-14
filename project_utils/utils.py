import numpy as np
import pandas as pd
import xarray as xr
from project_utils import parameters as param

## ----------------------------------------------------------------------------

def onehot(x):
    """convert x into onehot format. x should be 1D numpy array"""
    y = np.zeros((x.size, x.max()+1)) ## create new array
    y[np.arange(x.size),x] = 1
    
    return(y)

## ----------------------------------------------------------------------------

def class_weights(x):
    """ return dictionary of class weights for categorical array"""
    
    n_class = x.max() + 1
    
    csize = []
    for i in range(n_class):
        csize.append((x == i).sum())
    
    w = dict()
    for i in range(n_class):
        w[i] = max(csize)/(csize[i]*n_class)
       
    
    return(w)

## ----------------------------------------------------------------------------

def get_precip_classes(p, q = 0.95, onehot = False):
    """ create np.ndarray of output of precipitation classes based on quantile thresholds
    p = precipitation time series
    q = quantiles to separate classes
    onehot = boolean whether or not to return result as onehot encoding
    
    returns numpy array of classes
    """
    
    if not isinstance(q, list):
        q = [q]
    n_class = len(q) + 1
    
    bin_thr = [p.min()-.01]+ p.quantile(q).tolist() + [p.max()+.01]
    p_classes = pd.cut(p, bins = bin_thr, labels = False)
    p_classes = p_classes.astype('int').to_numpy()
    
    if onehot:
        p_classes = onehot(p_classes)
    
    return(p_classes)


import statsmodels.api as sm

def fit_ols(x, y, constant = True):
    
    if constant is not False:
        x = sm.add_constant(x)
        
    model = sm.OLS(y, x).fit()
    
    return [model.params[0], model.params[1], model.pvalues[1]]

