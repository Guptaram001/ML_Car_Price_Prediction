import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from joblib import load
import numpy as np
import json



st.set_page_config(page_title="Car Price Prediction", layout="centered")
st.image("static/image.png")
st.markdown("<h1 style='text-align: center; color: #0072C6;'>Car Price Prediction App</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

model = load("car_price_model.joblib")

categorical_columns = [
    'Kategorie', 'colour', 'make', 'model', 'Klimatisierung', 'Airbags',
    'Herkunft', 'Getriebe', 'Schadstoffklasse', 'primary_vehicle_type',
    'descriptor', 'primary_fuel', 'fuel_modifiers', 'Material', 'intColor'
]

numerical_columns = [
    'Kilometerstand', 'Leistung', 'CO2-Emissionen', 'Hubraum',
    'Anzahl Sitzplätze', 'Anzahl der Türen', 'age', 'availabilityDays',
    'combined', 'inner', 'outer'
]

numerical_ranges = {}
with open("numercial_values.json", 'r') as f:
    numerical_values = json.load(f)
    for k, v in numerical_values.items():
        numerical_ranges[k] = (v[0], v[1], 1)

with open("categorical_values.json", "r") as f:
    categories_values = json.load(f)

with open("feature_names.json") as f:
    expected_features = json.load(f)


if hasattr(model, "feature_importances_"):
    df_importance = pd.DataFrame({
        'Feature': expected_features,
        'Importance': model.feature_importances_
    })
    df_importance = df_importance.sort_values(by='Importance', ascending=False)
    df_importance.set_index('Feature', inplace=True)
    st.markdown("### Top 10 Important Features")
    st.bar_chart(df_importance.head(10))


st.markdown("###  Enter Car Details")
user_input = {}

with st.form("Car Info Form"):
    for col in categorical_columns:
        user_input[col] = st.selectbox(f"**{col}**", categories_values.get(col, ["Unknown"]))

    for col in numerical_columns:
        min_val, max_val, step = numerical_ranges.get(col, (0, 1000, 1))

        if isinstance(min_val, float) or isinstance(max_val, float):
            min_val, max_val, step = float(min_val), float(max_val), float(step)
            default_val = (min_val + max_val) / 2
        else:
            min_val, max_val, step = int(min_val), int(max_val), int(step)
            default_val = (min_val + max_val) // 2

        user_input[col] = st.slider(
            f"**{col}**",
            min_value=min_val-step,
            max_value=max_val+step,
            value=default_val,
            step=step
        )

    submitted = st.form_submit_button(" Predict Price")


if submitted:
    df = pd.DataFrame([user_input])
    df_encoded = pd.get_dummies(df, columns=categorical_columns, drop_first=True)

    for col in expected_features:
        if col not in df_encoded:
            df_encoded[col] = 0

    df_encoded = df_encoded[expected_features]

    prediction = model.predict(df_encoded)[0]

    st.success(f" Estimated Car Price: €{prediction:,.2f}")

    st.markdown("### 📈 Price Range Indicator")
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=prediction,
        title={'text': "Estimated Price (€)"},
        gauge={
            'axis': {'range': [0, 100000]},
            'bar': {'color': "darkblue"},
            'steps': [
                {'range': [0, 20000], 'color': 'lightgray'},
                {'range': [20000, 50000], 'color': 'gray'},
                {'range': [50000, 100000], 'color': 'lightblue'}
            ]
        }
    ))
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### 📋 Your Car Details")
    st.dataframe(df)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made using Streamlit | 2025</p>", unsafe_allow_html=True)

