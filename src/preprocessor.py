import pandas as pd

class clean:
    def __init__(self, df) -> None:
        self.df = df

    def clean_data(self):
        self.features = ['study_hours_per_week', 'attendance_rate', 'final_score']
        self.X = self.df[self.features]
        return self.X
    

