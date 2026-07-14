
import streamlit as st
import pandas as pd
import joblib

# Load all models
models = {
    "XGBoost": joblib.load("xgboost_model.pkl"),
    "LightGBM": joblib.load("lightgbm_model.pkl"),
    "CatBoost": joblib.load("catboost_model.pkl")
}

st.title("🏠 House Rent Prediction App Avhakholwi")

# Model selection
selected_model_name = st.selectbox(
    "Choose Model",
    list(models.keys())
)
model = models[selected_model_name]

# Input fields
BHK = st.number_input("BHK", 1, 10, 2)
Size = st.number_input("Size (sq ft)", 100, 10000, 1000)
Bathroom = st.number_input("Bathroom", 1, 10, 2)

Area_Type = st.selectbox("Area Type", ["Super Area", "Carpet Area", "Built Area"])
City = st.selectbox("City", ["Kolkata", "Mumbai", "Bangalore", "Delhi", "Chennai", "Hyderabad"])
Furnishing = st.selectbox("Furnishing Status", ["Unfurnished", "Semi-Furnished", "Furnished"])
Tenant = st.selectbox("Tenant Preferred", ["Bachelors/Family", "Bachelors", "Family"])
Floor = st.selectbox(
    "Floor",
    [
     'Floor_0','Floor_1','Floor_2','Floor_3','Floor_4','Floor_5',
     'Floor_6','Floor_7','Floor_8','Floor_9','Floor_10','Floor_11',
     'Floor_12','Floor_13','Floor_14','Floor_15','Floor_16','Floor_17',
     'Floor_18','Floor_19','Floor_20','Floor_21','Floor_22','Floor_23',
     'Floor_24','Floor_25','Floor_26','Floor_27','Floor_28','Floor_29',
     'Floor_30','Floor_32','Floor_33','Floor_34','Floor_35','Floor_36',
     'Floor_37','Floor_39','Floor_40','Floor_41','Floor_43','Floor_44',
     'Floor_45','Floor_46','Floor_47','Floor_48','Floor_49','Floor_50',
     'Floor_53','Floor_60','Floor_65','Floor_76'
    ]
)

if st.button("Predict Rent"):
    # Prepare input
    input_df = pd.DataFrame({
        "BHK": [BHK],
        "Size": [Size],
        "Bathroom": [Bathroom],
        "Area Type": [Area_Type],
        "City": [City],
        "Furnishing Status": [Furnishing],
        "Tenant Preferred": [Tenant],
        "Floor_Label": [Floor]
    })

    # Encode categorical variables
    input_encoded = pd.get_dummies(input_df)

    # Align with model features
    for col in model.feature_names_in_:
        if col not in input_encoded.columns:
            input_encoded[col] = 0

    input_encoded = input_encoded[model.feature_names_in_]

    # Predict
    prediction = model.predict(input_encoded)

    st.success(f"Estimated Rent ({selected_model_name}): ₹ {prediction[0]:,.0f}")
