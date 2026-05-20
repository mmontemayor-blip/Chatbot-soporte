import streamlit as st

st.set_page_config(
    page_title="Inicio",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)


def main():
    st.header("Bienvenido al Chatbot de soporte",divider="green")

    col1,col2 =st.columns(2)

    with col1:

        st.write("**Bienvenido al chatbot de atención al cliente**")
        st.write("")
        st.text("""Este sistema utiliza una red neuronal para comprender tus mensajes y brindarte información sobre productos, precios y soporte.
        """, width="stretch")
        st.write("**Escribe tu consulta para comenzar.**")
        st.text(""" """)

    with col2:
        st.image("images/imagen1.jpg",width=500,output_format="JPEG",channels="RGB",use_container_width=True)
    


if __name__ == "__main__":
    main()
