import requests, re, json

def extractFromRegularExpresion(regex, data):
    if data:
        return re.findall(regex, data)
    return None

try:
    with open(r"C:\Users\sergi\OneDrive\Desktop\TRABAJOS UNIVERSIDAD\Apache ejercicio\access.log") as data:
        contenido = data.read()
    
    regex = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s\-\s\-\s\[(\d{2}/[a-zA-Z]{3}/\d{4}):(\d{2}:\d{2}:\d{2})\s\+\d{4,6}]\s\"([A-Z]{3,7})"

    resultado = extractFromRegularExpresion(regex, contenido)

    for i in resultado:
        print(f"La IP: {i[0]}, la fecha es: {i[1]}, la hora: {i[2]} y el método: {i[3]}")
        
except FileNotFoundError:
    print("Error: El archivo no se encontró en la ruta especificada.")
except Exception as e:
    print(f"Se produjo un error: {e}")


