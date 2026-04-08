import json

directorio='/home/devasc/labs/devnet-src/parsing/myfile.json'

# Abre el archivo y lo asigna a la variable json_file
with open(directorio, 'r') as json_file:
    # Utiliza json.load para cargar el contenido en ourjson
    ourjson = json.load(json_file)

# Asumiendo las llaves típicas de los laboratorios DevNet para el token
print("Valor del Token:", ourjson.get('access_token'))
print("Tiempo restante antes de caducar:", ourjson.get('expires_in'))
