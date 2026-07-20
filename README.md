# 🏠 House Rent Prediction using Machine Learning

## Overview

This project is a Machine Learning application that predicts the monthly rent of residential properties based on property characteristics such as location, size, furnishing status, tenant preference, and other housing features. The project demonstrates an end-to-end data science workflow, from data preprocessing and feature engineering to model development, evaluation, and deployment.

Several regression algorithms were trained and compared to identify the best-performing model for accurate rent prediction.

---

## Features

- Data cleaning and preprocessing
- Exploratory Data Analysis (EDA)
- Feature engineering
- Multiple regression models
- Model performance comparison
- House rent prediction using trained models
- Interactive Streamlit web application
- Deployment-ready project structure

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Joblib
- Matplotlib
- Streamlit

---

## Dataset

The dataset contains rental property listings with various property attributes.

### Features

- BHK
- Size (Square Feet)
- Bathroom
- City
- Area Type
- Furnishing Status
- Tenant Preferred
- Floor
- Total Floors

### Target Variable

- Rent

---

## Project Workflow

### 1. Data Collection

- Load dataset
- Explore data structure
- Handle missing values
- Remove duplicates

---

### 2. Data Preprocessing

The dataset was prepared by:

- Cleaning missing values
- Removing unnecessary columns
- Encoding categorical variables
- Creating additional features
- Splitting features and target variable

---

### 3. Exploratory Data Analysis (EDA)

Performed data visualization and analysis to understand:

- Rent distribution
- City-wise rental prices
- Effect of furnishing status
- Property size vs rent
- Correlation between variables
- Outlier detection

---

### 4. Feature Engineering

Categorical variables were transformed using:

- One-Hot Encoding

Numerical features were scaled where appropriate.

---

### 5. Model Training

The following regression models were trained and evaluated:

- Linear Regression
- Ridge Regression
- Random Forest Regressor
- Support Vector Regressor (SVR)
- XGBoost Regressor
- LightGBM Regressor
- CatBoost Regressor

---

### 6. Model Evaluation

Models were evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

The best-performing model was selected and saved for deployment.

---

## Project Structure

```
House-Rent-Prediction/
│
├── data/
│   └── House_Rent_Dataset.csv
│
├── models/
│   ├── xgboost_model.pkl
│   ├── lightgbm_model.pkl
│   ├── catboost_model.pkl
│   └── onehot_encoder.pkl
│
├── notebooks/
│   └── House_Rent_Prediction.ipynb
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/house-rent-prediction.git
```

Navigate to the project directory

```bash
cd house-rent-prediction
```

Install the required dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Launch the Streamlit application

```bash
streamlit run app.py
```

The application allows users to:

- Enter property details
- Select a Machine Learning model
- Predict the estimated monthly rent instantly

---

## Example Prediction

### Input

| Feature | Value |
|---------|------|
| BHK | 3 |
| Size | 1800 |
| Bathroom | 2 |
| City | Bangalore |
| Area Type | Super Area |
| Furnishing | Semi-Furnished |
| Tenant Preferred | Family |
| Floor | 2 |

### Predicted Output

```
Estimated Monthly Rent:
₹32,850
```

*(Prediction values are illustrative.)*

---

## Model Comparison

The project compares multiple regression algorithms to determine the most accurate model for house rent prediction based on evaluation metrics.

Models compared include:

- Linear Regression
- Ridge Regression
- Random Forest
- Support Vector Regressor
- XGBoost
- LightGBM
- CatBoost

---

## Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Machine Learning
- Regression Modeling
- Model Evaluation
- Hyperparameter Tuning
- Model Deployment
- Streamlit Development
- Data Visualization
- Python Programming

---

## Future Improvements

- Integrate real-time property listings
- Add geographic mapping features
- Include additional property characteristics
- Deploy the application to Streamlit Community Cloud
- Create a REST API using FastAPI or Flask
- Improve prediction accuracy through ensemble learning

---

## Author

**Avhakholwi Maladze**

Data Scientist | Machine Learning Engineer | Data Analyst

- LinkedIn: *Add your LinkedIn profile*
- GitHub: *Add your GitHub profile*

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Streamlit
- Pandas
- NumPy
- Open-source Machine Learning community

- https://rentprediction-factfqn98kdihkylspfeue.streamlit.app/
