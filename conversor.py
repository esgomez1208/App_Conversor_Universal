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

# Función para conversiones de peso/masa
def peso_masa_converter():
    st.header("Conversiones de Peso/Masa")
    opciones_peso_masa = ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"]
    seleccion_peso_masa = st.selectbox("Selecciona una conversión de peso/masa", opciones_peso_masa)
    
    if seleccion_peso_masa == "Libras a Kilogramos":
        libras = st.number_input("Ingresa el peso en Libras", value=0.0)
        kilogramos = libras * 0.453592
        st.write(f"{libras} libras equivale a {kilogramos:.2f} kilogramos")
    elif seleccion_peso_masa == "Kilogramos a Libras":
        kilogramos = st.number_input("Ingresa el peso en Kilogramos", value=0.0)
        libras = kilogramos / 0.453592
        st.write(f"{kilogramos} kilogramos equivale a {libras:.2f} libras")
    elif seleccion_peso_masa == "Onzas a Gramos":
        onzas = st.number_input("Ingresa el peso en Onzas", value=0.0)
        gramos = onzas * 28.3495
        st.write(f"{onzas} onzas equivale a {gramos:.2f} gramos")
    elif seleccion_peso_masa == "Gramos a Onzas":
        gramos = st.number_input("Ingresa el peso en Gramos", value=0.0)
        onzas = gramos / 28.3495
        st.write(f"{gramos} gramos equivale a {onzas:.2f} onzas")

# Función para conversiones de volumen
def volumen_converter():
    st.header("Conversiones de Volumen")
    opciones_volumen = ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"]
    seleccion_volumen = st.selectbox("Selecciona una conversión de volumen", opciones_volumen)
    
    if seleccion_volumen == "Galones a Litros":
        galones = st.number_input("Ingresa el volumen en Galones", value=0.0)
        litros = galones * 3.78541
        st.write(f"{galones} galones equivale a {litros:.2f} litros")
    elif seleccion_volumen == "Litros a Galones":
        litros = st.number_input("Ingresa el volumen en Litros", value=0.0)
        galones = litros / 3.78541
        st.write(f"{litros} litros equivale a {galones:.2f} galones")
    elif seleccion_volumen == "Pulgadas cúbicas a Centímetros cúbicos":
        pulgadas_cubicas = st.number_input("Ingresa el volumen en Pulgadas cúbicas", value=0.0)
        cm_cubicos = pulgadas_cubicas * 16.3871
        st.write(f"{pulgadas_cubicas} pulgadas cúbicas equivale a {cm_cubicos:.2f} centímetros cúbicos")
    elif seleccion_volumen == "Centímetros cúbicos a Pulgadas cúbicas":
        cm_cubicos = st.number_input("Ingresa el volumen en Centímetros cúbicos", value=0.0)
        pulgadas_cubicas = cm_cubicos / 16.3871
        st.write(f"{cm_cubicos} centímetros cúbicos equivale a {pulgadas_cubicas:.2f} pulgadas cúbicas")

# Función para conversiones de tiempo
def tiempo_converter():
    st.header("Conversiones de Tiempo")
    opciones_tiempo = ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"]
    seleccion_tiempo = st.selectbox("Selecciona una conversión de tiempo", opciones_tiempo)
    
    if seleccion_tiempo == "Horas a Minutos":
        horas = st.number_input("Ingresa el tiempo en Horas", value=0.0)
        minutos = horas * 60
        st.write(f"{horas} horas equivale a {minutos:.2f} minutos")
    elif seleccion_tiempo == "Minutos a Segundos":
        minutos = st.number_input("Ingresa el tiempo en Minutos", value=0.0)
        segundos = minutos * 60
        st.write(f"{minutos} minutos equivale a {segundos:.2f} segundos")
    elif seleccion_tiempo == "Días a Horas":
        dias = st.number_input("Ingresa el tiempo en Días", value=0.0)
        horas = dias * 24
        st.write(f"{dias} días equivale a {horas:.2f} horas")
    elif seleccion_tiempo == "Semanas a Días":
        semanas = st.number_input("Ingresa el tiempo en Semanas", value=0.0)
        dias = semanas * 7
        st.write(f"{semanas} semanas equivale a {dias:.2f} días")

# Función para conversiones de velocidad
def velocidad_converter():
    st.header("Conversiones de Velocidad")
    opciones_velocidad = ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"]
    seleccion_velocidad = st.selectbox("Selecciona una conversión de velocidad", opciones_velocidad)
    
    if seleccion_velocidad == "Millas por hora a Kilómetros por hora":
        mph = st.number_input("Ingresa la velocidad en Millas por hora", value=0.0)
        kph = mph * 1.60934
        st.write(f"{mph} millas por hora equivale a {kph:.2f} kilómetros por hora")
    elif seleccion_velocidad == "Kilómetros por hora a Metros por segundo":
        kph = st.number_input("Ingresa la velocidad en Kilómetros por hora", value=0.0)
        mps = kph * 0.277778
        st.write(f"{kph} kilómetros por hora equivale a {mps:.2f} metros por segundo")
    elif seleccion_velocidad == "Nudos a Millas por hora":
        nudos = st.number_input("Ingresa la velocidad en Nudos", value=0.0)
        mph = nudos * 1.15078
        st.write(f"{nudos} nudos equivale a {mph:.2f} millas por hora")
    elif seleccion_velocidad == "Metros por segundo a Pies por segundo":
        mps = st.number_input("Ingresa la velocidad en Metros por segundo", value=0.0)
        fps = mps * 3.28084
        st.write(f"{mps} metros por segundo equivale a {fps:.2f} pies por segundo")

# Función para conversiones de área
def area_converter():
    st.header("Conversiones de Área")
    opciones_area = ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"]
    seleccion_area = st.selectbox("Selecciona una conversión de área", opciones_area)
    
    if seleccion_area == "Metros cuadrados a Pies cuadrados":
        metros_cuadrados = st.number_input("Ingresa el área en Metros cuadrados", value=0.0)
        pies_cuadrados = metros_cuadrados * 10.7639
        st.write(f"{metros_cuadrados} metros cuadrados equivale a {pies_cuadrados:.2f} pies cuadrados")
    elif seleccion_area == "Pies cuadrados a Metros cuadrados":
        pies_cuadrados = st.number_input("Ingresa el área en Pies cuadrados", value=0.0)
        metros_cuadrados = pies_cuadrados / 10.7639
        st.write(f"{pies_cuadrados} pies cuadrados equivale a {metros_cuadrados:.2f} metros cuadrados")
    elif seleccion_area == "Kilómetros cuadrados a Millas cuadradas":
        km_cuadrados = st.number_input("Ingresa el área en Kilómetros cuadrados", value=0.0)
        millas_cuadradas = km_cuadrados * 0.386102
        st.write(f"{km_cuadrados} kilómetros cuadrados equivale a {millas_cuadradas:.2f} millas cuadradas")
    elif seleccion_area == "Millas cuadradas a Kilómetros cuadrados":
        millas_cuadradas = st.number_input("Ingresa el área en Millas cuadradas", value=0.0)
        km_cuadrados = millas_cuadradas / 0.386102
        st.write(f"{millas_cuadradas} millas cuadradas equivale a {km_cuadrados:.2f} kilómetros cuadrados")

def energia_converter():
    st.header("Conversiones de Energía")
    opciones_energia = ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"]
    seleccion_energia = st.selectbox("Selecciona una conversión de energía", opciones_energia)
    
    if seleccion_energia == "Julios a Calorías":
        julios = st.number_input("Ingresa la energía en Julios", value=0.0)
        calorias = julios * 0.239006
        st.write(f"{julios} Julios equivale a {calorias:.2f} Calorías")
    elif seleccion_energia == "Calorías a Kilojulios":
        calorias = st.number_input("Ingresa la energía en Calorías", value=0.0)
        kilojulios = calorias * 0.004184
        st.write(f"{calorias} Calorías equivale a {kilojulios:.4f} Kilojulios")
    elif seleccion_energia == "Kilovatios-hora a Megajulios":
        kw_hora = st.number_input("Ingresa la energía en Kilovatios-hora", value=0.0)
        mjulios = kw_hora * 3.6
        st.write(f"{kw_hora} Kilovatios-hora equivale a {mjulios:.2f} Megajulios")
    elif seleccion_energia == "Megajulios a Kilovatios-hora":
        mjulios = st.number_input("Ingresa la energía en Megajulios", value=0.0)
        kw_hora = mjulios / 3.6
        st.write(f"{mjulios} Megajulios equivale a {kw_hora:.2f} Kilovatios-hora")

# Función para conversiones de presión
def presion_converter():
    st.header("Conversiones de Presión")
    opciones_presion = ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Bares"]
    seleccion_presion = st.selectbox("Selecciona una conversión de presión", opciones_presion)
    
    if seleccion_presion == "Pascales a Atmósferas":
        pascales = st.number_input("Ingresa la presión en Pascales", value=0.0)
        atmosferas = pascales / 101325
        st.write(f"{pascales} Pascales equivale a {atmosferas:.8f} Atmósferas")
    elif seleccion_presion == "Atmósferas a Pascales":
        atmosferas = st.number_input("Ingresa la presión en Atmósferas", value=0.0)
        pascales = atmosferas * 101325
        st.write(f"{atmosferas} Atmósferas equivale a {pascales:.2f} Pascales")
    elif seleccion_presion == "Barras a Libras por pulgada cuadrada":
        barras = st.number_input("Ingresa la presión en Barras", value=0.0)
        psi = barras * 14.5038
        st.write(f"{barras} Barras equivale a {psi:.2f} Libras por pulgada cuadrada")
    elif seleccion_presion == "Libras por pulgada cuadrada a Bares":
        psi = st.number_input("Ingresa la presión en Libras por pulgada cuadrada", value=0.0)
        barras = psi / 14.5038
        st.write(f"{psi} Libras por pulgada cuadrada equivale a {barras:.4f} Barras")

# Función para conversiones de tamaño de datos
def tamano_datos_converter():
    st.header("Conversiones de Tamaño de Datos")
    opciones_tamano_datos = ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
    seleccion_tamano_datos = st.selectbox("Selecciona una conversión de tamaño de datos", opciones_tamano_datos)
    
    if seleccion_tamano_datos == "Megabytes a Gigabytes":
        mb = st.number_input("Ingresa el tamaño en Megabytes", value=0.0)
        gb = mb / 1024
        st.write(f"{mb} Megabytes equivale a {gb:.6f} Gigabytes")
    elif seleccion_tamano_datos == "Gigabytes a Terabytes":
        gb = st.number_input("Ingresa el tamaño en Gigabytes", value=0.0)
        tb = gb / 1024
        st.write(f"{gb} Gigabytes equivale a {tb:.6f} Terabytes")
    elif seleccion_tamano_datos == "Kilobytes a Megabytes":
        kb = st.number_input("Ingresa el tamaño en Kilobytes", value=0.0)
        mb = kb / 1024
        st.write(f"{kb} Kilobytes equivale a {mb:.6f} Megabytes")
    elif seleccion_tamano_datos == "Terabytes a Petabytes":
        tb = st.number_input("Ingresa el tamaño en Terabytes", value=0.0)
        pb = tb / 1024
        st.write(f"{tb} Terabytes equivale a {pb:.6f} Petabytes")


# Inicialización de la app
st.title("Conversor Universal")
categorias = ["Temperatura", "Longitud", "Peso/Masa", "Volumen", "Tiempo", "Velocidad", "Área", "Energía", "Presión", "Tamaño de Datos"]
seleccion_categoria = st.selectbox("Selecciona una categoría", categorias)

# Lógica para seleccionar la categoría y llamar a la función correspondiente
if seleccion_categoria == "Temperatura":
    temperatura_converter()
elif seleccion_categoria == "Longitud":
    longitud_converter()
elif seleccion_categoria == "Peso/Masa":
    peso_masa_converter()
elif seleccion_categoria == "Volumen":
    volumen_converter()
elif seleccion_categoria == "Tiempo":
    tiempo_converter()
elif seleccion_categoria == "Velocidad":
    velocidad_converter()
elif seleccion_categoria == "Área":
    area_converter()
elif seleccion_categoria == "Energía":
    energia_converter()
elif seleccion_categoria == "Presión":
    presion_converter()
elif seleccion_categoria == "Tamaño de Datos":
    tamano_datos_converter()
