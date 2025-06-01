import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Leer el CSV usando ruta completa
df = pd.read_csv(r"C:\Users\Estuardo\Desktop\2025\Inteligencia Artificial\Proyecto Final\datos_actividad_etiquetado.csv")

X = df[["ax", "ay", "az", "gx", "gy", "gz"]]
y = df["actividad"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
print(classification_report(y_test, y_pred))

# Guardar el modelo en la carpeta del proyecto
joblib.dump(modelo, r"C:\Users\Estuardo\Desktop\2025\Inteligencia Artificial\Proyecto Final\modelo_actividad.pkl")
print("Modelo guardado en la ruta especificada.")

