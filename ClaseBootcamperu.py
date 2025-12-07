import streamlit as st
import requests

# URL de tu webhook Make (ya conectado a OpenAI)
WEBHOOK_URL = "https://hook.eu2.make.com/p6wvpkqvi1us6ml79qu24c6j4sv49t44"

st.set_page_config(page_title="Brilla Con Estilo", page_icon="💎", layout="wide")

# -------------------------
# Encabezado
# -------------------------
st.markdown("""
<h1 style='text-align: center; color: #D4AF37;'>💎 Brilla Con Estilo</h1>
<h4 style='text-align: center;'>Accesorios únicos para realzar tu belleza ✨</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------
# Catálogo visual (simulado con imágenes externas)
# -------------------------
col1, col2 = st.columns(2)
with col1:
    st.subheader("🌟 Cadenas")
    st.image("https://media.thejewellershop.com/images/products/1000/N5139-G-N5142-G_M2.jpg", caption="Cadena doble acero | $25.000")
    st.image("https://i.imgur.com/E6wU6HH.png", caption="Cadena estrella baño oro 18k | $32.000")
with col2:
    st.subheader("💫 Aretes")
    st.image("https://medusajoyas.com/8466-large_default/argollas-de-matrimonio-esperanza-dorada-con-bano-de-oro-amarillo-18k.jpg", caption="Argollas baño de oro | $18.000")
    st.image("https://i.imgur.com/DSqzgbN.png", caption="Corazones con circonias | $22.000")

col3, col4 = st.columns(2)
with col3:
    st.subheader("🌸 Pulseras")
    st.image("https://i.imgur.com/UyJcI7Z.png", caption="Perlas naturales | $28.000")
    st.image("https://i.imgur.com/vm8vMRB.png", caption="Pulsera cuero triple | $30.000")
with col4:
    st.subheader("🦋 Tobilleras")
    st.image("https://i.imgur.com/ocYiVt3.png", caption="Tobillera mariposa | $20.000")
    st.image("https://i.imgur.com/vJkij5X.png", caption="Tobillera doble con estrella | $27.000")

st.markdown("---")

# -------------------------
# Chat para preguntas
# -------------------------
st.subheader("💬 ¿Tienes preguntas? ¡Habla con nuestro asistente!")

with st.form("chat_form"):
    pregunta = st.text_input("Escribe tu pregunta sobre productos, combinaciones o envíos:", "")
    submitted = st.form_submit_button("Enviar al asistente 🤖")

    if submitted and pregunta.strip() != "":
        with st.spinner("Consultando al asistente vía Make..."):
            try:
                # Enviar pregunta al webhook de Make
                payload = {"text": pregunta}
                response = requests.post(WEBHOOK_URL, json=payload, timeout=30)

                if response.status_code == 200:
                    respuesta = response.text
                    st.success("Respuesta del asistente:")
                    st.markdown(f"🧠 **{respuesta}**")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Error en la conexión: {str(e)}")

# Footer
st.markdown("---")
st.caption("Creado con 💖 por Brilla Con Estilo - Powered by Streamlit + Make")
