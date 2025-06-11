import streamlit as st

st.title("🧮 Calculadora Básica")

num1 = st.number_input("Ingresa el primer número", step=1.0)
num2 = st.number_input("Ingresa el segundo número", step=1.0)
operacion = st.selectbox("Selecciona una operación", ["Suma", "Resta", "Multiplicación", "División"])

resultado = None
if operacion == "Suma":
    resultado = num1 + num2
elif operacion == "Resta":
    resultado = num1 - num2
elif operacion == "Multiplicación":
    resultado = num1 * num2
elif operacion == "División":
    if num2 != 0:
        resultado = num1 / num2
    else:
        st.error("❌ No se puede dividir entre cero")

if resultado is not None:
    st.success(f"Resultado: {resultado}")
