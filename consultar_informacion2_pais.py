"""
    Consultar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.tareasprogavanz
coleccion = db.paises

# se usa método find_one con parámetros, a partir de la colección
print("Muestra un solo documento de la base de datos")
data_01 = coleccion.find_one({'nombre':'Ecuador'})
print(data_01)

# se usa método find con parámetros, a partir de la colección
print("Muestra todos los documentos de la base de datos que cumplan con la \
condición")
data_02 = coleccion.find({'numero_poblacion':{"$lt":17757000}})
for registro in data_02:
    print(registro)
