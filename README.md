# Student Performance Analysis and Prediction

## Overview
This project is an end-to-end machine learning pipeline designed to analyze student habits and predict their academic performance. By leveraging both unsupervised and supervised machine learning techniques, the system categorizes student behavior and predicts final scores based on study hours, attendance, and behavioral clusters.

## Pipeline Architecture
The project follows a modular, object-oriented design split into several key stages:

1. **Data Loading (`src.data_loader`)**: Ingests raw dataset from the CSV files.
2. **Preprocessing (`src.preprocessor`)**: Cleans the data and handles any missing values or formatting issues.
3. **Unsupervised Learning (`src.UnSupervised_models`)**: Analyzes the dataset to group similar data points, ultimately generating a `Student_profile` feature.
4. **Visualization (`src.visualization`)**: Provides visual insights into the dataset and the newly created student profiles.
5. **Supervised Learning (`src.Supervised_model`)**: Utilizes a Linear Regression model (evaluated via R² and RMSE) to predict a student's `final_score` based on `study_hours_per_week`, `attendance_rate`, and `Student_profile`.

## Project Structure

```text
Student_performance/
├── Data/
│   └── student_performance.csv       # Raw dataset
├── src/
│   ├── data_loader.py                # Handles CSV ingestion
│   ├── preprocessor.py               # Data cleaning logic
│   ├── UnSupervised_models.py        # Clustering algorithms (Student Profiling)
│   ├── Supervised_model.py           # Linear Regression predictive model
│   └── visualization.py              # Data visualization and plotting
└── main.py                           # Main execution script
```

## Requirements

To run this project, you will need Python 3.8+ and the following libraries:
- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib` / `seaborn` (for visualization)

You can install these dependencies using pip:
```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

## Usage

To execute the entire pipeline, simply run the `main.py` script from the root directory:

```bash
python main.py
```

### What happens when you run `main.py`:
1. The raw dataset (`Data/student_performance.csv`) is loaded into a Pandas DataFrame.
2. The data cleaner processes the DataFrame to ensure data integrity.
3. The unsupervised learning agent runs, assigning a `Student_profile` to each student.
4. The visualization module generates plots based on the cleaned and clustered data.
5. The supervised learning model scales the data, splits it into training and testing sets, trains a Linear Regression model, and finally prints a preview of the actual vs. predicted final scores.
