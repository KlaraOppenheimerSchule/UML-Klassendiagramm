from pickle import NONE

class spieler():
       
    
#constructor
    def __init__(self, spielername, konto):
        self.__spielername = spielername
        self.__konto = konto
        
#getName
    def getName(self):
        return self.__spielername
  
# Class Strasse
class strasse():
     
    #constructor
    def __init__(self, strassenname, miete):
        self.__strassenname = strassenname
        self.__miete = miete
        self.__besitzer = [spieler] = NONE
    
    #getBesitzer
    def getBesitzer(self):
        return self.__besitzer
    
    
    #addBesitzer
    def addBesitzer(self, besitzer):
        self.__besitzer = besitzer
        
      
    #Remove Besitzer      
    def removeBesitzer(self):
        self.__besitzer == None
    
sp1 = spieler('max', 100.00)

st1 = strasse('Badstrasse',1000.00)

st1.addBesitzer(sp1)

print(st1.getBesitzer().getName())

st1.removeBesitzer()



