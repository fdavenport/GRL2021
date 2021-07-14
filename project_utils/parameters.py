import numpy as np
import xarray as xr

# general analysis
time_period = slice("1981-01-01", "2019-12-31") # for climatology calculations
early_years = slice("1981-01-01", "1999-12-31")
early_stop = 1999
late_years = slice("2000-01-01", "2019-12-31")

dates = xr.open_dataset("../processed_data/dates.nc").reset_coords().time
n = 14244 ## number of days 

mm2inch = 0.0393701
g = 9.80665
mflux_levels = slice(1000, 300)
hgt_level = 500

## reanalysis region
lat_bbox = slice(55, 20)  
lon_bbox = slice(220, 305) 
lats = np.array([55. , 52.5, 50. , 47.5, 45. , 42.5, 40. , 37.5, 35. , 32.5, 30. ,
       27.5, 25. , 22.5, 20. ])
nlats = len(lats)
lons = np.array([220. , 222.5, 225. , 227.5, 230. , 232.5, 235. , 237.5, 240. ,
       242.5, 245. , 247.5, 250. , 252.5, 255. , 257.5, 260. , 262.5,
       265. , 267.5, 270. , 272.5, 275. , 277.5, 280. , 282.5, 285. ,
       287.5, 290. , 292.5, 295. , 297.5, 300. , 302.5, 305. ])
nlons = len(lons)

## midwest precipitation region
region_lat = slice(48, 37)
region_lon = slice(-104, -86)
region_box_y = [region_lat.start, region_lat.start, region_lat.stop, region_lat.stop, region_lat.start]
region_box_x = [region_lon.start, region_lon.stop, region_lon.stop, region_lon.start, region_lon.start]

