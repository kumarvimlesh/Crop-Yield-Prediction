# -*- coding: utf-8 -*-
"""midesem8_mproject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1R_jbhJD3kfZV00UXwUbe_JrsUIF0yx5c
"""

import json
import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import array
from numpy import concatenate
import tensorflow as tf
from numpy import newaxis
from pandas import concat
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from tensorflow import keras
from keras.layers import TimeDistributed
from keras.models import Sequential
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Conv1D,Conv2D, MaxPooling1D
from keras.layers import Activation
from keras.layers import LSTM
from keras.layers import Dropout
from keras.optimizers import Adam
import pickle

"""## Rice Crop Production Dataset"""

path="crop_production.csv"
dfx=pd.read_csv(path)
dfx

dfx.shape

rice_df=dfx[dfx['Crop']=='Rice']
rice_df

rice_df = rice_df.groupby(['State_Name','Crop_Year']).sum().reset_index()
rice_df

rice_df.head(20)

final_data=rice_df
final_data

new_row = {'State_Name':'Delhi', 'Crop_Year':2000, 'Area':6800, 'Production':29000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2001, 'Area':5800, 'Production':19000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2002, 'Area':6500, 'Production':23700}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2003, 'Area':6800, 'Production':29000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2004, 'Area':6900, 'Production':30000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2005, 'Area':7440, 'Production':31420}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2006, 'Area':7000, 'Production':31000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2007, 'Area':7400, 'Production':31400}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2008, 'Area':7400, 'Production':31400}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2009, 'Area':6800, 'Production':29000}
final_data=final_data.append(new_row,ignore_index=True)
new_row = {'State_Name':'Delhi', 'Crop_Year':2010, 'Area':7000, 'Production':29400}
final_data=final_data.append(new_row,ignore_index=True)

print(final_data.shape)

final_data.isnull().sum()

fd = pd.DataFrame(final_data) 
fd.State_Name.unique()

"""# Weather Data Set"""

weather_path="weather_data.csv"
weather_df=pd.read_csv(weather_path)
weather_df

new_data=weather_df
new_data

new_data["State_Name"].replace({"Gujrat":"Gujarat","Dadra and Nagar Haveli, DN, India":"Dadra and Nagar Haveli","kerala":"Kerala"},inplace=True)

new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2000,'Max Temperature': 25.1, 'Min Temperature': 10.3,'Temperature': 13.2,'Heat Index': 23.2,'Precipitation':234.6,'Wind Speed':72.2,'Visibility': 1.9,'Cloud Cover':66.8,'Relative Humidity':81.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2001,'Max Temperature': 24.6, 'Min Temperature': 11.2,'Temperature': 14.8,'Heat Index': 29.3,'Precipitation':197.2,'Wind Speed':74.2,'Visibility': 2.1,'Cloud Cover':71.1,'Relative Humidity':78.8}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2002,'Max Temperature': 24.9, 'Min Temperature': 11.7,'Temperature': 18.4,'Heat Index': 28.6,'Precipitation':332.8,'Wind Speed':78.4,'Visibility': 3.2,'Cloud Cover':55.8,'Relative Humidity':83.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2003,'Max Temperature': 23.8, 'Min Temperature': 10.6,'Temperature': 17.3,'Heat Index': 28.9,'Precipitation':343.2,'Wind Speed':67.8,'Visibility': 2.8,'Cloud Cover':67.2,'Relative Humidity':79.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2004,'Max Temperature': 25.5, 'Min Temperature': 9.8,'Temperature': 16.2,'Heat Index': 29.9,'Precipitation':298.4,'Wind Speed':69.0,'Visibility': 3.9,'Cloud Cover':69.0,'Relative Humidity':73.7}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2005,'Max Temperature': 25.1, 'Min Temperature': 12.3,'Temperature': 19.2,'Heat Index': 30.2,'Precipitation':534.2,'Wind Speed':58.6,'Visibility': 4.1,'Cloud Cover':70.7,'Relative Humidity':85.6}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2006,'Max Temperature': 24.3, 'Min Temperature': 12.8,'Temperature': 20.0,'Heat Index': 28.0,'Precipitation':433.5,'Wind Speed':65.5,'Visibility': 5.2,'Cloud Cover':75.2,'Relative Humidity':81.9}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2007,'Max Temperature': 23.1, 'Min Temperature': 11.1,'Temperature': 18.1,'Heat Index': 26.6,'Precipitation':257.7,'Wind Speed':59.0,'Visibility': 2.4,'Cloud Cover':76.5,'Relative Humidity':81.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2008,'Max Temperature': 23.9, 'Min Temperature': 12,'Temperature': 17.8,'Heat Index': 25.9,'Precipitation':288.0,'Wind Speed':75.9,'Visibility': 4.2,'Cloud Cover':68.2,'Relative Humidity':76.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2009,'Max Temperature': 24.5, 'Min Temperature': 10.7,'Temperature': 17.1,'Heat Index': 26.7,'Precipitation':380.9,'Wind Speed':74.1,'Visibility': 3.5,'Cloud Cover':66.8,'Relative Humidity':72.3}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Jammu and Kashmir','Crop_Year': 2010,'Max Temperature': 25.3, 'Min Temperature': 9.9,'Temperature': 19.2,'Heat Index': 27.0,'Precipitation':654.3,'Wind Speed':68.8,'Visibility': 2.7,'Cloud Cover':69.1,'Relative Humidity':86.0}
new_data=new_data.append(new_row,ignore_index=True)

new_row={'State_Name': 'Nagaland','Crop_Year': 2000,'Max Temperature': 28.1, 'Min Temperature': 19.3,'Temperature': 23.2,'Heat Index': 38.5,'Precipitation':1634.6,'Wind Speed':72.2,'Visibility': 5.9,'Cloud Cover':66.8,'Relative Humidity':81.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2001,'Max Temperature': 29.6, 'Min Temperature': 20.2,'Temperature': 24.5,'Heat Index': 39.3,'Precipitation':1797.2,'Wind Speed':74.2,'Visibility': 4.1,'Cloud Cover':71.1,'Relative Humidity':78.8}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2002,'Max Temperature': 29.9, 'Min Temperature': 20.7,'Temperature': 24.2,'Heat Index': 38.6,'Precipitation':1332.8,'Wind Speed':78.4,'Visibility': 3.2,'Cloud Cover':55.8,'Relative Humidity':83.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2003,'Max Temperature': 28.8, 'Min Temperature': 19.6,'Temperature': 23.2,'Heat Index': 38.9,'Precipitation':1543.2,'Wind Speed':67.8,'Visibility': 5.8,'Cloud Cover':67.2,'Relative Humidity':79.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2004,'Max Temperature': 30.5, 'Min Temperature': 18.8,'Temperature': 26.7,'Heat Index': 39.9,'Precipitation':1698.4,'Wind Speed':69.0,'Visibility': 4.9,'Cloud Cover':69.0,'Relative Humidity':73.7}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2005,'Max Temperature': 30.1, 'Min Temperature': 21.3,'Temperature': 26.3,'Heat Index': 40.2,'Precipitation':2034.2,'Wind Speed':58.6,'Visibility': 6.2,'Cloud Cover':70.7,'Relative Humidity':85.6}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2006,'Max Temperature': 29.3, 'Min Temperature': 22.8,'Temperature': 27.8,'Heat Index': 38.0,'Precipitation':1833.5,'Wind Speed':65.5,'Visibility': 5.2,'Cloud Cover':75.2,'Relative Humidity':81.9}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2007,'Max Temperature': 27.1, 'Min Temperature': 20.1,'Temperature': 25.2,'Heat Index': 36.6,'Precipitation':2257.7,'Wind Speed':59.0,'Visibility': 4.8,'Cloud Cover':76.5,'Relative Humidity':81.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2008,'Max Temperature': 27.9, 'Min Temperature': 22.0,'Temperature': 23.9,'Heat Index': 35.9,'Precipitation':2088.0,'Wind Speed':75.9,'Visibility': 4.8,'Cloud Cover':68.2,'Relative Humidity':76.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2009,'Max Temperature': 28.5, 'Min Temperature': 19.7,'Temperature': 25.6,'Heat Index': 36.7,'Precipitation':1780.9,'Wind Speed':74.1,'Visibility': 5.5,'Cloud Cover':66.8,'Relative Humidity':72.3}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Nagaland','Crop_Year': 2010,'Max Temperature': 30.3, 'Min Temperature': 18.9,'Temperature': 28.4,'Heat Index': 37.0,'Precipitation':1654.3,'Wind Speed':68.8,'Visibility': 5.7,'Cloud Cover':69.1,'Relative Humidity':86.0}
new_data=new_data.append(new_row,ignore_index=True)

new_row={'State_Name': 'Chandigarh','Crop_Year': 2000,'Max Temperature': 30.1, 'Min Temperature': 21.3,'Temperature': 25.2,'Heat Index': 34.5,'Precipitation':980.6,'Wind Speed':52.2,'Visibility': 5.9,'Cloud Cover':66.8,'Relative Humidity':71.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2001,'Max Temperature': 31.6, 'Min Temperature': 22.2,'Temperature': 26.5,'Heat Index': 42.3,'Precipitation':1000.2,'Wind Speed':54.2,'Visibility': 5.1,'Cloud Cover':71.1,'Relative Humidity':68.8}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2002,'Max Temperature': 31.9, 'Min Temperature': 22.7,'Temperature': 26.2,'Heat Index': 41.6,'Precipitation':1102.8,'Wind Speed':58.4,'Visibility': 5.2,'Cloud Cover':55.8,'Relative Humidity':73.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2003,'Max Temperature': 30.8, 'Min Temperature': 21.6,'Temperature': 25.2,'Heat Index': 41.9,'Precipitation':876.2,'Wind Speed':57.8,'Visibility': 6.8,'Cloud Cover':67.2,'Relative Humidity':69.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2004,'Max Temperature': 32.5, 'Min Temperature': 20.8,'Temperature': 28.7,'Heat Index': 42.9,'Precipitation':902.4,'Wind Speed':59.0,'Visibility': 6.9,'Cloud Cover':69.0,'Relative Humidity':63.7}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2005,'Max Temperature': 32.1, 'Min Temperature': 23.3,'Temperature': 28.3,'Heat Index': 43.2,'Precipitation':1054.2,'Wind Speed':58.6,'Visibility': 6.2,'Cloud Cover':70.7,'Relative Humidity':75.6}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2006,'Max Temperature': 31.3, 'Min Temperature': 24.8,'Temperature': 29.8,'Heat Index': 41.0,'Precipitation':1098.5,'Wind Speed':55.5,'Visibility': 6.2,'Cloud Cover':75.2,'Relative Humidity':71.9}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2007,'Max Temperature': 29.1, 'Min Temperature': 22.1,'Temperature': 27.2,'Heat Index': 39.6,'Precipitation':998.7,'Wind Speed':59.0,'Visibility': 6.8,'Cloud Cover':76.5,'Relative Humidity':71.1}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2008,'Max Temperature': 29.9, 'Min Temperature': 24.0,'Temperature': 25.9,'Heat Index': 38.9,'Precipitation':982.0,'Wind Speed':55.9,'Visibility': 6.8,'Cloud Cover':68.2,'Relative Humidity':66.4}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2009,'Max Temperature': 30.5, 'Min Temperature': 21.7,'Temperature': 27.6,'Heat Index': 39.7,'Precipitation':1002.9,'Wind Speed':54.1,'Visibility': 6.5,'Cloud Cover':66.8,'Relative Humidity':62.3}
new_data=new_data.append(new_row,ignore_index=True)
new_row={'State_Name': 'Chandigarh','Crop_Year': 2010,'Max Temperature': 32.3, 'Min Temperature': 20.9,'Temperature': 30.4,'Heat Index': 40.0,'Precipitation':1201.3,'Wind Speed':58.8,'Visibility': 6.7,'Cloud Cover':69.1,'Relative Humidity':76.0}
new_data=new_data.append(new_row,ignore_index=True)

nd = pd.DataFrame(new_data) 
nd.State_Name.unique()

new_data

df=new_data.merge(final_data,how='left',on=['State_Name','Crop_Year'])
df

df.iloc[190, df.columns.get_loc('Production')] = 208900
df.iloc[191, df.columns.get_loc('Production')] = 142100
df.iloc[192, df.columns.get_loc('Production')] = 126500
df.iloc[193, df.columns.get_loc('Production')] = 134800
df.iloc[250, df.columns.get_loc('Visibility')] = 8.8
df.iloc[259, df.columns.get_loc('Production')] = 118300
df.iloc[308, df.columns.get_loc('Production')] = 1771882
df.iloc[309, df.columns.get_loc('Production')] = 1644700
df.iloc[316, df.columns.get_loc('Production')] = 3336400
df.iloc[317, df.columns.get_loc('Production')] = 3420200
df.iloc[318, df.columns.get_loc('Production')] = 1538400
df.iloc[527, df.columns.get_loc('Production')] = 31000
df.iloc[528, df.columns.get_loc('Production')] = 21900
df.iloc[529, df.columns.get_loc('Production')] = 22100
df.iloc[541, df.columns.get_loc('Visibility')] = 4.7
df.iloc[542, df.columns.get_loc('Visibility')] = 5.1
df.iloc[667, df.columns.get_loc('Production')] = 406200
df.iloc[668, df.columns.get_loc('Production')] = 39700
df.iloc[669, df.columns.get_loc('Production')] = 319941
df.iloc[862, df.columns.get_loc('Production')] = 796416
df.iloc[863, df.columns.get_loc('Production')] = 594719
df.iloc[864, df.columns.get_loc('Production')] = 297610
df.iloc[865, df.columns.get_loc('Production')] = 358144
df.iloc[866, df.columns.get_loc('Production')] = 555128
df.iloc[867, df.columns.get_loc('Production')] = 938666
df.iloc[868, df.columns.get_loc('Production')] = 805904
df.iloc[869, df.columns.get_loc('Production')] = 990000
df.iloc[870, df.columns.get_loc('Production')] = 1150307
df.iloc[871, df.columns.get_loc('Production')] = 918970
df.iloc[872, df.columns.get_loc('Production')] = 1323714
df.iloc[882, df.columns.get_loc('Relative Humidity')] = 73.89
df.iloc[883, df.columns.get_loc('Production')] = 44400
df.iloc[890, df.columns.get_loc('Production')] = 415342
df.iloc[891, df.columns.get_loc('Production')] = 422298
df.iloc[892, df.columns.get_loc('Production')] = 421457
df.iloc[893, df.columns.get_loc('Production')] = 504797
df.iloc[894, df.columns.get_loc('Production')] = 492372
df.iloc[895, df.columns.get_loc('Production')] = 556774
df.iloc[896, df.columns.get_loc('Production')] = 554000
df.iloc[897, df.columns.get_loc('Production')] = 561355
df.iloc[898, df.columns.get_loc('Production')] = 563100
df.iloc[899, df.columns.get_loc('Production')] = 497375
df.iloc[900, df.columns.get_loc('Production')] = 507660
#------------------------------------------------------------------------
df.iloc[190, df.columns.get_loc('Area')] = 59023
df.iloc[191, df.columns.get_loc('Area')] = 57207	
df.iloc[192, df.columns.get_loc('Area')] = 49383
df.iloc[193, df.columns.get_loc('Area')] = 50169
df.iloc[259, df.columns.get_loc('Area')] = 77700
df.iloc[308, df.columns.get_loc('Area')] = 1712400
df.iloc[309, df.columns.get_loc('Area')] = 1693600
df.iloc[316, df.columns.get_loc('Area')] = 1653700
df.iloc[317, df.columns.get_loc('Area')] = 1683600
df.iloc[318, df.columns.get_loc('Area')] = 99500
df.iloc[527, df.columns.get_loc('Area')] = 11000
df.iloc[528, df.columns.get_loc('Area')] = 7300
df.iloc[529, df.columns.get_loc('Area')] = 7900
df.iloc[667, df.columns.get_loc('Area')] = 166100
df.iloc[668, df.columns.get_loc('Area')] = 168400
df.iloc[669, df.columns.get_loc('Area')] = 169400
df.iloc[862, df.columns.get_loc('Area')] = 262301
df.iloc[863, df.columns.get_loc('Area')] = 219587
df.iloc[864, df.columns.get_loc('Area')] = 131668
df.iloc[865, df.columns.get_loc('Area')] = 123008
df.iloc[866, df.columns.get_loc('Area')] = 192692
df.iloc[867, df.columns.get_loc('Area')] = 310697
df.iloc[868, df.columns.get_loc('Area')] = 284276
df.iloc[869, df.columns.get_loc('Area')] = 311000
df.iloc[870, df.columns.get_loc('Area')] = 361812
df.iloc[871, df.columns.get_loc('Area')] = 273430
df.iloc[872, df.columns.get_loc('Area')] = 405315
df.iloc[883, df.columns.get_loc('Area')] = 47200
df.iloc[890, df.columns.get_loc('Area')] = 244051
df.iloc[891, df.columns.get_loc('Area')] = 249830
df.iloc[892, df.columns.get_loc('Area')] = 236199
df.iloc[893, df.columns.get_loc('Area')] = 259815
df.iloc[894, df.columns.get_loc('Area')] = 250044
df.iloc[895, df.columns.get_loc('Area')] = 259014
df.iloc[896, df.columns.get_loc('Area')] = 261094
df.iloc[897, df.columns.get_loc('Area')] = 263246
df.iloc[898, df.columns.get_loc('Area')] = 264490
df.iloc[899, df.columns.get_loc('Area')] = 281002
df.iloc[900, df.columns.get_loc('Area')] = 282021

df

new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2000,'Max Temperature': 29.6, 'Min Temperature': 25.2,'Temperature': 25.2,'Precipitation':0,'Wind Speed':52.2,'Visibility': 4.9,'Cloud Cover':96.8,'Relative Humidity':91.1,'Area':118601,'Production':132690}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2004,'Max Temperature': 30.2, 'Min Temperature': 24.7,'Temperature': 25.3,'Precipitation':0,'Wind Speed':56.9,'Visibility': 4.6,'Cloud Cover':98.8,'Relative Humidity':90.6,'Area':121642,'Production':134950}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2005,'Max Temperature': 28.5, 'Min Temperature': 24.2,'Temperature': 25.6,'Precipitation':0,'Wind Speed':57.2,'Visibility': 4.7,'Cloud Cover':94.8,'Relative Humidity':92.8,'Area':122267,'Production':146191}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2006,'Max Temperature': 29.3, 'Min Temperature': 24.7,'Temperature': 24.7,'Precipitation':0,'Wind Speed':60.9,'Visibility': 4.8,'Cloud Cover':94.2,'Relative Humidity':89.1,'Area':123038,'Production':144635}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2007,'Max Temperature': 30.1, 'Min Temperature': 23.9,'Temperature': 23.9,'Precipitation':0,'Wind Speed':65.2,'Visibility': 5.0,'Cloud Cover':91.0,'Relative Humidity':86.9,'Area':124029,'Production':158146}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2008,'Max Temperature': 29.9, 'Min Temperature': 24.4,'Temperature': 25.0,'Precipitation':0,'Wind Speed':66.9,'Visibility': 5.1,'Cloud Cover':88.8,'Relative Humidity':92.3,'Area':126799,'Production': 164538}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2009,'Max Temperature': 31.4, 'Min Temperature': 22.2,'Temperature': 27.9,'Precipitation':0,'Wind Speed':61.8,'Visibility': 4.4,'Cloud Cover':89.3,'Relative Humidity':90.6,'Area':121468,'Production': 143895}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Arunachal Pradesh','Crop_Year': 2010,'Max Temperature': 28.7, 'Min Temperature': 23.3,'Temperature': 25.8,'Precipitation':0,'Wind Speed':52.9,'Visibility': 4.3,'Cloud Cover':90.1,'Relative Humidity':88.8,'Area':121570,'Production':155993}
df=df.append(new_row,ignore_index=True)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2000,'Max Temperature': 29.8, 'Min Temperature': 28.2,'Temperature': 28.2,'Precipitation':0,'Wind Speed':12.2,'Visibility': 10,'Cloud Cover':36.8,'Relative Humidity':61.1,'Area':10881,'Production':32184}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2001,'Max Temperature': 30.6, 'Min Temperature': 29.0,'Temperature': 29.0,'Precipitation':0,'Wind Speed':22.2,'Visibility': 10,'Cloud Cover':32.8,'Relative Humidity':59.4,'Area':9801,'Production':27333}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2004,'Max Temperature': 30.2, 'Min Temperature': 27.8,'Temperature': 27.8,'Precipitation':0,'Wind Speed':15.2,'Visibility': 10,'Cloud Cover':33.8,'Relative Humidity':63.9,'Area':10734.9,'Production':29192.2}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2006,'Max Temperature': 31.3, 'Min Temperature': 28.0,'Temperature': 28.0,'Precipitation':0,'Wind Speed':18.8,'Visibility': 10,'Cloud Cover':30.1,'Relative Humidity':62.3,'Area':7776.17,'Production':21535.3}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2008,'Max Temperature': 32.1, 'Min Temperature': 27.7,'Temperature': 27.7,'Precipitation':0,'Wind Speed':23.3,'Visibility': 10,'Cloud Cover':27.6,'Relative Humidity':64.7,'Area':7300,'Production':21900}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Dadra and Nagar Haveli','Crop_Year': 2010,'Max Temperature': 32.0, 'Min Temperature': 28.2,'Temperature': 28.2,'Precipitation':0,'Wind Speed':20.2,'Visibility': 10,'Cloud Cover':22.0,'Relative Humidity':55.3,'Area':8390,'Production': 23916}
df=df.append(new_row,ignore_index=True)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
new_row={'State_Name': 'Punjab','Crop_Year': 2000,'Max Temperature': 20.8, 'Min Temperature': 17.2,'Temperature': 18.2,'Precipitation':0,'Wind Speed':12.2,'Visibility': 6,'Cloud Cover':86.8,'Relative Humidity':61.1,'Area':2611000,'Production':9154000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Punjab','Crop_Year': 2001,'Max Temperature': 21.6, 'Min Temperature': 19.0,'Temperature': 19.0,'Precipitation':0,'Wind Speed':22.2,'Visibility': 8,'Cloud Cover':82.8,'Relative Humidity':59.4,'Area':2487000,'Production':8816000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Punjab','Crop_Year': 2004,'Max Temperature': 21.2, 'Min Temperature': 17.8,'Temperature': 17.8,'Precipitation':0,'Wind Speed':15.2,'Visibility': 7,'Cloud Cover':83.8,'Relative Humidity':63.9,'Area':2800000,'Production':10437000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Punjab','Crop_Year': 2006,'Max Temperature': 22.3, 'Min Temperature': 18.0,'Temperature': 18.0,'Precipitation':0,'Wind Speed':18.8,'Visibility': 8,'Cloud Cover':80.1,'Relative Humidity':62.3,'Area':2621000,'Production':10138000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Punjab','Crop_Year': 2007,'Max Temperature': 23.1, 'Min Temperature': 17.7,'Temperature': 17.7,'Precipitation':0,'Wind Speed':23.3,'Visibility': 8,'Cloud Cover':87.6,'Relative Humidity':64.7,'Area':2610000,'Production':10489000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Punjab','Crop_Year': 2008,'Max Temperature': 23.0, 'Min Temperature': 18.2,'Temperature': 18.2,'Precipitation':0,'Wind Speed':20.2,'Visibility': 9,'Cloud Cover':82.0,'Relative Humidity':55.3,'Area':2735000,'Production': 11000000}
df=df.append(new_row,ignore_index=True)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
new_row={'State_Name': 'Mizoram','Crop_Year': 2000,'Max Temperature': 30.8, 'Min Temperature': 27.2,'Temperature': 28.2,'Precipitation':0,'Wind Speed':12.2,'Visibility': 6,'Cloud Cover':86.8,'Relative Humidity':71.1,'Area':50080,'Production':103700}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2001,'Max Temperature': 31.6, 'Min Temperature': 29.0,'Temperature': 29.0,'Precipitation':0,'Wind Speed':22.2,'Visibility': 6,'Cloud Cover':72.8,'Relative Humidity':69.4,'Area':52600,'Production':105700}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2002,'Max Temperature': 31.2, 'Min Temperature': 27.8,'Temperature': 27.8,'Precipitation':0,'Wind Speed':15.2,'Visibility': 5,'Cloud Cover':73.8,'Relative Humidity':73.9,'Area':52100,'Production':109200}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2004,'Max Temperature': 32.3, 'Min Temperature': 28.0,'Temperature': 28.0,'Precipitation':0,'Wind Speed':18.8,'Visibility': 5,'Cloud Cover':60.1,'Relative Humidity':72.3,'Area':51800,'Production':104100}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2005,'Max Temperature': 33.1, 'Min Temperature': 27.7,'Temperature': 27.7,'Precipitation':0,'Wind Speed':23.3,'Visibility': 4.8,'Cloud Cover':67.6,'Relative Humidity':74.7,'Area':52000,'Production':99200}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2006,'Max Temperature': 33.0, 'Min Temperature': 28.2,'Temperature': 28.2,'Precipitation':0,'Wind Speed':20.2,'Visibility': 4.4,'Cloud Cover':72.0,'Relative Humidity':65.3,'Area':53000,'Production':29500 }
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2007,'Max Temperature': 30.8, 'Min Temperature': 27.2,'Temperature': 28.2,'Precipitation':0,'Wind Speed':12.2,'Visibility': 5.2,'Cloud Cover':76.8,'Relative Humidity':71.1,'Area':54600,'Production':15700}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2008,'Max Temperature': 31.6, 'Min Temperature': 29.0,'Temperature': 29.0,'Precipitation':0,'Wind Speed':22.2,'Visibility': 5.8,'Cloud Cover':62.8,'Relative Humidity':69.4,'Area':52000,'Production':46000}
df=df.append(new_row,ignore_index=True)
new_row={'State_Name': 'Mizoram','Crop_Year': 2009,'Max Temperature': 31.2, 'Min Temperature': 27.8,'Temperature': 27.8,'Precipitation':0,'Wind Speed':15.2,'Visibility': 6.7,'Cloud Cover':63.8,'Relative Humidity':73.9,'Area':472000,'Production':44300}
df=df.append(new_row,ignore_index=True)

is_Nan = df.isnull()
row_has_Nan = is_Nan.any(axis=1)
rows_with_Nan = df[row_has_Nan]
rows_with_Nan

df=df.dropna()

df.isnull().sum()

df

df=df[df['State_Name']!='Mizoram']
print(df)

stateNames=df.State_Name.unique()
print(stateNames)
dict_file={'states':stateNames}
print(dict_file)

"""# CNN-LSTM Model"""
print("\n\n---------------------\nCNN-LSTM Model")

clmodel = Sequential()
clmodel.add(TimeDistributed(Conv1D(filters=64, kernel_size=2, activation='relu'), input_shape=(None, 5, 1)))
clmodel.add(TimeDistributed(MaxPooling1D(pool_size=2)))
clmodel.add(TimeDistributed(Flatten()))
clmodel.add(LSTM(50, activation='relu'))
clmodel.add(Dense(1))
clmodel.compile(optimizer='adam', loss='mse', metrics=[keras.metrics.MeanAbsoluteError()])
print("Model Summary")
print(clmodel.summary())

model_json=clmodel.to_json()
with open("model.json","w") as json_file:
  json_file.write(model_json)

"""# Training for all States"""

mae=[]
n_columns=11
for i in range(len(stateNames)):
  print("\n\n---------------------------\n",stateNames[i],"\n---------------------------")
  tmp_dict={}
  s_df=df[df['State_Name']==stateNames[i]]
  years=s_df.Crop_Year.unique();
  print(years)
  print(s_df)
  s_df=s_df[['Max Temperature','Min Temperature','Temperature','Heat Index','Precipitation','Wind Speed','Visibility','Cloud Cover','Relative Humidity','Area','Production']]
  s_df.columns=['Max Temperature','Min Temperature','Temperature','Heat Index','Precipitation','Wind Speed','Visibility','Cloud Cover','Relative Humidity','Area','Production']
  values = s_df.values
  plt.figure(figsize=(8, 20))
  for j in range(n_columns):
    tmp_dict[s_df.columns[j]]=values[:,j]
    plt.subplot(n_columns, 1, j+1)
    plt.plot(years,values[:,j])
    plt.title(s_df.columns[j],y=.5,loc='right')
  #plt.tight_layout()
  spttl="Plot of different statistics for "+stateNames[i]+" in different years"
  plt.suptitle(spttl)
  plt.show() 
  dict_file[stateNames[i]]=tmp_dict
  print(s_df.shape)
  print("Splitting Dataset into X and Y")
  s_df=s_df.to_numpy()
  x=s_df[:,0:10]
  print(x.shape)
  print(x)
  y=s_df[:,9]
  print(y.shape)
  print(y)
  print("Splitting into Test and Training")
  x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)
  print("x_train.shape = ",x_train.shape)
  print("y_train.shape = ",y_train.shape)
  print("x_test.shape",x_test.shape)
  print("y_test.shape",y_test.shape)
  print("Reshaping Testing and Training Dataset")
  x_train = x_train.reshape((x_train.shape[0], 2, 5, 1))
  x_test = x_test.reshape((x_test.shape[0], 2, 5, 1))
  print(x_train.shape)
  print(x_test.shape)
  print("Training the model for ",stateNames[i])
  history=clmodel.fit(x_train, y_train, epochs=2000, verbose=1)
  print("Evaluating Model")
  eval=clmodel.evaluate(x_test,y_test,verbose=1)
  mae.append(eval[1])
  print(mae)
  print(len(mae))
  print("Model Loss")
  print(history.history.keys())
  #plt.plot(history.history['loss'])
  plt.plot(history.history['mean_absolute_error'])
  modelLossTitle="Training Model Loss for "+stateNames[i]+""
  plt.title(modelLossTitle)
  plt.ylabel("Loss")
  plt.xlabel('Epochs')
  plt.legend(['train'],loc='upper left')
  plt.show()
  print("Mean Absolute Error = ",eval[1])
  print("Making Prediction for given Test Dataset")
  cl_pred=clmodel.predict(x_test)
  wt=clmodel.get_weights()
  #print("weights")
  #print(wt)
  cl_pred=cl_pred.reshape(x_test.shape[0],)
  print("Predicted")
  print(cl_pred)
  print("\nReal")
  print(y_test)
  plt.figure(figsize=(10,10))
  plt.plot(y_test)
  plt.plot(cl_pred) 
  plt.title(stateNames[i])
  plt.legend(['Real','Predicted'])
  plt.show()
  filePath='weights/'
  '''for k in range(len(stateNames[i])):
  	c=stateNames[i][k]
  	if(c==' '):
  		c='_'
  	filePath+=stateNames[i][k]'''
  filePath+=stateNames[i]
  filePath+='_model.hdf5'
  clmodel.save(filePath)

plt.figure(figsize=(50, 6))
plt.plot(mae)
plt.title('Mean Absolute Error')
plt.ylabel("Mean Absolute Error")
plt.xlabel('State Number')
plt.show()
dict_file

#with open("json_file.json","w") as json_file:
#  json.dump(dict_file,json_file)