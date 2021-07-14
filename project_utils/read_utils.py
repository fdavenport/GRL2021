import numpy as np
import pandas as pd
import xarray as xr
from project_utils import parameters as param

def get_hgt_input():
    """ create np.ndarray of hgt data from pre-processed files
    
    returns = numpy ndarray with dimmensions of [time, lat, lon, vars]
    """
    
    hgt_xr = xr.open_dataset("../processed_data/hgt_detrended_anomalies.nc")
    dat_np = np.array(hgt_xr['hgt_anom']).reshape(param.n, param.nlats, param.nlons, 1)
    
    return(dat_np)

def get_hgt_slp_input():
    """ create np.ndarray of hgt and slp data from pre-processed files 
    
    returns = numpy ndarray with dimmensions of [time, lat, lon, vars]
    """
    
    hgt_xr = xr.open_dataset("../processed_data/hgt_detrended_anomalies.nc")
    slp_xr = xr.open_dataset("../processed_data/slp_anomalies.nc")
    dat_np = np.concatenate([np.array(hgt_xr['hgt_anom']).reshape(param.n, param.nlats, param.nlons, 1), 
                             np.array(slp_xr['slp_anom']).reshape(param.n, param.nlats, param.nlons, 1)], 
                            axis = 3)
    
    return(dat_np)
