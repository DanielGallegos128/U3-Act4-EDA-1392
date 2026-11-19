
import pandas as pd
import matplotlib.pyplot as plt
# Daniel Gallegos NC 1392
# 1. Crear diccionario con datos de libros
libros_biblioteca = {
    'isbn': ['978-1', '978-2', '978-3', '978-4', '978-5', '978-6'],
    'titulo': ['Cien años de soledad', 'El principito', '1984', 'Don Quijote', 'Fahrenheit 451', 'Orgullo y prejuicio'],
    'autor': ['Garcia Marquez', 'Saint-Exupery', 'Orwell', 'Cervantes', 'Bradbury', 'Austen'],
    'ano_publicacion': [1967, 1943, 1949, 1605, 1953, 1813],
    'genero': ['Realismo magico', 'Infantil', 'Distopia', 'Aventuras', 'Ciencia ficcion', 'Romance'],
    'ejemplares_totales': [5, 8, 4, 3, 4, 6],
    'ejemplares_prestados': [2, 5, 1, 0, 2, 3],
    'ubicacion_estante': ['A1', 'B2', 'C1', 'A2', 'C2', 'B3'],
    'estado_conservacion': ['Bueno', 'Regular', 'Excelente', 'Regular', 'Bueno', 'Excelente'],
    'fecha_ultimo_prestamo': ['2024-01-10', '2024-01-12', '2023-12-20', '2023-11-05', '2024-01-08', '2024-01-11']
}
print("Análisis Exploratorio de Datos")
print("Exploratory Data Analysis por Daniel Gallegos NC 1392")
print("1. Crear diccionario con 10 listas y 6 elementos")
# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(libros_biblioteca)
print("\n--- TABLA ORIGINAL DE LIBROS ---")
print(df)
# 3. Exportar los datos a CSV
print("\n+-+-+- Convertir DataFrame en archivo CSV -+-+-+")
df.to_csv(
    'libros_biblioteca_1392.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\nArchivo CSV creado correctamente")
# 4. Leer archivo CSV
print("\n--- Leer archivo CSV ---")
print("libros_biblioteca_1392.csv")
df = pd.read_csv('libros_biblioteca_1392.csv')
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)
# 5. Primeros y últimos registros
print("\n1. PRIMEROS REGISTROS (Head):")
print(df.head(3))
print("\n2. ÚLTIMOS REGISTROS (Tail):")
print(df.tail(2))
# 6. Dimensiones y estructura
print("\n--- 6. DIMENSIONES Y ESTRUCTURA ---")
print(df)
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()
# 7. Estadísticas y limpieza
print("\n--- 7. ESTADÍSTICAS Y LIMPIEZA ---")
print("\n7. ESTADÍSTICAS DESCRIPTIVAS:")
print(df.describe())
print("\n8. VALORES FALTANTES (Nulls):")
print(df.isnull().sum())
print("\n9. REGISTROS DUPLICADOS:")
print(df.duplicated().sum())
print("\n10. VALORES ÚNICOS POR COLUMNA:")
print(df.nunique())
print("Géneros únicos:", df['genero'].unique())
# 8. Análisis específico
print("\n--- 8. ANÁLISIS ESPECÍFICO ---")
print(df)
print("\n11. LIBROS POR GÉNERO:")
print(df['genero'].value_counts())
print("\n12. PROMEDIO DE EJEMPLARES TOTALES:")
print(df['ejemplares_totales'].mean())
print("\n13. MAYOR CANTIDAD DE EJEMPLARES:")
print(df['ejemplares_totales'].max())
print("\n14. MENOR CANTIDAD DE EJEMPLARES:")
print(df['ejemplares_totales'].min())
# 9. Ordenamiento, filtrado y agrupación
print("\n--- 9. ORDENAMIENTO, FILTRADO Y AGRUPACIÓN ---")
print("\n15. LIBROS ORDENADOS POR AÑO DE PUBLICACIÓN:")
print(df.sort_values(by='ano_publicacion', ascending=False))
print("\n16. LIBROS CON MÁS DE 3 EJEMPLARES PRESTADOS:")
filtro = df[df['ejemplares_prestados'] > 3]
print(filtro)
print("\n17. RESUMEN POR GÉNERO:")
resumen = df.groupby('genero').agg(
    cantidad_libros=('isbn', 'count'),
    promedio_ejemplares=('ejemplares_totales', 'mean'),
    total_prestados=('ejemplares_prestados', 'sum')
)
print(resumen)
# 18. Gráfica de barras: Libros por género
print("\n18. GRÁFICA DE BARRAS: LIBROS POR GÉNERO")
conteo = df['genero'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Libros por género - Daniel 1392')
plt.xlabel('Género')
plt.ylabel('Cantidad de libros')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 19. Gráfica de barras: Ejemplares prestados por libro
plt.figure(figsize=(8, 5))
plt.bar(df['titulo'], df['ejemplares_prestados'], color='lightgreen')
plt.title('Ejemplares prestados por libro - Daniel 1392')
plt.xlabel('Título del libro')
plt.ylabel('Ejemplares prestados')
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 20. Histograma: Distribución de años de publicación
plt.figure(figsize=(8, 5))
plt.hist(df['ano_publicacion'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de años de publicación - Daniel 1392')
plt.xlabel('Año de publicación')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 21. Gráfica de dispersión: Ejemplares totales vs prestados
plt.figure(figsize=(8, 5))
plt.scatter(
    df['ejemplares_totales'],
    df['ejemplares_prestados'],
    color='red',
    s=100
)
plt.title('Ejemplares totales vs prestados - Daniel 1392')
plt.xlabel('Ejemplares totales')
plt.ylabel('Ejemplares prestados')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 22. Diagrama de caja: Distribución de ejemplares
plt.figure(figsize=(7, 5))
plt.boxplot(
    df['ejemplares_totales'],
    patch_artist=True,
    boxprops=dict(facecolor='lightblue')
)
plt.title('Distribución de ejemplares totales - Daniel 1392')
plt.ylabel('Cantidad de ejemplares')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
# 23. Matriz de correlación
# Convertir fecha a formato numérico para el análisis
df['fecha_ultimo_prestamo'] = pd.to_datetime(
    df['fecha_ultimo_prestamo']
)
df['fecha_numerica'] = (
    df['fecha_ultimo_prestamo'].astype('int64')
)
correlacion = df.corr(numeric_only=True)
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)
plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(
    range(len(correlacion.columns)),
    correlacion.columns,
    rotation=45
)
plt.yticks(
    range(len(correlacion.columns)),
    correlacion.columns
)
plt.title('Matriz de correlación de libros - Daniel 1392')
plt.tight_layout()
plt.show()