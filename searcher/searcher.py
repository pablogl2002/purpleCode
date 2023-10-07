import sqlalchemy

class Searcher:

    def __init__(self, user, pasw, ip, name):
        db_username = user          #Usuario externo que hemos creado (user123)
        db_password = pasw          #Contraseña del usuario externo (passpass)
        db_ip = ip                  #IP externa de la instancia     
        db_name = name                 # (bookspace)
        s = 'mysql+mysqlconnector://{0}:{1}@{2}/{3}'.format(db_username, db_password, db_ip, db_name)
        self.engine = sqlalchemy.create_engine(s)

    def get_from_planetas(self, planeta = "Earth", columna="desc"):   
        planets = self.engine('SELECT ' + columna + 'FROM tablaPlanetas WHERE planeta = ' + planeta)
        return planets

    def get_lunas(self):
        lunas = self.engine('SELECT * FROM tablaLunas')
        return lunas
    
