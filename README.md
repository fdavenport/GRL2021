## Using machine learning to analyze physical causes of climate change: a case study of U.S. Midwest extreme precipitation

[![DOI](https://zenodo.org/badge/386007204.svg)](https://zenodo.org/badge/latestdoi/386007204)

Supporting code for Davenport and Diffenbaugh (2021) 'Using machine learning to analyze physical causes of climate change: a case study of U.S. Midwest extreme precipitation' 

#### To cite: 

Davenport, F. V. & Diffenbaugh, N. S. (2021). Using machine learning to analyze physical causes of climate change: a case study of U.S. Midwest extreme precipitation. *Geophysical Research Letters*, 48, e2021GL093787, https://doi.org/10.1029/2021GL093787

If you find meaningful errors in the code or have questions, please contact Frances Davenport

## Organization of repository 
* **input_data**: input data used for analysis (not all raw data is included due to size; see details below)
* **notebooks**: jupyter notebooks and python scripts to read and analyze data, and create figures
* **processed_data**: processed data from analysis
* **project_utils**: python utilities used in analysis (see instructions below to install)
* **figures** (placeholder directory for figure pdfs created by running figure notebooks in **notebooks** directory)
* environment.yml (specifies python packages needed to run notebooks)
* environment_tf1.yml (specifies python packages needed to run the LRP notebook)

## data
Data analyzed in the paper is publicly available from  the following sources: 

* **PRISM daily precipitation**: available from the [PRISM Climate
Group](http://www.prism.oregonstate.edu/), Oregon State University

* **NCEP/NCAR-R1 reanalysis**: daily reanalysis is available through ftp access from [NOAA](https://psl.noaa.gov/data/gridded/data.ncep.reanalysis.html). The following variables are used in the analysis: geopotential height (*hgt*), sea-level pressure (*slp*), zonal wind (*uwind*), meridional wind (*vwind*), specific humidity (*shum*). 

* **GHCN precipitation station data**: daily precipitation observations from the Global Historical Climatology Network are available from [NOAA](https://www.ncdc.noaa.gov/ghcnd-data-access). 

Due to the large size of the raw data, pre-processed data has been uploaded to figshare and is available to download [here](https://figshare.com/articles/dataset/Pre-processed_data_for_Davenport_and_Diffenbaugh_2021/14977440). See **notebooks** directory for more detail on recreating the analysis starting from the pre-processed data. 

## Steps to run the notebooks:
1. download this repository  
2. download pre-processed data [here](https://figshare.com/articles/dataset/Pre-processed_data_for_Davenport_and_Diffenbaugh_2021/14977440) into the processed_data folder. 
3. install the required python modules using conda. The environment.yml and environment_tf1.yml provide information on the required modules. (The environment_tf1.yml files specifies the tensorflow 1 compatible environment needed to calculate the layerwise relevance propagation - see **notebooks** directory for more details)
4. install project_utils in conda environment with the following command (should be run from within the main project directory): 
```bash
pip install -e . --user
```
5. run and/or edit the notebooks. 
