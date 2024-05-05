from fastapi import FastAPI
import psycopg2
import psycopg2.extensions
import modulos as mod

app = FastAPI()
'''db_params = {
    'dbname': 'my_collections',
    'user': 'postgres',
    'password': '1234',
    'host': 'localhost',
    'port': '5432',
      
}'''



conn = psycopg2.connect(**db_params)

print('Conexión exitosa')

# Se crea una nueva base de datos
query = '''CREATE TABLE My_movies(

ID SERIAL PRIMARY KEY,
AUTOR VARCHAR(255),
DESCRIPCION TEXT,
FECHA_ESTRENO VARCHAR(255)



)'''

conn = psycopg2.connect(**db_params)
print('Conexión exitosa')

try:
    

    cursor = conn.cursor()
    query = '''
    INSERT INTO My_movies (AUTOR, DESCRIPCION, FECHA_ESTRENO)
    VALUES ('Francis Ford Coppola', 'EL PADRINO - Las familias mafiosas de Nueva York entran en conflicto cuando el capo de una de las más poderosas, Vito Corleone, se opone a que la Cosa Nostra entre en el negocio del tráfico de drogas.', '1972-02-26')
    '''




    cursor.execute(query)
    conn.commit()
    print('Tabla creada exitosamente')

except Exception as e:
    print(f'El error es {str(e)}')  # Convertir el error a una cadena Unicode antes de imprimirlo

finally:
    if conn:
        cursor.close()
        conn.close()
        print('Conexiones cerradas')



