import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

class model:
    def __init__(self, df) -> None:
        self.df = df
    
    def unsupervised_model(self, df):
        
        self.kmean = KMeans(n_clusters=5, random_state=42, n_init='auto')
        self.d = self.df['Student_profile'] = self.kmean.fit_predict(self.df[['study_hours_per_week', 'attendance_rate']])

        centroid = pd.DataFrame(self.kmean.cluster_centers_, columns=['avg study_Hr', 'AVG_attendance_rate'])
        print(centroid.round(2))
        return

