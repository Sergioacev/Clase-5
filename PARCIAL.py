import requests, re, json

ipsAlmacenadas = {}

def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None

# Abrir y leer el archivo
with open(r"C:\Users\sergi\OneDrive\Desktop\TRABAJOS UNIVERSIDAD\Apache ejercicio\access.log", "r", encoding="utf-8") as file:
    data = file.read()

# Expresión regular para extraer los datos
regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\-\s\-\s\[(\d{2}\/\b[a-zA-Z]{3}\b\/\d{4}):(\d{2}:\d{2}:\d{2})\s\+\d{4,6}]\s\"([A-Z]{3,7})\s(\/\S+)\sHTTP\/\d{1}\.\d{1}\"\s(\d{3})"

# Extraer datos del archivo
resultado = extractFromRegularExpresion(regex, data)

# Procesar cada línea del log
for entry in resultado:
    ip = entry[0]  # Dirección IP
    codigo = entry[5]  # Código de estado (200, 300, 400, etc.)

    # Si la IP no está registrada, la agregamos con un diccionario de códigos
    if ip not in ipsAlmacenadas:
        ipsAlmacenadas[ip] = {"200": 0, "300": 0, "400": 0, "500": 0}

    # Contabilizar el código en la IP correspondiente
    if codigo.startswith("2"):
        ipsAlmacenadas[ip]["200"] += 1
    elif codigo.startswith("3"):
        ipsAlmacenadas[ip]["300"] += 1
    elif codigo.startswith("4"):
        ipsAlmacenadas[ip]["400"] += 1
    elif codigo.startswith("5"):
        ipsAlmacenadas[ip]["500"] += 1

# Mostrar resultados en formato JSON
print(json.dumps(ipsAlmacenadas, indent=4))

