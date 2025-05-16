# Medical-Insurance-Tracker
# 🏥 Medical Insurance Expense Prediction

## 🔍 Problem Statement

The objective of this project is to build an end-to-end machine learning solution that can predict future medical expenses based on individual attributes such as age, BMI, number of children, smoking habits, and geographical region. This predictive system will assist medical insurance companies in making data-driven decisions when calculating insurance premiums.

By analyzing historical data on medical charges and various personal and demographic features, the model aims to establish meaningful relationships between these variables and forecast future costs effectively.

---

## 📊 Project Overview

This project demonstrates the complete lifecycle of a Machine Learning project using structured ML pipeline architecture. It includes stages such as:

- **Data Ingestion** from CSV and NoSQL (MongoDB)
- **Data Validation** for schema and missing values
- **Data Transformation** including encoding, scaling
- **Model Training & Evaluation**
- **Prediction Pipeline**
- **Logging, Exception Handling & Modular Code Structure**

---

## 🛠️ Tech Stack

- **Language**: Python
- **ML Libraries**: Pandas, NumPy, Scikit-learn, Matplotlib
- **Database**: MongoDB (NoSQL) for storing and retrieving data
- **Tools & Frameworks**: 
  - PyMongo for MongoDB connection
  - Logging & Custom Exception Handling
  - Modular project structure with proper abstraction

---

## 🧠 ML Pipeline Stages

### ✅ 1. Data Ingestion
- Loads raw data from a `.csv` file
- Stores the data in a MongoDB collection
- Also saves a local copy for reproducibility

### ✅ 2. Data Validation
- Checks for:
  - Missing values
  - Schema validation
  - Duplicate entries

### ✅ 3. Data Transformation
- Label encoding for categorical variables (e.g., sex, smoker, region)
- Feature scaling using StandardScaler
- Train-test split

### ✅ 4. Model Training
- Trained using **Linear Regression**, **Random Forest**, and other regressors
- Model evaluation using:
  - R² Score
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)

### ✅ 5. Prediction
- Accepts user inputs
- Applies preprocessing and predicts future medical expenses

---

## 📁 Project Structure

```bash
Medical-Insurance-Tracker/
│
├── main.py                          # Entry point of the application
├── requirements.txt                # Required libraries
├── config/                         # Configuration settings
├── Insurance/
│   ├── components/                 # Core pipeline components
│   ├── pipeline/                   # Training and prediction pipeline
│   ├── logger/                     # Custom logging
│   ├── exception/                  # Custom exception handling
│   └── utils.py                    # Utility functions
└── artifacts/                      # Stores outputs like models, transformed data
