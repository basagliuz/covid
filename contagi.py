import pandas as pd

cov = pd.read_table('TEST.csv', header = 0, sep = ',', index_col = 'data', parse_dates = True)
tab = tabella(cov)

class tabella():

    """Una classe costruita per plottare grafici"""

    table: pd.DataFrame

    def __init__(self, t: pd.DataFrame):
        self.table = t

    def plot(self, x: str):
        self.table[self.table["denominazione_regione"] == "Friuli Venezia Giulia"].plot()

tab = tabella(data)
tab.plot('Friuli Venezia Giulia')