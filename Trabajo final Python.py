import pandas as pd

df = pd.read_csv(r"C:\Users\USER\OneDrive\Escritorio\Trabajo Final Python\notas_matematicas.csv")

# Calcular el promedio de cada alumno 
df["Promedio"] = df["Matematicas"]

# Alumno con mayor promedio
max_prom = df.loc[df["Promedio"].idxmax()]

# Alumno con menor promedio
min_prom = df.loc[df["Promedio"].idxmin()]

print("Alumno con el promedio más alto:")
print(f"{max_prom['Nombre']} {max_prom['Apellido_Paterno']} {max_prom['Apellido_Materno']} -> {max_prom['Promedio']}")

print("\nAlumno con el promedio más bajo:")
print(f"{min_prom['Nombre']} {min_prom['Apellido_Paterno']} {min_prom['Apellido_Materno']} -> {min_prom['Promedio']}")

