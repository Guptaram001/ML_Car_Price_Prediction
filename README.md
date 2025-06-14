# 🚗 Car Price Prediction App

An interactive **Machine Learning web application** built using **Streamlit** to estimate the price of a used car based on its specifications. This app takes various inputs like car brand, model, mileage, engine size, etc., and predicts the estimated price using a trained machine learning model.

---

## 📌 Features

- 🎯 Predict car prices based on both categorical and numerical features
- 📊 Visualize top 10 most important features using bar chart
- 📈 Interactive gauge chart showing predicted price range
- 📋 Input form with dynamic dropdowns and sliders
- 🌐 User-friendly and responsive interface

---

## 🧠 Technologies Used

- **Python 3**
- **Streamlit** – UI and web app framework
- **Plotly** – Interactive visualizations (gauge charts)
- **Pandas, NumPy** – Data processing and manipulation
- **Scikit-learn, Joblib** – Machine learning model loading
- **Matplotlib** – (optional) for additional charts if needed

---

## 📁 Project Structure

├── main.py # Streamlit app source code  
├── requirements.txt # Python dependencies  
├── static/  
├── image.png # Header image for the app  
├── numercial_values.json # Range values for sliders  
├── categorical_values.json # Dropdown options for categories  
└── feature_names.json # Ordered list of model input features  


### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/car-price-prediction-app.git
cd car-price-prediction-app
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the App

```bash
streamlit run main.py
```

Then open http://localhost:8501 in your browser.


