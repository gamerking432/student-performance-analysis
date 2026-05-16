import matplotlib.pyplot as plt
import seaborn as sns

class Visualise:
    def __init__(self, df) -> None:
        self.df = df

    def Visualisation(self):

        plt.figure(figsize=(9,8))
        sns.scatterplot(data=self.df, x='study_hours_per_week', y='attendance_rate', hue='Student_profile', palette='deep', s=100, alpha=0.7)
        plt.show()