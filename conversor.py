import streamlit as st

# Función para conversiones de temperatura
def temperatura_converter():
    st.header("Conversiones de Temperatura")
    opciones_temperatura = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]
    seleccion_temperatura = st.selectbox("Selecciona una conversión de temperatura", opciones_temperatura)
    
    if seleccion_temperatura == "Celsius a Fahrenheit":
        celsius = st.number_input("Ingresa la temperatura en Celsius", value=0.0)
        fahrenheit = (celsius * 9/5) + 32
        st.write(f"{celsius} °C equivale a {fahrenheit:.2f} °F")
    elif seleccion_temperatura == "Fahrenheit a Celsius":
        fahrenheit = st.number_input("Ingresa la temperatura en Fahrenheit", value=32.0)
        celsius = (fahrenheit - 32) * 5/9
        st.write(f"{fahrenheit} °F equivale a {celsius:.2f} °C")
    elif seleccion_temperatura == "Celsius a Kelvin":
        celsius = st.number_input("Ingresa la temperatura en Celsius", value=0.0)
        kelvin = celsius + 273.15
        st.write(f"{celsius} °C equivale a {kelvin:.2f} K")
    elif seleccion_temperatura == "Kelvin a Celsius":
        kelvin = st.number_input("Ingresa la temperatura en Kelvin", value=0.0)
        celsius = kelvin - 273.15
        st.write(f"{kelvin} K equivale a {celsius:.2f} °C")

# Función para conversiones de longitud
def longitud_converter():
    st.header("Conversiones de Longitud")
    opciones_longitud = ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"]
    seleccion_longitud = st.selectbox("Selecciona una conversión de longitud", opciones_longitud)
    
    if seleccion_longitud == "Pies a Metros":
        pies = st.number_input("Ingresa la longitud en Pies", value=0.0)
        metros = pies * 0.3048
        st.write(f"{pies} pies equivale a {metros:.2f} metros")
    elif seleccion_longitud == "Metros a Pies":
        metros = st.number_input("Ingresa la longitud en Metros", value=0.0)
        pies = metros / 0.3048
        st.write(f"{metros} metros equivale a {pies:.2f} pies")
    elif seleccion_longitud == "Pulgadas a Centímetros":
        pulgadas = st.number_input("Ingresa la longitud en Pulgadas", value=0.0)
        centimetros = pulgadas * 2.54
        st.write(f"{pulgadas} pulgadas equivale a {centimetros:.2f} centímetros")
    elif seleccion_longitud == "Centímetros a Pulgadas":
        centimetros = st.number_input("Ingresa la longitud en Centímetros", value=0.0)
        pulgadas = centimetros / 2.54
        st.write(f"{centimetros} centímetros equivale a {pulgadas:.2f} pulgadas")

# Inicialización de la app
st.title("Conversor Universal")
categorias = ["Temperatura", "Longitud"]  # Agrega el resto de las categorías aquí
seleccion_categoria = st.selectbox("Selecciona una categoría", categorias)

# Lógica para seleccionar la categoría y llamar a la función correspondiente
if seleccion_categoria == "Temperatura":
    temperatura_converter()
elif seleccion_categoria == "Longitud":
    longitud_converter()
# Agrega más bloques elif para el resto de las categorías
