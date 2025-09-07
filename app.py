import streamlit as st

st.title("LDTA Embraer 145 (GRF)")
st.write("Calculateur LDTA basé sur les tables GP-7924 (version simplifiée).")

# Entrées
poids = st.number_input("Poids atterrissage (kg)", 15000, 22000, 18000)
alt = st.number_input("Altitude pression (ft)", 0, 10000, 0)
vent = st.number_input("Vent (kt, +face / -arrière)", -50, 50, 0)

# Exemple de calcul simplifié (à remplacer par les tables complètes)
ldta = 1200 + (poids - 18000)/1000*50 + (alt/1000*30) - (vent*10)

st.subheader(f"LDTA calculée: {ldta:.0f} m")
