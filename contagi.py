# Esercizio di TRMD.
# Vorrei plottere l'andamento dei contagi covid di una data regione nel tempo.

# Pacchetti necessari

import pandas as pd
import matplotlib.pyplot as mpl

# Importo da una tabella le colonne relative al tempo [0], regione[3], [contagi]

data = pd.read_csv('TEST.csv',
                   index_col = 0,
                   sep = ',',
                   parse_dates = True,
                   usecols = [0, 2, 10])

# Creo una classe con una funzione che mi fornisca il plot che cerco in base alla regione

class tabella():

    """Una classe con lo scopo di fornire il plot di un dataframe"""

    def __init__(self, t):
        self.table = t

    def plot(self, x):
        reg = self.table[self.table["codice_regione"] == x]
        mpl.plot(reg['totale_positivi'])
        mpl.savefig('contagi.png')
        
# Creo un oggetto a partire dal dataframe con i dati del covid
# e provo a plottare i dati relativi ad una certa regione

tab = tabella(data)
print("TABELLA",tab.table.head())
tab.plot(6)