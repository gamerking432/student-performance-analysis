# 🎓 Student Performance Analysis & Prediction

An end-to-end machine learning pipeline for analyzing student learning behavior and predicting academic performance using **unsupervised** and **supervised machine learning models**.

This project identifies student study patterns, generates behavioral profiles through clustering, and predicts final academic scores based on performance-related factors.

---

## 📌 Overview

This project is designed to analyze student habits and predict academic outcomes by combining:

- **Unsupervised Learning** for student behavioral profiling
- **Supervised Learning** for final score prediction
- **Data Visualization** for analytical insights
- **Modular Architecture** for maintainability and scalability

The system evaluates student performance using key features such as:

- Study Hours per Week
- Attendance Rate
- Behavioral Cluster (Student Profile)

---

## 🚀 Features

### Student Behavioral Profiling
Groups students into clusters based on learning patterns and habits.

### Performance Prediction
Predicts final student scores using **Linear Regression**.

### Data Visualization
Generates visual insights into trends, clusters, and feature relationships.

### Modular Pipeline
Well-structured object-oriented design for easy extension and maintenance.

---

## 🏗 Pipeline Architecture

The project follows a modular workflow:

### 1. Data Loading
**Module:** `src/data_loader.py`

Responsible for:

- Loading CSV datasets
- Converting data into Pandas DataFrames
- Initial validation

---

### 2. Data Preprocessing
**Module:** `src/preprocessor.py`

Handles:

- Missing values
- Data cleaning
- Formatting consistency
- Feature preparation

---

### 3. Unsupervised Learning
**Module:** `src/UnSupervised_models.py`

Performs clustering to identify similar student behavior patterns.

**Output:**
`Student_profile`

This feature represents clustered student behavior categories.

---

### 4. Visualization
**Module:** `src/visualization.py`

Generates plots for:

- Feature distributions
- Cluster analysis
- Performance trends

---

### 5. Supervised Learning
**Module:** `src/Supervised_model.py`

Uses **Linear Regression** to predict:

**Target Variable:**  
`final_score`

**Input Features:**

- `study_hours_per_week`
- `attendance_rate`
- `Student_profile`

**Evaluation Metrics:**

- R² Score
- RMSE (Root Mean Square Error)

---

## 📂 Project Structure

```bash
Student_performance/
├── Data/
│   └── student_performance.csv
├── src/
│   ├── data_loader.py
│   ├── preprocessor.py
│   ├── UnSupervised_models.py
│   ├── Supervised_model.py
│   └── visualization.py
└── main.py
```

---

## 🛠 Requirements

Python **3.8+**

Required libraries:

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn

Install dependencies:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn
```

---

## ▶️ Usage

Run the complete pipeline:

```bash
python main.py
```

---

## ⚙️ Execution Workflow

When `main.py` is executed:

### Step 1: Load Dataset
Loads:

```bash
Data/student_performance.csv
```

---

### Step 2: Clean Data

The preprocessing module:

- Handles missing values
- Ensures data consistency
- Prepares features

---

### Step 3: Generate Student Profiles

The unsupervised learning model:

- Detects behavioral patterns
- Assigns cluster-based profiles

---

### Step 4: Visualize Insights

Generates visual plots for:

- Cluster distributions
- Feature correlations
- Analytical trends

---

### Step 5: Train Prediction Model

The supervised learning model:

- Scales data
- Splits train/test sets
- Trains Linear Regression
- Evaluates model performance
- Displays predicted vs actual scores

---

## 🔄 Workflow Diagram

```text
Raw Dataset
    ↓
Data Preprocessing
    ↓
Behavior Clustering
    ↓
Student Profile Generation
    ↓
Visualization
    ↓
Linear Regression Prediction
    ↓
Performance Evaluation
```

---

## 📊 Learning Outcomes

This project demonstrates:

- Data preprocessing pipelines
- Feature engineering
- Clustering techniques
- Regression modeling
- Model evaluation
- Modular ML project design

---

## 🔮 Future Improvements

Potential enhancements:

- Random Forest Regression
- XGBoost implementation
- Hyperparameter tuning
- Model deployment with Flask / FastAPI
- Interactive dashboard integration
- Real-time prediction API

---

## 📖 Technologies Used

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Matplotlib**
- **Seaborn**

---

## 👨‍💻 Author

Student Performance Analysis & Prediction  
Machine Learning Project

Built for practical exploration of educational data analysis and predictive modeling.
