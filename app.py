import pickle
import numpy as np
import streamlit as st

#load save model
model = pickle.load(open('employee.sav','rb'))

#judul web
st.title('Prediksi Kinerja Karyawan')

col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    Kehadiran = st.text_input('Kehadiran')
with col2:
    Kedisiplinan = st.text_input('Kedisiplinan')
with col3:
    Tanggung_Jawab = st.text_input('Tanggung Jawab')
with col4:
    Attitude = st.text_input('Attitude')
with col5:
    Komunikasi = st.text_input('Komunikasi')

#code for prediction
prediksi = ''

#buat tombol prediksi
if st.button('Prediksi Kinerja Karyawan'):
    employee_prediction = model.predict([[Kehadiran, Kedisiplinan, Tanggung_Jawab, Attitude, Komunikasi]])

    if(employee_prediction[0==1]):
        prediksi = 'Lolos'
    else:
        prediksi = 'Tidak Lolos'

st.success(prediksi)