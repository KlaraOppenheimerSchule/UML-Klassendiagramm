from pickle import FALSE, NONE

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
    def __init__(self, strassenname, miete, spieler):
        self.__strassenname = strassenname
        self.__miete = miete
        self.__besitzer = spieler
    
    #getBesitzer
    def getBesitzer(self):
        if self.__besitzer is NONE:
            return 'Die Strasse hat keinen Besitzer'
        else:
            return self.__besitzer.getName()
    

# Test   
sp1 = spieler('Max', 100.00)
st1 = strasse('Badstrasse',1000.00, sp1)


# Besitzer ausgeben lassen
print(st1.getBesitzer())


