class Busline():
    def __init__(self,id,name,stop=[]):
        self.id=id
        self.name=name
        self.stop=stop
    
    def __repr__(self):
        return self.name

class Stop():
    def __init__(self,id,name,adress,sens):
        self.id=id
        self.name=name
        self.adress=adress
        self.sens=sens

    def __repr__(self):
        return self.name

class Bus():
    def __init__(self,id,number,registration,nb_place,line_id,line_name):
        self.id=id
        self.number=number
        self.registration=registration
        self.nb_place=nb_place
        self.line_id=line_id
        self.line_name=line_name

    def __repr__(self):
        return "["+str(self.id) + ","+str(self.number)+ ","+str(self.registration)+ ","+str(self.nb_place)+ ","+str(self.line_id)+ ","+str(self.line_name)+"}"

