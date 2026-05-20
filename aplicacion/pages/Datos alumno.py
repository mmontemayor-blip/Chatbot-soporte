import streamlit as st
import psycopg2 


st.set_page_config(
    page_title="Datos alumno",
    page_icon="",
    layout="wide"
)
def main ():

    st.header("Datos del alumno")
    
    st.write("",)
    st.write("**Universidad Autónoma de Nuevo Leon.**")
    st.write("")
    st.text("""
    
    Facultad de ingeniería mecánica y eléctrica.
    SEMINARIO DE SISTEMAS II.
    Nombre: Miguel Angel Montemayor Coronado.
    Grupo: 002
    Docente: Ing. Tomas Eloy Salais Fierro.
    Hora: V4
    Semestre Enero-Junio""")

main()