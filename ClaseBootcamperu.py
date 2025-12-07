# app.py
import streamlit as st
import requests

# Reemplaza esto con la URL de tu Webhook de Make
WEBHOOK_URL = "https://hook.eu2.make.com/p6wvpkqvi1us6ml79qu24c6j4sv49t44"

st.title("🤖 Pregúntale a GPT vía Make Webhook")

# Input del usuario
pregunta = st.text_input("Haz una pregunta:", "")

if st.button("Enviar") and pregunta.strip() != "":
    with st.spinner("Esperando respuesta de Make..."):
        try:
            # Enviar la pregunta al webhook de Make
            payload = {"text": pregunta}
            response = requests.post(WEBHOOK_URL, json=payload, timeout=30)

            if response.status_code == 200:
                respuesta = response.text
                st.success("Respuesta de Make / GPT:")
                st.markdown(f"> {respuesta}")
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"Error en la conexión: {str(e)}")
