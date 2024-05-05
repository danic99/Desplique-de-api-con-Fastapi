from fastapi import FastAPI
import sqlalchemy as db
from pydantic import BaseModel
import psycopg2
import modulos as m



app = FastAPI()

db_name,user,password,host,port = m.cred()
db_params = {
    'dbname': db_name,
    'user':user,
    'password': password,
    'host': host,
    'port': port
}

conn = psycopg2.connect(**db_params)
print('Conexión exitosa')

class insertTBL(BaseModel):
    nombre_db: str
    autor: str
    descripcion: str
    fecha: str

class updateTBL(BaseModel):
   nombre_tb: str
   columna_tb: str
   valor_new_columna: str
   nombre_filtro: str
   valor_filtro: str

class deleteTBL(BaseModel):
   nombre_tb: str
   filtro: str
   valor_filtro:str




@app.get('/')
def menu():
   return 'Esta api tiene un metodo get,post,put,delete'

@app.get('/Tblbase/{nombre}')
async def baseDedatos(nombre:str):
    temporal_list = []
    with conn.cursor() as cursor:
      
      try:
       query = f'''SELECT * FROM {nombre}''' 
       cursor.execute(query)
       rows = cursor.fetchall()

       for row in rows:
          print(row)
          temporal_list.append(row)
          

      except Exception as e:
         print(f'Error {e}')
    print('Carga datos')
    return {'Message': temporal_list}
     

@app.post('/new_registro')
def agregar(item:insertTBL):
 temporal_list = []
 with conn.cursor() as cursor:
    try:
       query = f'''INSERT INTO {item.nombre_db}(autor, descripcion, fecha_estreno)  VALUES (%s, %s, %s) ''' 
       values =(item.autor,item.descripcion,item.fecha)
       cursor.execute(query,values)
       conn.commit()

    except Exception as e:
         print(f'Error {e}')
    temporal_list.append(values)
    print('insersion datos')
 return {'Message': temporal_list}



@app.put('/upddate_registro')
def actualizar(item:updateTBL):
 
 with conn.cursor() as cursor:
   try:
       query = f'''UPDATE {item.nombre_tb} SET {item.columna_tb} = %s where {item.nombre_filtro} = %s ''' 
       values =(item.valor_new_columna,item.valor_filtro)
       cursor.execute(query,values)
       conn.commit()
       return 'Correcta update'

   except Exception as e:
         print(f'Error {e}')


@app.delete('/delete_registros')
def borrar(item:deleteTBL):
   
 with conn.cursor() as cursor:
   try:
       query = f'''DELETE FROM {item.nombre_tb} WHERE {item.filtro} = %s ''' 
       values =(item.valor_filtro)
       cursor.execute(query,values)
       conn.commit()
       return 'Correcta delete'

   except Exception as e:
         print(f'Error {e}')
  
   