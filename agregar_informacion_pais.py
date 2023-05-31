"""
    Agregar información en una colección de MongoDB
    desde Python
"""
from enlace_base import client

# se obtiene la colección general (base de datos)

db = client.tareasprogavanz
coleccion = db.paises

# conjunto de datos a guardar en la colección
# importante, aquí se usa la estructura de Python denominada diccionario va con {}

# proceso que agrega un solo documento
#data_01 = {"nombre": "Colombia", "Continente": "Sur América",
#"capital":"Bogotá", "numero_poblacion": 51609000}
# coleccion.insert_one(data_01) / agregar de uno en uno (preferí cargar en lista).

# proceso que agrega una lista de documentos/ igual es de tipo diccionario
lista = [
{"nombre": "Ecuador", "Continente": "Sur América",
"capital":"Quito", "numero_poblacion": 17757000},
{"nombre": "Argentina", "Continente": "Sur América",
"capital":"Buenos Aires", "numero_poblacion": 46000000}
]

coleccion.insert_many(lista)
