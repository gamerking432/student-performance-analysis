from src.data_loader import load_csv
from src.preprocessor import clean
from src.UnSupervised_models import model
from src.visualization import Visualise
from src.Supervised_model import soopervised_model

if __name__ == "__main__":
    loader = load_csv(df="Data/student_performance.csv")
    data = loader.load_data()

    cleaner = clean(df=data)
    data = cleaner.clean_data()

    
    agent = model(df=data)
    agent.unsupervised_model(df=data)

    vis = Visualise(df=data)
    vis.Visualisation()

    data = agent.df

    supr_model = soopervised_model(df=data)
    supr_model.supervised_model(X=data)





