import os
import pickle  
import streamlit as st  
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Prediction of Disease Outbreaks", layout="wide")


diabetes_model = pickle.load(open(r"diabetes_model.sav", 'rb'))
heart_disease_model = pickle.load(open(r"heart_model.sav", 'rb'))
parkinsons_disease_model = pickle.load(open(r"parkinsons_model.sav", 'rb'))

with st.sidebar:
    selected = option_menu(
        "Prediction of Disease Outbreak System",
        ["Diabetes Prediction", "Heart Disease Prediction", "Parkinsons Prediction"],
        menu_icon='hospital-fill',
        icons=['activity', 'heart', 'person'],
        default_index=0
    )


if selected == "Diabetes Prediction":
    st.title("Diabetes Prediction using ML")
    
   
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pregnancies = st.number_input("Number of Pregnancies (0-20)", min_value=0, max_value=20, value=0)
        glucose = st.number_input("Glucose Level (0-200 mg/dL)", min_value=0, max_value=200, value=0)
        blood_pressure = st.number_input("Blood Pressure (0-150 mm Hg)", min_value=0, max_value=150, value=0)
    
    with col2:
        skin_thickness = st.number_input("Skin Thickness (0-100 mm)", min_value=0, max_value=100, value=0)
        insulin = st.number_input("Insulin Level (0-1000 IU/mL)", min_value=0, max_value=1000, value=0)
        bmi = st.number_input("BMI (0.0-70.0)", min_value=0.0, max_value=70.0, value=0.0)
    
    with col3:
        diabetes_pedigree = st.number_input("Diabetes Pedigree Function (0.0-2.5)", min_value=0.0, max_value=2.5, value=0.0)
        age = st.number_input("Age (0-120 years)", min_value=0, max_value=120, value=0)
    
   
    if st.button("Predict Diabetes"):
        diabetes_prediction = diabetes_model.predict([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        if diabetes_prediction[0] == 1:
            st.success("The person has diabetes.")
        else:
            st.success("The person does not have diabetes.")


if selected == "Heart Disease Prediction":
    st.title("Heart Disease Prediction using ML")
    
   
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", min_value=0, max_value=120, value=0)
        sex = st.selectbox("Sex", ["Male", "Female"])
        cp = st.number_input("Chest Pain Type (0-3)", min_value=0, max_value=3, value=0)
        trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=200, value=0)
    
    with col2:
        chol = st.number_input("Serum Cholesterol (mg/dL)", min_value=0, max_value=600, value=0)
        fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", ["False", "True"])
        restecg = st.number_input("Resting Electrocardiographic Results (0-2)", min_value=0, max_value=2, value=0)
        thalach = st.number_input("Maximum Heart Rate Achieved", min_value=0, max_value=300, value=0)
    
    with col3:
        exang = st.selectbox("Exercise Induced Angina", ["No", "Yes"])
        oldpeak = st.number_input("ST Depression Induced by Exercise", min_value=0.0, max_value=10.0, value=0.0)
        slope = st.number_input("Slope of the Peak Exercise ST Segment (0-2)", min_value=0, max_value=2, value=0)
        ca = st.number_input("Number of Major Vessels (0-3)", min_value=0, max_value=3, value=0)
        thal = st.number_input("Thalassemia (0-3)", min_value=0, max_value=3, value=0)
    
  
    if st.button("Predict Heart Disease"):
        
        sex = 1 if sex == "Male" else 0
        fbs = 1 if fbs == "True" else 0
        exang = 1 if exang == "Yes" else 0
        
       
        heart_disease_prediction = heart_disease_model.predict([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        
      
        if heart_disease_prediction[0] == 1:
            st.success("The person has heart disease.")
        else:
            st.success("The person does not have heart disease.")
    


if selected == "Parkinsons Prediction":
    st.title("Parkinson's Disease Prediction using ML")
    
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        mdvp_fo = st.number_input("MDVP:Fo(Hz) - Average Vocal Frequency", min_value=0.0, max_value=300.0, value=0.0)
        mdvp_fhi = st.number_input("MDVP:Fhi(Hz) - Max Vocal Frequency", min_value=0.0, max_value=300.0, value=0.0)
        mdvp_flo = st.number_input("MDVP:Flo(Hz) - Min Vocal Frequency", min_value=0.0, max_value=300.0, value=0.0)
        mdvp_jitter_percent = st.number_input("MDVP:Jitter(%) - Jitter Percentage", min_value=0.0, max_value=1.0, value=0.0)
        mdvp_jitter_abs = st.number_input("MDVP:Jitter(Abs) - Absolute Jitter", min_value=0.0, max_value=0.01, value=0.0)
    
    with col2:
        mdvp_rap = st.number_input("MDVP:RAP - Relative Amplitude Perturbation", min_value=0.0, max_value=0.1, value=0.0)
        mdvp_ppq = st.number_input("MDVP:PPQ - Five-point Period Perturbation Quotient", min_value=0.0, max_value=0.1, value=0.0)
        jitter_ddp = st.number_input("Jitter:DDP - Jitter Differential", min_value=0.0, max_value=0.1, value=0.0)
        mdvp_shimmer = st.number_input("MDVP:Shimmer - Shimmer in dB", min_value=0.0, max_value=1.0, value=0.0)
        mdvp_shimmer_db = st.number_input("MDVP:Shimmer(dB) - Shimmer in Decibels", min_value=0.0, max_value=1.0, value=0.0)
    
    with col3:
        shimmer_apq3 = st.number_input("Shimmer:APQ3 - Shimmer Amplitude Perturbation Quotient 3", min_value=0.0, max_value=1.0, value=0.0)
        shimmer_apq5 = st.number_input("Shimmer:APQ5 - Shimmer Amplitude Perturbation Quotient 5", min_value=0.0, max_value=1.0, value=0.0)
        mdvp_apq = st.number_input("MDVP:APQ - Amplitude Perturbation Quotient", min_value=0.0, max_value=1.0, value=0.0)
        shimmer_dda = st.number_input("Shimmer:DDA - Shimmer Differential", min_value=0.0, max_value=1.0, value=0.0)
        nhr = st.number_input("NHR - Noise-to-Harmonics Ratio", min_value=0.0, max_value=1.0, value=0.0)
        hnr = st.number_input("HNR - Harmonics-to-Noise Ratio", min_value=0.0, max_value=50.0, value=0.0)
    
  
    st.subheader("Nonlinear Measures")
    col4, col5 = st.columns(2)
    
    with col4:
        rpde = st.number_input("RPDE - Recurrence Period Density Entropy", min_value=0.0, max_value=1.0, value=0.0)
        dfa = st.number_input("DFA - Detrended Fluctuation Analysis", min_value=0.0, max_value=1.0, value=0.0)
    
    with col5:
        spread1 = st.number_input("Spread1 - Signal Variability 1", min_value=-10.0, max_value=10.0, value=0.0)
        spread2 = st.number_input("Spread2 - Signal Variability 2", min_value=-10.0, max_value=10.0, value=0.0)
        d2 = st.number_input("D2 - Correlation Dimension", min_value=0.0, max_value=10.0, value=0.0)
        ppe = st.number_input("PPE - Pitch Period Entropy", min_value=0.0, max_value=1.0, value=0.0)
    
   
    if st.button("Predict Parkinson's"):
        
        input_features = [
            mdvp_fo, mdvp_fhi, mdvp_flo, mdvp_jitter_percent, mdvp_jitter_abs,
            mdvp_rap, mdvp_ppq, jitter_ddp, mdvp_shimmer, mdvp_shimmer_db,
            shimmer_apq3, shimmer_apq5, mdvp_apq, shimmer_dda, nhr, hnr,
            rpde, dfa, spread1, spread2, d2, ppe
        ]
        
        
        parkinsons_prediction = parkinsons_disease_model.predict([input_features])
        
       
        if parkinsons_prediction[0] == 1:
            st.success("The  person has Parkinson's disease.")
        else:
            st.success("The person does not have Parkinson's disease.")