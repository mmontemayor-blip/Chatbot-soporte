import streamlit as st
import json
import pandas as pd

# --- CARGAR JSON ---
try:
    with open("aplicacion/catalogo.json", "r", encoding="utf-8") as f:
        catalogo_lista = json.load(f)
except:
    st.error("No se encontró catalogo.json ❌")
    st.stop()

df_catalogo = pd.DataFrame(catalogo_lista)

# convertir a diccionario
catalogo = {item["nombre"]: item for item in catalogo_lista}



# --- RESPUESTAS BÁSICAS ---
qa_pairs = {
    "hola": "¡Hola! 👋 Bienvenido a nuestro sistema de atención al cliente. Estoy aquí para ayudarte con productos, precios y soporte técnico.",
    "como te llamas": "Soy un asistente virtual diseñado para brindar soporte automatizado 🤖.",
    "quien te creo": "Proyecto desarrollado por un estudiante de Ingeniería en Sistemas.",
    "adios": "Gracias por usar el sistema 😊",
    "bye": "Hasta luego 👋",
    "que puedes hacer": "Puedo ayudarte con catálogo, precios, soporte y evaluación."
}

# --- SOPORTE ---
soporte = {


        "laptop no enciende": """🔧 SOPORTE TÉCNICO: LAPTOP NO ENCIENDE

        1.- 🔌 Verifica cargador, enchufe y mantén presionado el botón de encendido 10 segundos.

        🔋 2.- Revisa la batería.

        💡 3.- Verifica luces o señales de encendido.

        🔄 4.- Realiza un reinicio de energía (Power Reset).

        👨‍🔧 Si después de estos pasos la laptop no responde, se recomienda acudir con soporte técnico especializado para una revisión más profunda.
        """,

            "laptop lenta": """🔧 SOPORTE TÉCNICO: LAPTOP LENTA

        ⚡ 1.- Reinicia el equipo.

        📂 2.- Cierra programas que no estés utilizando.

        💾 3.- Revisa el espacio de almacenamiento.

        🧹 4.- Limpia archivos temporales.

        🛡️ 5.- Analiza posibles virus o malware.

        🚀 6.- Desactiva programas de inicio innecesarios.

        🔄 7.- Verifica actualizaciones del sistema.

        👨‍🔧 Si después de realizar estos pasos el problema continúa, se recomienda acudir con soporte técnico para una revisión más profunda del hardware.
        """,

            "wifi laptop": """🔧 SOPORTE TÉCNICO: WIFI EN LAPTOP

        📶 1.- Verifica que el Wi-Fi esté activado.

        🔄 2.- Reinicia el módem y la laptop.

        🔑 3.- Reconecta la red Wi-Fi.

        🌐 4.- Verifica internet en otros dispositivos.

        💻 5.- Revisa controladores de red.

        👨‍🔧 Si el problema continúa, se recomienda acudir a soporte técnico especializado.
        """,

            "impresora no imprime": """🔧 SOPORTE TÉCNICO: IMPRESORA NO IMPRIME

        🖨️ 1.- Revisa la conexión USB o Wi-Fi.

        🖋️ 2.- Verifica niveles de tinta.

        📄 3.- Revisa si hay papel atascado.

        🔄 4.- Reinicia la impresora.

        👨‍🔧 Si el problema continúa, acude a soporte técnico.
        """,

            "servidor caido": """🔧 SOPORTE TÉCNICO: SERVIDOR CAÍDO

        ⚡ 1.- Verifica la energía eléctrica.

        🌐 2.- Revisa la conexión de red.

        🔄 3.- Reinicia el servidor.

        🖥️ 4.- Verifica estado de CPU y RAM.

        👨‍🔧 Si el problema persiste, contacta al administrador del sistema.
    """,
           "pantalla azul": """🔧 SOPORTE TÉCNICO: PANTALLA AZUL (BSOD)

💻 1.- Reinicia la laptop o PC.

⚠️ 2.- Si el error aparece constantemente:
- Revisa si instalaste programas nuevos.
- Desinstala software reciente.

🛡️ 3.- Ejecuta un análisis antivirus.

🔄 4.- Actualiza drivers:
- Windows Update
- Drivers de video
- Drivers de red

💾 5.- Verifica memoria RAM:
- Presiona Windows + R
- Escribe: mdsched.exe

🖥️ 6.- Revisa espacio del disco duro.

👨‍🔧 Si el problema persiste, puede tratarse de una falla de hardware o sistema operativo.
""",

"laptop se calienta": """🔧 SOPORTE TÉCNICO: LAPTOP SE CALIENTA

🌡️ 1.- Verifica ventilación.
- No tapes salidas de aire.
- Usa superficie plana.

🧹 2.- Limpia ventiladores.
El polvo puede bloquear la ventilación.

❌ 3.- Cierra programas pesados.

🔄 4.- Reinicia el equipo.

⚙️ 5.- Revisa uso de CPU:
- Ctrl + Shift + Esc
- Administrador de tareas

🧊 6.- Usa base de enfriamiento.

👨‍🔧 Si se apaga sola constantemente, acude a soporte técnico.
""",

"teclado no funciona": """🔧 SOPORTE TÉCNICO: TECLADO NO FUNCIONA

⌨️ 1.- Reinicia la computadora.

🔌 2.- Si es teclado USB:
- Desconecta y vuelve a conectar.

🔋 3.- Si es inalámbrico:
- Revisa baterías.

💻 4.- Verifica drivers:
- Administrador de dispositivos
- Teclado

🧹 5.- Limpia teclas atoradas.

👨‍🔧 Si algunas teclas siguen sin funcionar, puede requerir reemplazo.
""",

"mouse no funciona": """🔧 SOPORTE TÉCNICO: MOUSE NO FUNCIONA

🖱️ 1.- Desconecta y conecta nuevamente.

🔋 2.- Revisa batería (si es inalámbrico).

💻 3.- Prueba otro puerto USB.

🧹 4.- Limpia sensor inferior.

🔄 5.- Reinicia computadora.

⚙️ 6.- Revisa controladores USB.

👨‍🔧 Si sigue sin responder, podría estar dañado.
""",

"impresora atascada": """🔧 SOPORTE TÉCNICO: PAPEL ATASCADO EN IMPRESORA

🖨️ 1.- Apaga la impresora.

📄 2.- Retira cuidadosamente el papel.

⚠️ 3.- No jales fuerte para evitar daños.

🧹 4.- Limpia rodillos internos.

🔄 5.- Reinicia impresora.

📌 6.- Usa hojas en buen estado.

👨‍🔧 Si continúa el problema, revisa sensores internos.
""",

"internet lento": """🔧 SOPORTE TÉCNICO: INTERNET LENTO

📶 1.- Reinicia módem.

📍 2.- Acércate al router.

📱 3.- Desconecta equipos innecesarios.

🌐 4.- Ejecuta prueba de velocidad.

🔄 5.- Reinicia laptop o PC.

🛡️ 6.- Verifica virus o malware.

💻 7.- Actualiza drivers de red.

👨‍🔧 Si sigue lento, contacta a tu proveedor de internet.
""",

"pc no enciende": """🔧 SOPORTE TÉCNICO: PC NO ENCIENDE

🔌 1.- Revisa cable de corriente.

⚡ 2.- Verifica enchufe eléctrico.

💡 3.- Revisa si hay luces LED.

🖥️ 4.- Escucha ventiladores.

🔄 5.- Mantén presionado botón de encendido 10 segundos.

🧹 6.- Verifica memoria RAM.

👨‍🔧 Si no responde, puede ser fuente de poder dañada.
""",

"servidor lento": """🔧 SOPORTE TÉCNICO: SERVIDOR LENTO

📊 1.- Revisa uso de CPU y RAM.

💾 2.- Verifica espacio disponible.

🌐 3.- Revisa tráfico de red.

🔄 4.- Reinicia servicios.

🛡️ 5.- Verifica malware.

📁 6.- Elimina procesos innecesarios.

👨‍🔧 Si continúa lento, revisar configuración del servidor.
""",

"wifi desconectado": """🔧 SOPORTE TÉCNICO: WIFI DESCONECTADO

📶 1.- Verifica que Wi-Fi esté activado.

🔄 2.- Reinicia módem.

💻 3.- Reinicia laptop.

🔑 4.- Reconecta red Wi-Fi.

⚙️ 5.- Actualiza drivers de red.

🌐 6.- Verifica conexión en otros dispositivos.

👨‍🔧 Si continúa, podría fallar la tarjeta de red.
""",

"pantalla negra": """🔧 SOPORTE TÉCNICO: PANTALLA NEGRA

💻 1.- Verifica brillo de pantalla.

🔄 2.- Reinicia equipo.

🔌 3.- Conecta monitor externo.

⚡ 4.- Mantén presionado encendido 15 segundos.

💾 5.- Revisa memoria RAM.

👨‍🔧 Si sigue igual, puede ser falla de pantalla o tarjeta gráfica.
""",

}

# --- CONFIG ---
st.set_page_config(page_title="Chatbot Técnico", page_icon="🤖")
st.title("🤖 Chatbot de Atención al Cliente")
st.caption("Consulta productos, soporte o escribe 'opinar sistema'")

# --- ESTADOS ---
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hola En que puedo ayudarte"}]
if "doing_test" not in st.session_state:
    st.session_state.doing_test = False

# --- MOSTRAR HISTORIAL ---
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).markdown(msg["content"])

# --- ENCUESTA ---
if st.session_state.doing_test:
    with st.form("Encuesta"):
        st.subheader("📊 Encuesta de satisfacción")

        calificacion = st.radio("¿Qué tan útil fue?", [1,2,3,4,5])
        comentario = st.text_area("Comentario")

        submitted = st.form_submit_button("Enviar")

    if submitted:
        resultado = f"Gracias 😊\nCalificación: {calificacion}\nComentario: {comentario}"
        st.chat_message("assistant").markdown(resultado)
        st.session_state.messages.append({"role": "assistant", "content": resultado})

        st.session_state.doing_test = False
        st.rerun()

# --- CHAT ---
else:
    categorias = {}
    def llamar_catalogo():
        
        for nombre, info in catalogo.items():
            cat = info["categoria"]
            if cat not in categorias:
                categorias[cat] = []
            categorias[cat].append(nombre)

        response = "📦 CATÁLOGO:\n\n"

        for cat, items in categorias.items():
            response += f"🔹 {cat.upper()}:\n"
            for item in items:
                response += f"   - {item}\n"
            response += "\n"

        response += "Escribe el nombre del producto para ver detalles."
        st.session_state.messages.append({"role": "assistant", "content": response})

    co1,co2,co3 = st.columns(3)
    co1.button("Productos" ,on_click= llamar_catalogo,width="stretch")

    def llamar_soporte():
        st.session_state.messages.append({"role": "assistant", "content":"Describe tu problema:" })
        for idx, item in enumerate(soporte):
            st.button(item,key=f"Soporte_{idx}",on_click = lambda item = item : st.session_state.messages.append({"role": "user", "content":f"soporte {item}" }))

        
        
    if co2.button("Soporte",width="stretch"):
        st.session_state.messages.append({"role": "assistant", "content":"Describe tu problema:" })
        for idx, item in enumerate(soporte):
            st.button(f"{idx+1} - {item}",key=f"Soporte_{idx}",on_click= lambda item = item : st.session_state.update({"user_input_chat":f"soporte {item}"}),type=("tertiary"))
                
        
        
    co3.button("Opinión del sistema",width="stretch",on_click= lambda: st.session_state.update({"user_input_chat":"opinar"}))
    
    user_input = st.chat_input("Escribe aquí...",key="user_input_chat")

    if user_input:
        st.chat_message("user").markdown(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})

        user_text = user_input.lower()
        response = None

        # 📊 ENCUESTA
        if "opinar" in user_text:
            st.session_state.doing_test = True
            st.rerun()

        # 📦 MOSTRAR CATALOGO
        elif "catalogo" in user_text:
            categorias = {}

            for nombre, info in catalogo.items():
                cat = info["categoria"]
                if cat not in categorias:
                    categorias[cat] = []
                categorias[cat].append(nombre)

            response = "📦 CATÁLOGO:\n\n"

            for cat, items in categorias.items():
                response += f"🔹 {cat.upper()}:\n"
                for item in items:
                    response += f"   - {item}\n"
                response += "\n"

            response += "Escribe el nombre del producto para ver detalles."

        # 🔍 BUSCAR PRODUCTO
        elif any(p in user_text for p in catalogo):
            for p in catalogo:
                if p in user_text:
                    producto = catalogo[p]
                    response = f"""💻 {p.upper()}

{producto['info']}

Incluye soporte técnico básico."""
                    break

 # 🛠️ SOPORTE
        elif "soporte" in user_text:
            for problema in soporte:
                if problema in user_text:
                    response = soporte[problema]
                    break
            if response is None:
                response = "Describe tu problema (ej: soporte laptop lenta)"

        # AYUDA
        elif "ayuda" in user_text:
            response = """🤖 OPCIONES:

📦 catalogo → ver productos  
💻 nombre producto → ver info  
🛠️ soporte problema  
📊 opinar sistema"""

        # RESPUESTAS BÁSICAS
        else:
            for key, value in qa_pairs.items():
                if key in user_text:
                    response = value
                    break

            if response is None:
                response = "No entendí 😅 escribe 'catalogo'"

        st.chat_message("assistant").markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
