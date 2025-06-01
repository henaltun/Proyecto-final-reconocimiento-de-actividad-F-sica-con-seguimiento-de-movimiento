import serial
import pandas as pd
import os

puerto = serial.Serial('COM3', 9600) 
datos = []

print("Leyendo datos... Presiona Ctrl+C para detener")

try:
    while True:
        linea = puerto.readline().decode().strip()
        partes = linea.split(",")
        if len(partes) == 6:
            datos.append([int(x) for x in partes])
except KeyboardInterrupt:
    df = pd.DataFrame(datos, columns=["ax", "ay", "az", "gx", "gy", "gz"])
    
    ruta = r"C:\Users\Estuardo\Desktop\2025\Inteligencia Artificial\Proyecto Final"
    archivo = os.path.join(ruta, "datos_actividad.csv")
    
    df.to_csv(archivo, index=False)
    print(f"Datos guardados en '{archivo}'")
