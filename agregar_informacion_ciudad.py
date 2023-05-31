"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.tareasprogavanz
coleccion = db.ciudades

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario va con {}

# proceso que agrega un solo documento
#data_01 = {"nombre": "Cuenca", "provincia": "Azuay",
#"pais":"Ecuador", "numero_poblacion": 580000}
# coleccion.insert_one(data_01) / agregar de uno en uno (preferí cargar en lista).

# proceso que agrega una lista de documentos/ igual es de tipo diccionario
lista = [
{"nombre": "Quito", "provincia": "Pichincha",
"pais":"Ecuador", "numero_poblacion": 2827106},
{"nombre": "Guayaquil", "provincia": "Guayas",
"pais":"Ecuador", "numero_poblacion": 2698077}
]

coleccion.insert_many(lista)
