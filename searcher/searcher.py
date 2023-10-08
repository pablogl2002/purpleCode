import sqlalchemy
import pandas as pd
import mysql.connector

class Searcher:
  
    pointer = None

    def __init__(self):
        print("preconexion")
        self.conexion = mysql.connector.connect(
            host='bookspace.earth',
            port=3306,
            user='user123',
            password='pass123',
            database='bookspace'
        )        
        print("postconexion | precursor")  # (bookspace

        #s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)
        #self.engine = sqlalchemy.create_engine(s)


    def get_cursor(self):
        return self.conexion.cursor()

    def get_planet(self, planet):   
        columns = ["sun_distance", "earth_distance", "year_length", "day_length", "diameter", "mass", "density", "known_satellites", "avg_orbital", "avg_temperatures", "description", "images", "offer_title", "offer_description"]

        pointer = self.get_cursor()
        pointer.execute(f'SELECT * FROM planets WHERE name = "{planet}"')
        planets = pointer.fetchall()
        self.planet_json(columns, planets)
        return planets


    def planet_json(self, columns, t):
        datos = {}
        print(len(t))
        for i in range(len(columns)):
            datos[columns[i]] = t[0][i]            

    def moon_json(self, columns, t):
        datos = {}
        print(len(t))
        j=0
        for l in t:
            print(l)
            for j in range(len(columns)):
                print(columns[j])
                datos[columns[j]] = datos.get(columns[j], []) + [l[j]]

        return datos


    def get_moon(self, planet):
        columns = ["name", "planet", "planet_distance", "diameter", "orbit_days", "description"]

        pointer = self.get_cursor()
        pointer.execute('SELECT * FROM moons')
        lunas = pointer.fetchall()
        #print(lunas)
        print(self.moon_json(columns, lunas))
        return lunas
    
    def insert_moons_data(self, moons):
        consulta = "INSERT INTO moons (name, planet_distance, diameter, orbit_days, description, planet) VALUES (%s, %s, %s, %s, %s, %s)"
        # Realiza inserciones en la base de datos para cada conjunto de datos en el diccionario
        for i in range(len(moons["name"])):
            valores = (
                moons["name"][i],
                moons["planet_distance"][i],
                moons["diameter"][i],
                moons["orbit_days"][i],
                moons["description"][i],
                moons["planet"][i]
            )
            self.get_cursor().execute(consulta, valores)

        # Confirma los cambios en la base de datos
        self.conexion.commit()

        # Cierra el cursor y la conexión


    def insert_planets_data(self, lista):
        print('preentrada')

        consulta = "INSERT INTO planets (name, sun_distance, earth_distance, year_length, day_length, diameter, mass, density, known_satellites, avg_orbital, avg_temperatures, description, images) VALUES (%s, %s, %s, %s, %s, %s,%s ,%s, %s, %s, %s, %s, %s)"

        for i in range(len(lista["name"])):
            valores = (
                lista["name"][i],
                lista["sun_distance"][i],
                lista["earth_distance"][i],
                lista["year_length"][i],
                lista["day_length"][i],
                lista["diameter"][i],
                lista["mass"][i],
                lista["density"][i],
                lista["known_satellites"][i],
                lista["avg_orbital"][i],
                lista["avg_temperatures"][i],
                lista["description"][i],
                lista["images"][i]
            )

        self.get_cursor().execute(consulta, valores) 
        self.conexion.commit()

        print('comiteado')


