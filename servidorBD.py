from conexionBD import *

class bd:
    def __init__(self):
        self.conexion = ConexionBD("bd")
        self.conexion.conectar()

    def __del__(self):
        self.conexion.desconectar()

    def getVuelo(self, aerolinea, numVuelo, fecha):
        return self.conexion.ejecutarSQL("""select aerolinea, numVuelo, fecha, STD, ATD
                                         from vuelos
                                         where aerolinea = '%s' and numVuelo = '%s' and fecha = '%s'""" %(aerolinea, numVuelo, fecha))

    def ingresarVueloProgramado(self, aerolinea, numVuelo, fecha, STD):
        try:
            self.conexion.ejecutarSQL("""
                                      insert into vuelos (aerolinea, numVuelo, fecha, STD)
                                      values ('%s', '%s', '%s', '%s')"""%(aerolinea, numVuelo, fecha, STD))
        except Exception, e:
            self.conexion.rollback()
            print str(e)
            return False
        self.conexion.commit()
        return True

    def actualizarVuelo(self, aerolinea, numVuelo, fecha, ATD):
        try:
            self.conexion.ejecutarSQL("""
                                      update vuelos set ATD='%s'
                                      where aerolinea='%s' and numVuelo='%s' and fecha='%s'"""
                                      %(ATD, aerolinea, numVuelo, fecha))
        except Exception, e:
            self.conexion.rollback()
            print str(e)
            return False
        self.conexion.commit()
        return True


# probando
vuelos = bd()
vuelos.ingresarVueloProgramado("AV", "9320", "2018-01-20", "16:20")
print vuelos.getVuelo("AV", "9320", "2018-01-20")
vuelos.actualizarVuelo("AV", "9320", "2018-01-20", "16:25")
print vuelos.getVuelo("AV", "9320", "2018-01-20")
