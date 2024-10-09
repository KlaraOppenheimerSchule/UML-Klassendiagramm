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
        if spieler == None:
            return None

        else:
            self.__strassenname = strassenname
            self.__miete = miete
            self.__besitzer = spieler
    
    #getBesitzer
    def getBesitzer(self):
        return self.__besitzer.getName()
    

# Test   
sp1 = spieler('Max', 100.00)
st1 = strasse('Badstrasse',1000.00, sp1)
st2 = strasse('Badstrasse',1000.00, None)


# Besitzer ausgeben lassen
print(st1.getBesitzer())
print(st2.getBesitzer())
