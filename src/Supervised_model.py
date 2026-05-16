from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

class soopervised_model:
    def __init__(self, df) -> None:
        self.df = df

    def supervised_model(self, X):
        x = X[['study_hours_per_week', 'attendance_rate', 'Student_profile']]
        y = X[['final_score']]

        X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)  # Use transform, not fit_transform

        model = LinearRegression()
        model.fit(X_train_scaled, y_train)

        # Get predictions for all data
        X_all_scaled = scaler.transform(x)
        predictions = model.predict(X_all_scaled)
        print(predictions)

        # Evaluate model
        test_pred = model.predict(X_test_scaled)
        r2 = r2_score(y_test, test_pred)
        rmse = np.sqrt(mean_squared_error(y_test, test_pred))

        # print('='*80)
        # print('SUPERVISED LEARNING - LINEAR REGRESSION')
        # print('='*80)
        # print(f'R² Score: {r2:.4f}')
        # print(f'RMSE: {rmse:.2f}')
        # print(f'Coefficients: study_hours={model.coef_[0][0]:.4f}, attendance={model.coef_[0][1]:.4f}, profile={model.coef_[0][2]:.4f}')


        X['Predicted_Score'] = np.round(predictions.flatten(), 1)
        print(X[['study_hours_per_week', 'attendance_rate', 'final_score', 'Predicted_Score']].head(15))