Python 3.10.5 (tags/v3.10.5:f377153, Jun  6 2022, 16:14:13) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

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


plt.figure(figsize=(30,10))
sns.countplot(x=hotel_booking_df['meal'])
plt.title('preferred meal type')
plt.xlabel('Type of meal needed in hotel')
plt.ylabel('count')

left',labels=labels)hotel_booking_df['meal'].value_counts().plot.pie(explode=(0.05,0.05,0.05,0.05,0.05),autopct='%1.1f%%',shadow=False,figsize=(14,8),fontsize=25,labels=None)
plt.title("%Distribution of meal",fontsize=20)
labels=hotel_booking_df['meal'].value_counts().index.tolist()
plt.legend(bbox_to_anchor=(0.085,1),loc='upper          
           
