"""
    Eliminar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.tareasprogavanz
coleccion = db.paises

print("Muestra todos los documentos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)

# se usa método delete_many con parámetros, a partir de la colección
# para eliminar un documento de la colección
print("Proceso para borrar un documento de una colección")
coleccion.delete_many({'numero_poblacion':17757000})

print("Muestra todos los documentos")
data_02 = coleccion.find()
for registro in data_02:
    print(registro)
