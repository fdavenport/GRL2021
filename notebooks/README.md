
## notebooks

Notebooks are numbered in the order they are run. 

* **0a_read_reanalysis.ipynb** *(can be skipped if starting with pre-processed data)*
* **0b_read_prism.ipynb** *(can be skipped if starting with pre-processed data)*
* **0c_read_ghcn.ipynb** *(can be skipped if starting with pre-processed data)*
* **1_train_cnn.ipynb**
* **2_lrp.ipynb** *(requires tensorflow 1.15)* 

The first three notebooks (0a, 0b, 0c) read raw data and save processed data for later analysis. 
These notebooks can be skipped if pre-processed data is downloaded [here](https://figshare.com/articles/dataset/Pre-processed_data_for_Davenport_and_Diffenbaugh_2021/14977440). 

Notebooks 1 and 2 train the CNN, and perform the layerwise relevance propagation calculations. 
* Note 1: The trained model weights are included in the processed data folder. These are recreated by running 1_train_cnn.ipynb. However, as the exact training is subject to some randomness, very slight variations in the training results may arise when training on a different computer.
* Note 2: lrp is calculated using the iNNvestigate package, which requires tensorflow <=1.15 (as of writing). 
The lrp notebook was run in the environment specified by the environment_tf1.yml file in the main project directory. (The lrp results are also included with the pre-processed data [here](https://figshare.com/articles/dataset/Pre-processed_data_for_Davenport_and_Diffenbaugh_2021/14977440)). 

The remaining notebooks perform additional calculations and create the final figures: 
* **Figure_1.ipynb**
* **Figure_2.ipynb** *(also Fig. S1, S2, S5, S6)*
* **Figure_3.ipynb** *(also Fig. S7, S8, Table S1)*
* **Figure_4.ipynb**
* **Figure_S3.ipynb**
* **Figure_S4.ipynb**
