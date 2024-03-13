import pandas as pd
import seaborn as sns 
import matplotlib as mpl 
import matplotlib.pyplot as plt 

ruta = r'qsqn.csv'
dataframe = pd.read_csv(ruta)

#Creacion de histogramas con la frecuencia de aparición de cada clasificación
plt.figure(figsize=(10,6))
sns.histplot(data=dataframe, x='qs_ERH', discrete=True, shrink=0.8)
plt.title('Histograma de clasificación para el ERH', fontsize=20)
plt.xlabel('Clasificación')
plt.ylabel('Frecuencia')
plt.savefig('Hist_ERH.png')

#Creacion de histogramas con la frecuencia de aparición de cada clasificación
plt.figure(figsize=(10,6))
sns.histplot(data=dataframe, x='qs_rms', discrete=True, shrink=0.8, stat='percent')
plt.title('Histograma de clasificación para el RMS', fontsize=20)
plt.xlabel('Clasificación')
plt.ylabel('Frecuencia')
plt.savefig('Hist_RMS.png')

#Creacion de histogramas con la frecuencia de aparición de cada clasificación
plt.figure(figsize=(10,6))
sns.histplot(data=dataframe, x='qs_ERZ', discrete=True, shrink=0.8)
plt.title('Histograma de clasificación para el ERZ', fontsize=20)
plt.xlabel('Clasificación')
plt.ylabel('Frecuencia')
plt.savefig('Hist_ERZ.png')

#Creacion de histogramas con la frecuencia de aparición de cada clasificación
plt.figure(figsize=(10,6))
sns.histplot(data=dataframe, x='qn_GAP', discrete=True, shrink=0.8)
plt.title('Histograma de clasificación para el GAP', fontsize=20)
plt.xlabel('Clasificación')
plt.ylabel('Frecuencia')
plt.savefig('Hist_GAP.png')




