# 🧠 Student Depression Prediction

![Python](https://img.shields.io/badge/Python-blue)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-red)

## 🌐 Live Demo
👉 [Click here to try the app](https://student-depression-prediction-ckgym2pcykuprbh9xehlb4.streamlit.app/)

---

## 📌 Project Overview
A machine learning web application that predicts the likelihood of depression in students based on their lifestyle, academic, and personal factors. The app takes user inputs and instantly predicts whether a student is likely to be depressed or not, along with a confidence score.

---

## Project Structure

```
├── app.py                                    # Streamlit frontend
├── project notebook.ipynb                    # Full training pipeline 
├── depression_model.pkl                      # Trained model
└── requirements.txt                          # Dependencies
```

---

## 📂 Dataset

- **Source:** \[Student Depression Dataset - Kaggle](https://www.kaggle.com/datasets/hopesb/student-depression-dataset/data)
- **Total Rows:** 27,901
- **Total Columns:** 18
- **Target Variable:** Depression (0 = No Depression, 1 = Depression)
- **Class Distribution:** 58.5% Depression, 41.5% No Depression

---

## ✅ Features Used

### Numerical Features

| Feature | Description |
|---|---|
| Age | Age of the student (18-59) |
| Academic Pressure | Level of academic pressure (0-5) |
| Study Satisfaction | Level of study satisfaction (0-5) |
| Work/Study Hours | Daily work or study hours (0-12) |
| Financial Stress | Level of financial stress (1-5) |

### Categorical Features

| Feature | Values |
|---|---|
| Sleep Duration | Less than 5 hours, 5-6 hours, 7-8 hours, More than 8 hours |
| Dietary Habits | Unhealthy, Moderate, Healthy |
| Suicidal Thoughts | Yes, No |
| Family History of Mental Illness | Yes, No |

---

## 🔬 Methodology
### 1. Exploratory Data Analysis (EDA)
- Analyzed class distribution of target variable
- Used histplots with proportion fill for numerical features
- Used crosstab with normalize='index' for categorical features
- Analyzed mean values per class for numerical features
- Checked correlation matrix for multicollinearity

### 2. Feature Selection
- Dropped identifier column (id)
- Dropped columns with near zero variance (Work Pressure, Job Satisfaction)
- Dropped columns with no signal (CGPA, Gender, City, Profession, Degree)
- Kept features with strong data signal AND real world relevance

### 3. Data Preprocessing
- Handled 3 missing values in Financial Stress by dropping rows
- Removed invalid categories (Others) from Sleep Duration and Dietary Habits
- Applied StandardScaler on numerical features
- Applied OrdinalEncoder with correct category order on ordinal features
- Applied binary mapping (Yes=1, No=0) on binary features
- Used ColumnTransformer with remainder='passthrough' for clean pipeline

### 4. Model Building
- Established DummyClassifier baseline (F1 = 0.5841)
- Trained and compared 7 models:
  - Logistic Regression
  - KNN
  - SVM
  - Decision Tree
  - Random Forest
  - XGBoost
  - Gradient Boosting
- Used 5-fold cross validation with F1 scoring
- Monitored both Train and Validation F1

### 5. Hyperparameter Tuning
- Selected top 3 models based on validation F1 and consistency
- Used GridSearchCV with cv=5 and f1 scoring
- Tuned Logistic Regression, SVM and Gradient Boosting

### 6. Final Model
- Retrained best model (Logistic Regression) on full dataset
- Saved using joblib

---

## 📊 Model Performance
### Model Comparison

| Model | Train F1 | Validation F1 | Verdict |
|---|---|---|---|
| Dummy Classifier | — | 0.5841 | Baseline |
| Logistic Regression | 0.8703 | 0.8700 | ✅ Best |
| KNN | 0.8898 | 0.8495 | ⚠️ Mild Overfitting |
| SVM | 0.8737 | 0.8678 | ✅ Consistent |
| Decision Tree | 0.9979 | 0.8003 | ❌ Overfitting |
| Random Forest | 0.9979 | 0.8567 | ❌ Overfitting |
| XGBoost | 0.9100 | 0.8586 | ⚠️ Mild Overfitting |
| Gradient Boosting | 0.8749 | 0.8693 | ✅ Consistent |

### Then we checked the test scores and based on that Logistic Regression was chosen

### Final Model Results (Logistic Regression)

| Metric | Score |
|---|---|
| Train F1 | 0.8709 |
| Validation F1 | 0.8710 |
| Test F1 | 0.8776 |
| Accuracy | 0.85 |
| Recall (Depression) | 0.90 |
| AUC | 0.92 |

---

## 🛠️ Technologies Used
| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas | Data manipulation |
| NumPy | Numerical computing |
| Matplotlib & Seaborn | Data visualization |
| Scikit-learn | ML models and preprocessing |
| Joblib | Model serialization |
| Streamlit | Web application deployment |

---

## ⚠️ Limitations
- Dataset is limited to student population — may not generalize to other groups
- Depression is a complex medical condition — this model should not be used as a substitute for professional medical diagnosis
- Model is based on synthetic dataset which may contain bias
- Model achieves 90% recall but still misses 10% of depression cases — real world deployment requires human expert validation

---

## Author

Rajat — [GitHub](https://github.com/rajat-datasci)
