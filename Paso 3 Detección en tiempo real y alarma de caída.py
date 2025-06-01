import joblib
import serial
import pandas as pd
from datetime import datetime
import os
import time

# Cargar modelo
modelo = joblib.load(r"C:\Users\Estuardo\Desktop\2025\Inteligencia Artificial\Proyecto Final\modelo_actividad.pkl")
puerto = serial.Serial("COM3", 9600)

# Ruta del proyecto
ruta_proyecto = r"C:\Users\Estuardo\Desktop\2025\Inteligencia Artificial\Proyecto Final"
ruta_csv = os.path.join(ruta_proyecto, "registros_actividad.csv")

# Preguntar nombre del usuario al inicio
usuario = input("Ingrese el nombre del usuario: ").strip()

# Lista para guardar registros
registros = []

try:
    while True:
        linea = puerto.readline().decode().strip()
        partes = linea.split(",")
        if len(partes) == 6:
            datos = [int(x) for x in partes]
            pred = modelo.predict([datos])[0]
            ahora = datetime.now()

            print(f"{ahora} - Usuario: {usuario} - Actividad: {pred}")
            if pred == "caída":
                print("¡ALERTA DE CAÍDA!")

            registros.append({
                "timestamp": ahora,
                "usuario": usuario,
                "ax": datos[0],
                "ay": datos[1],
                "az": datos[2],
                "gx": datos[3],
                "gy": datos[4],
                "gz": datos[5],
                "actividad": pred
            })

            # Guardar CSV cada 10 registros
            if len(registros) >= 10:
                df = pd.DataFrame(registros)
                df.to_csv(ruta_csv, index=False, mode='a', header=not os.path.exists(ruta_csv))
                registros = []


            # Esperar 5 segundos antes de leer el siguiente dato
            time.sleep(1)

except KeyboardInterrupt:
    puerto.close()
    if registros:
        df = pd.DataFrame(registros)
        df.to_csv(ruta_csv, index=False, mode='a', header=not os.path.exists(ruta_csv))
    print(f"Programa finalizado. Datos guardados en: {ruta_csv}")
