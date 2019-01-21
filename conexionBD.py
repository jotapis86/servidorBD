import sqlite3

class ConexionBD:
    def __init__(self, bd):
        self.bd = bd
        
    def conectar(self):
        try:
            self.conexion = sqlite3.connect(self.bd)
            self.cursor = self.conexion.cursor()
        except Exception, e:
            print "ConexionBD::conectar - ", e

    def ejecutarSQL(self, s):
        self.cursor.execute(s)
        return self.cursor.fetchall()

    def commit(self):
        self.conexion.commit()

    def rollback(self):
        self.conexion.rollback()

    def desconectar(self):
        self.cursor.close()
