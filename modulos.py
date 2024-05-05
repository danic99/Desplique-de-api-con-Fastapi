import json
from cryptography.fernet import Fernet

def cred():

 '''Desencriptar las credenciales necesaias para la conexion'''

 with open(r"C:\Users\USUARIO\ApiTrabajo\ApiTrabajo_cred.txt",'r') as archivo:
    data = archivo.read()
    data =  json.loads(data)

 with open(r"C:\Users\USUARIO\ApiTrabajo\ApiTrabajo_masc.txt",'r') as masc:
      mascara = masc.read()
   
 fernet = Fernet(mascara)

 valores = []
 for i in data:
    for clave,valor  in i.items():
       valores.append(fernet.decrypt(valor).decode())

 return valores



