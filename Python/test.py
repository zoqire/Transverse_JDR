#import scipy
#import numpy
#import sklearn
#from sklearn import datasets
import time
from random import randint
        
#class 

class Wizard:
    
    def __init__(self,nom):
        self.id = 1
        self.nom = nom                                                          #String
        self.hp = 3465                                                            #int
        self.Resistance = 20
        self.Armure = 205                                                         #int
        self.Cp_Critique = 38                                                    # %
        self.Block = 10
        self.Attack = 218 
        self.precision = 90                                                        # %
        self.provocation = 25
        self.attaqueCible = [0,1,0]        
        self.attaquesNom = ["Boule  de  feu","Chaine  d’eclairs","Meteore"]     #tab string
        self.attaquesDammage = [184,125,250]
        self.attaquesCooldown = [0,3,6]
        
        
class Assassin:
    
    def __init__(self,nom):
        self.id = 2
        self.nom = nom                                                          #String
        self.hp = 3540                                                            #int
        self.Resistance = 27
        self.Armure = 153                                                         #int
        self.Cp_Critique = 29                                                    #%
        self.Block = 10
        self.Attack = 266 
        self.precision = 93                                                        #%
        self.provocation = 21
        self.attaqueCible = [0,0,0]        
        self.attaquesNom = ["Coup de dague","Lame fantome","Assomoir"]     #tab string
        self.attaquesDammage = [140,180,70]
        self.attaquesCooldown = [0,4,5]
        

class Warrior:
    
    def __init__(self,nom):
        self.id = 3
        self.nom = nom                                                          #String
        self.hp = 3930                                                            #int
        self.Resistance = 42
        self.Armure = 215                                                         #int
        self.Cp_Critique = 14                                                    #%
        self.Block = 15
        self.Attack = 230 
        self.precision = 89                                                        #%
        self.provocation = 30
        self.attaqueCible = [0,0]        
        self.attaquesNom = ["Charge feroce","Provocation"]     #tab string
        self.attaquesDammage = [150,0]
        self.attaquesCooldown = [0,3]
        
"""        
class Priest:
    
    def __init__(self,nom):
        self.nom = nom                                                          #String
        self.hp = 3465                                                          #int
        self.Resistance = 22
        self.Armure = 201                                                       #int
        self.Cp_Critique = 25                                                   # %
        self.Block = 18
        self.Attack = 223 
        self.precision = 94                                                     # %
        self.provocation = 18
        self.attaqueCible = [0,0,0]        
        self.attaquesNom = ["Chatiment","Guerison sacre","Vitesse sacre"]       #tab string
        self.attaquesDammage = [130,-720,0]
        self.attaquesCooldown = [0,3,6]
"""
        
        
class Mob:
    
    def __init__(self,nom):
        self.id = 0
        self.nom = nom                                                          #String
        self.hp = 15000                                                         #int
        self.Resistance = 43
        self.Armure = 350                                                       #int
        self.Cp_Critique = 35                                                   # %
        self.Block = 35
        self.Attack = 400 
        self.precision = 95
        self.attaqueCible = [0,1,0,0,1,0]        
        self.attaquesNom = ["Enchainement furieux","Impact monstrueux","Coup de griffe","Morsure","Souffle de feu","Regeneration"]     #tab string
        self.attaquesDammage = [150,230,170,250,200,-4500]
        self.attaquesCooldown = [0,4,0,3,4,6]
        
    def test(self,enemy,choix,mon_fichier):
        basedmg = self.Attack
        dmg = 0
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if choix != 5 :
                    dmg = basedmg + self.attaquesDammage[choix]
                else :
                    dmg = self.attaquesDammage[5]
                    
                if randint(1,100) <= self.Cp_Critique:
                    if choix != 5 :
                            dmg = dmg*2 + enemy.Armure
                            
                if choix == 5 :
                    print "\n[", self.nom, " heal himself of ", (-dmg), " hp !]"
                    dmg = dmg + enemy.Armure
                else :
                    print "\n[", self.nom, " has dealt " , dmg, " dammage to ", enemy.nom, " !]" 
                
                enemy.hp -= dmg - enemy.Armure
                
            elif choix != 5 : 
                print "\n[", self.nom, " attack on ", enemy.nom, " has been blocked!]"
            else :
                dmg =  self.attaquesDammage[5]
                enemy.hp -= dmg
                print "\n[", self.nom, " heal himself of ", -dmg, " hp !]"
                
        else:
            print "\n[", self.nom, " missed ", enemy.nom, " !]"
        
        
        mon_fichier.write(str(choix))
        mon_fichier.write(",")
        mon_fichier.write(str(enemy.id))
        mon_fichier.write(",")
        mon_fichier.write(str(dmg))
        mon_fichier.write(",")
        mon_fichier.write(str(self.attaquesCooldown[choix]))
        mon_fichier.write(",")
        if dmg >= 800 :
            mon_fichier.write("1")
        elif dmg <= -800 :
            mon_fichier.write("1")
        else :
            mon_fichier.write("0")
        mon_fichier.write(",\n")
        
        #id_attaque,id_cible,dmg,cldwn
        
        enemy.hp += dmg
                
        


        
print "\n\n      Projet Transverse\n\n"
print "Notre IA va se retrouver en combat avec 3 personnages dont les "
print "actions sont automatises par notre programme"

IA = Mob('0')
Joueur1 = Wizard('1')
Joueur2 = Assassin('2')
Joueur3 = Warrior('3')
#Joueur4 = Priest("Priest")

print(IA.nom)

print(Joueur1.attaquesCooldown[1])

mon_fichier = open("fichier.csv", "w")

nbSample = 200

mon_fichier.write(str(nbSample))
mon_fichier.write(",5,id_attaque,id_cible,degats,cooldown,efficacite,\n")

i=0
while i < nbSample :
    
    choixAttack = randint(0,5)
    choixTarget = randint(1,3)
    
    if choixAttack == 5:
        IA.test(IA,choixAttack,mon_fichier)
    elif choixTarget == 1:
        IA.test(Joueur1,choixAttack,mon_fichier)
    elif choixTarget == 2:
        IA.test(Joueur2,choixAttack,mon_fichier)
    elif choixTarget == 3:
        IA.test(Joueur3,choixAttack,mon_fichier)
    i+=1
   
mon_fichier.close()

