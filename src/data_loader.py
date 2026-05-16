import pandas as pd

class load_csv:
    def __init__(self, df) -> None:
        self.df = df
    
    def load_data(self):
        self.data = pd.read_csv(self.df)
        return self.data 

