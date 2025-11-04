# Fraud Detection System for Financial Transactions

**Dataset Link:** [Kaggle](https://www.kaggle.com/datasets/ealaxi/paysim1)

**Reference:** [GitHub](https://github.com/EdgarLopezPhD/PaySim?tab=readme-ov-file)

**GitHub Repository:** [Fraud Detection System](https://github.com/PRIYAtechky/Fraud-Detection-System-for-Financial-Transaction)

## Tech Stack Used
<p align="left">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask" />
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas" />
  <img src="https://img.shields.io/badge/Scikit--learn-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white" alt="Scikit-learn" />
  <img src="https://img.shields.io/badge/XGBoost-EB0028?style=for-the-badge&logo=xgboost&logoColor=white" alt="XGBoost" />
  <img src="https://img.shields.io/badge/Machine_Learning-0078D4?style=for-the-badge&logo=databricks&logoColor=white" alt="Machine Learning" />
</p>


## Problem Statement
Financial institutions face challenges in detecting and preventing fraudulent transactions. UPI-based financial fraud leads to significant monetary losses.

## Project Overview
This project aims to detect fraudulent financial transactions in real time using machine learning. It leverages AI/ML models to analyze transaction patterns, ensuring scalability and adaptability to emerging fraud tactics. A web application built with Flask provides an interface for users to input transaction details and receive fraud risk predictions.

## Objective & Solution Approach
- Develop an AI/ML model to analyze transaction patterns and detect fraud in real time.
- Ensure scalability for handling large transaction volumes.
- Implement adaptive learning for detecting emerging fraud patterns.

## Technology & Models Used
### Machine Learning Models:
- Logistic Regression
- Decision Tree
- K-Nearest Neighbors (KNN)
- Random Forest
- Naïve Bayes
- XGBoost (Best Performing)

## Implementation
### Dataset Features:
- Transaction type, amount, source & destination balances, timestamp

### Preprocessing:
- Feature engineering, normalization using `scaler.pkl`

### Model Training & Evaluation:
- Trained on historical transaction data
- Best accuracy achieved using XGBoost

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/PRIYAtechky/Fraud-Detection-System-for-Financial-Transaction.git
   ```
2. Navigate to the project directory:
   ```sh
   cd Fraud-Detection-System-for-Financial-Transaction
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## How to Use
1. **Update File Paths:**
   - Open `app.py` and update the file paths for `scaler.pkl`, `xgb_model.pkl`, and `column_names.pkl` to match your system's directory structure.
   ```python
   with open(r'path/to/scaler.pkl', 'rb') as file:
       scaler = pickle.load(file)
   
   with open(r'path/to/xgb_model.pkl', 'rb') as file:
       model = pickle.load(file)
   
   with open(r'path/to/column_names.pkl', 'rb') as file:
       column_names = pickle.load(file)
   ```
2. **Run the Flask application:**
   ```sh
   python app.py
   ```
3. **Access the Web Application:**
   - Once `app.py` runs successfully, it will display a local server address in the output.
   - Open your browser and enter the URL provided in the terminal (default: `http://127.0.0.1:5000/`).
4. **Input transaction details** to check for fraud risk.


