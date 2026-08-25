import streamlit as st
import requests

# ==========================================
# 1. PAGE & API CONFIGURATION
# ==========================================
st.set_page_config(page_title="Concrete Strength Predictor", page_icon="🤖", layout="wide")

# Set the FastAPI endpoint URL (local or deployed)
API_URL = "http://127.0.0.1:8000/predict"

st.title("Concrete Compressive Strength Predictor")
st.markdown("Enter the mixture components below to predict the 28-day equivalent compressive strength of the concrete.")
st.divider()

# ==========================================
# 2. INPUT FEATURES FORM
# ==========================================
# Wrapping inputs in a form prevents the app from rerunning on every single keypress
with st.form(key="prediction_form"):
    st.subheader("Input Features")
    
    col1, col2 = st.columns(2)
    with col1:
        cement = st.number_input("Cement (kg/m³)", min_value=0.0)
        slag = st.number_input("Blast Furnace Slag (kg/m³)", min_value=0.0)
        ash = st.number_input("Fly Ash (kg/m³)", min_value=0.0)
        water = st.number_input("Water (kg/m³)", min_value=0.0)
    with col2:
        superplastic = st.number_input("Superplasticizer (kg/m³)", min_value=0.0)
        coarseagg = st.number_input("Coarse Aggregate (kg/m³)", min_value=0.0)
        fineagg = st.number_input("Fine Aggregate (kg/m³)", min_value=0.0)
        age = st.number_input("Curing Age (Days)", min_value=1, max_value=365)
        
    # Submit button
    submitted = st.form_submit_button("Run Prediction")

# ==========================================
# 3. INFERENCE & API REQUEST
# ==========================================
if submitted:
    # A. Format payload to perfectly match the FastAPI Pydantic schema
    payload = {
            'cement': cement,
            'slag': slag,
            'ash': ash,
            'water': water,
            'superplastic': superplastic,
            'coarseagg': coarseagg,
            'fineagg': fineagg,
            'age': age
            }

    # B. Send POST request to FastAPI backend
    with st.spinner("Calculating..."):
        try:
            response = requests.post(API_URL, json=payload)
            response.raise_for_status() # Catches HTTP errors (e.g., 404, 500)
            
            # C. Extract and display the response
            result = response.json()    # will be in dictionary format
            predicted_strength = result['prediction']

            # Display
            st.success('Prediction Complete')
            st.metric(label="Predicted Strength", value=f"{predicted_strength:.2f} MPa")

# Output Schema of fastAPI
# class Response(BaseModel):
# prediction: float

        except requests.exceptions.ConnectionError:
            st.error("Error: Could not connect to the backend. Is FastAPI (uvicorn) running on port 8000?")
        except requests.exceptions.HTTPError as e:
            st.error(f"API Error: {e}")

# run
# streamlit run app.py