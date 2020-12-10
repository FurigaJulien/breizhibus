import mysql.connector
from BreizhibusClass import *
import time


class BDD():

   

    @classmethod
    def connect(cls):
        cls.link = mysql.connector.connect(**{
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'database': 'breizhibus'
            })
        cls.cursor=cls.link.cursor()
        

    @classmethod
    def getLines(cls):
        cls.connect()
        busLineList=[]
        get_query="Select * from lignes"
        cls.cursor.execute(get_query)
        list=cls.cursor.fetchall()
        for row in list:

            id=int(row[0])
            name=str(row[1])
            busLine=Busline(id,name)
            busLineList.append(busLine)
        cls.close()
        return busLineList

    @classmethod
    def getStops(cls,id_ligne):
        cls.connect()
        stops=[]
        get_query="SELECT arrets.id_arret,nom,adresse,sens FROM arrets JOIN arrets_lignes ON arrets.id_arret = arrets_lignes.id_arret WHERE id_ligne ="+str(id_ligne)
        cls.cursor.execute(get_query)
        list=cls.cursor.fetchall()
        for row in list:
            id=int(row[0])
            name=str(row[1])
            adress=str(row[2])
            sens=int(row[3])
            stop=Stop(id,name,adress,sens)
            stops.append(stop)
        cls.close()
        return stops,id_ligne

    @classmethod
    def getBus(cls):
        cls.connect()
        busList=[]
        get_query="SELECT bus.id_bus,bus.numero,bus.immatriculation,bus.nombre_place,bus.id_ligne,lignes.nom FROM bus JOIN lignes ON bus.id_ligne=lignes.id_ligne"
        cls.cursor.execute(get_query)
        liste=cls.cursor.fetchall()
        for row in liste:
            id=int(row[0])
            number=str(row[1])
            registration=str(row[2])
            nb_place=str(row[3])
            line_id=str(row[4])
            line_name=str(row[5])

            bus=Bus(id,number,registration,nb_place,line_id,line_name)
            busList.append(bus)
        cls.close()
        return busList

    @classmethod
    def createBus(cls,name,number,registration,numberPlace):
        
        query="INSERT INTO `bus` ( `numero`, `immatriculation`, `nombre_place`, `id_ligne`) VALUES (%s,%s,%s,%s)"
        idLigne=cls.getIdLigne(name)
        cls.connect()
        cls.cursor.execute(query,(number,registration,numberPlace,idLigne))
        cls.link.commit()
        cls.close()

    @classmethod
    def getIdLigne(cls,nom_ligne):
        busLine=cls.getLines()
        for element in busLine:
            if element.name==nom_ligne:
                return element.id

    @classmethod
    def updateBusInBase(cls,bus,number,registration,numberPlace,idLigne):
        cls.connect()
        query="UPDATE `bus` SET `numero` = '{}', `immatriculation` = '{}', `nombre_place` = '{}', `id_ligne` = '{}' WHERE `bus`.`id_bus` = '{}'".format(number,registration,numberPlace,idLigne,bus.id)
        cls.cursor.execute(query)
        cls.link.commit()
        cls.close()
        
    @classmethod
    def deleteBus(cls,bus):
        cls.connect()
        query="DELETE FROM `bus` WHERE bus.id_bus = {}".format(bus.id)

        cls.cursor.execute(query)
        cls.link.commit()
        cls.close()

    @classmethod
    def close(cls):
        cls.cursor.close()
        cls.link.close()
