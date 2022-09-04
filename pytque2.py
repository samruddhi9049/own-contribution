import matplotlib.pyplot as plt #matplotlib(python visualization package or library) pyplot is python module in matplotlib 
import matplotlib as mpl #matplotlib package
import matplotlib.animation as animation #animation module from mpl package
import matplotlib.axis as axs #axis module from mpl package
import pandas as pd #pandas package of python
import numpy as np #python's package for scientific computing
import seaborn as sns #statistical plotting library 

from matplotlib import rc
rc('animation', html='jshtml')
hotel_booking_df=pd.read_csv(https://drive.google.com/file/d/1wuF1pJKO4pleroRKXygX9ekp8YWOj53M/view)


plt.figure(figsize=(20,10))
sns.countplot(x=hotel_booking_df['required_car_parking_spaces'])
plt.title('percentage of required_car_parking_spaces')
plt.xlabel('numbers of customers')
plt.ylabel('count')

from locale import normalize
hotel_booking_df['required_car_parking_spaces'].value_counts(normalize=True)

hotel_booking_df['required_car_parking_spaces'].value_counts().plot.pie(explode=(0.05,0.05,0.05,0.05,0.05),autopct='%1.1f%%',shadow=False,figsize=(14,8),fontsize=25,labels=None)
labels=hotel_booking_df['required_car_parking_spaces'].value_counts().index.tolist()
plt.legend(bbox_to_anchor=(0.085,1),loc='upper left',labels=labels)

