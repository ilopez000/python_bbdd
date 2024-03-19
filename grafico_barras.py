import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

try:
    # Establecer la conexión con la base de datos
    conexion = mysql.connector.connect(
        host='localhost',
        port=3306,
        user='root',
        password='changeme',
        database='dolibarr'
    )

    cursor = conexion.cursor()

    # Ejecutar la consulta SQL
    cursor.execute("SELECT concepto, SUM(cantidad) FROM transacciones_financieras GROUP BY concepto")

    # Obtener todos los resultados
    resultados = cursor.fetchall()

    conceptos = [fila[0] for fila in resultados]
    cantidades = [fila[1] for fila in resultados]

    # Crear gráfico de barras
    plt.figure(figsize=(12, 7))  # Tamaño del gráfico
    plt.bar(conceptos, cantidades, color='skyblue')  # Crear barras con los datos
    plt.title('Consulta a Transacciones Financieras')  # Título del gráfico
    plt.xlabel('Concepto')  # Etiqueta eje X
    plt.ylabel('Cantidades')  # Etiqueta eje Y
    plt.xticks(rotation=45)  # Rotar las etiquetas del eje X para mejor lectura
    plt.grid(axis='y')  # Mostrar cuadrícula solo en eje Y

    # Mostrar el gráfico
    plt.show()

except mysql.connector.Error as error:
    print(f"Se produjo un error: {error}")

finally:
    if (conexion.is_connected()):
        cursor.close()
        conexion.close()
        print("La conexión a la base de datos se ha cerrado")
