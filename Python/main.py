import scipy
import numpy
import sklearn

import importlib
importlib.import_module('Projet_transverse')

from Projet_transverse import analyses

from sklearn import datasets

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
        self.Block = 21
        self.Attack = 218 
        self.precision = 90                                                        # %
        self.provocation = 25
        self.attaqueCible = [0,1,0]        
        self.attaqueNom = ["Boule  de  feu","Chaine  d'eclairs","Meteore"]     #tab string
        self.attaqueDammage = [184,125,250]
        self.attaqueCooldown = [0,3,6]
        
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    if self.attaqueCooldown[2] == 6:
                        dmg = basedmg + self.attaqueDammage[2]
                        enemy.hp -= dmg * 2
                        print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2))
                        self.attaqueCooldown[2] = 0
                    elif self.attaqueCooldown[1] == 4:
                        dmg = basedmg + self.attaqueDammage[1]
                        enemy.hp -= dmg * 2
                        print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2))
                        self.attaqueCooldown[1] = 0
                    else:
                        dmg = basedmg + self.attaqueDammage[0]
                        enemy.hp -= dmg * 2
                        print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2))
                elif self.attaqueCooldown[2] == 6:
                    dmg = basedmg + self.attaqueDammage[2]
                    enemy.hp -= dmg - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[2] = 0
                elif self.attaqueCooldown[1] == 4:
                    dmg = basedmg + self.attaqueDammage[1]
                    enemy.hp -= dmg - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[1] = 0
                else :
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg  - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg))                     
            else: print ("[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: 
            print ("[%s missed %s !]" % (self.nom,enemy.nom))
            self.attaqueCooldown[2] += 1
            self.attaqueCooldown[1] += 1
 
       
class Assassin:
    
    def __init__(self,nom):
        self.id = 2
        self.nom = nom                                                          #String
        self.hp = 3540                                                            #int
        self.Resistance = 27
        self.Armure = 153                                                         #int
        self.Cp_Critique = 29                                                    #%
        self.Block = 30
        self.Attack = 266 
        self.precision = 93                                                        #%
        self.provocation = 21
        self.attaqueCible = [0,0,0]        
        self.attaqueNom = ["Coup de dague","Lame fantome"]     #tab string
        self.attaqueDammage = [140,180]
        self.attaqueCooldown = [0,4]
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    if self.attaqueCooldown[1] == 4:
                        dmg = basedmg + self.attaqueDammage[1]
                        enemy.hp -= dmg * 2
                        print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2)) 
                        self.attaqueCooldown[1] = 0
                    else:
                        dmg = basedmg + self.attaqueDammage[0]
                        enemy.hp -= dmg * 2
                        print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2)) 
                elif self.attaqueCooldown[1] == 4:
                    dmg = basedmg + self.attaqueDammage[1]
                    enemy.hp -= dmg - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[1] = 0
                else:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg  - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg))              
            else: print ("[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: print ("[%s missed %s !]" % (self.nom,enemy.nom))
        self.attaqueCooldown[1] += 1
         

class Warrior:
    
    def __init__(self,nom):
        self.id = 3
        self.nom = nom                                                          #String
        self.hp = 5000                                                            #int
        self.Resistance = 42
        self.Armure = 215                                                         #int
        self.Cp_Critique = 14                                                    #%
        self.Block = 38
        self.Attack = 230 
        self.precision = 89                                                        #%
        self.provocation = 30
        self.attaqueCible = [0,0]        
        self.attaqueNom = ["Charge feroce"]     #tab string
        self.attaqueDammage = [150]
        self.attaqueCooldown = [0,3]
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg * 2
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg*2)) 
                else:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg  - enemy.Armure
                    print ("[%s has dealt %d dammage !]" % (self.nom,dmg))               
            else: print ("[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: print ("[%s missed %s !]" % (self.nom,enemy.nom))  
        self.attaqueCooldown[1] += 1        
        
        
class Mob:
    
    def __init__(self,nom):
        self.id = 0
        self.nom = nom                                                          #String
        self.hp = 15000                                                         #int
        self.Resistance = 43
        self.Armure = 350                                                       #int
        self.Cp_Critique = 35                                                   # %
        self.Block = 15
        self.Attack = 400 
        self.precision = 95
        self.attaqueCible = [0,1,0,0,1,0]        
        self.attaqueNom = ["Enchainement furieux","Impact monstrueux","Coup de griffe","Morsure","Souffle de feu","Regeneration"]     #tab string
        self.attaqueDammage = [250,330,270,350,300,-4500]
        self.attaqueCooldown = [0,4,1,3,4,6]
        
    def attack(self,enemy,choix):
         basedmg = self.Attack
         dmg = 0
         if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if choix != 5 :
                    dmg = basedmg + self.attaqueDammage[choix]
                else :
                    dmg = self.attaqueDammage[5]
                        
                if randint(1,100) <= self.Cp_Critique:
                    if choix != 5 :
                        dmg = dmg * 2 + enemy.Armure
                                
                if choix == 5 :
                    print ("\n[%s heal himself of %d hp !]" % (self.nom,-dmg))
                    self.hp -= dmg
                else :
                    print ("\n[%s has dealt %d dammage to %s !]" % (self.nom,dmg,enemy.nom)) 
                    
                    enemy.hp -= dmg - enemy.Armure
                    
            elif choix != 5 : 
                print ("\n[%s attack on %s has been blocked!]" % (self.nom,enemy.nom))
            else :
                dmg =  self.attaqueDammage[5]
                enemy.hp -= dmg
                print ("\n[%s heal himself of %d hp !]" % (self.nom,-dmg))
                    
         else:
            print ("\n[%s missed %s !]" % (self.nom,enemy.nom))
         self.attaqueCooldown[choix] = -1
         i = 0
         
         if enemy.hp < 0 :
             enemy.hp = 0
         
         while(i != 6):
             self.attaqueCooldown[i] += 1
             i+=1
        
    def choixAttack(self) :
        if self.attaqueCooldown[3] >= 3 :
            return 3
        elif self.attaqueCooldown[1] >= 4 :
            return 1
        elif self.attaqueCooldown[4] >= 4 :
            return 4
        elif self.attaqueCooldown[2] >= 1 :
            return 2
        else :
            return 0
        #en fonction des cooldowns
        
    def choixTarget(self,Joueur3,Joueur1,Joueur2) : #######################################################
        #choisi la cible en fonction de sa resistance aux attaques
        #utilisation des donnees
        if Joueur3.hp > 0:
            return 3
        elif Joueur1.hp > 0:
            return 1
        elif Joueur2.hp > 0:
            return 2
            
            
def combat():
    print ("\n\nFight begin")
    cpt = 0
    while (Joueur1.hp > 0 or Joueur2.hp > 0 or Joueur3.hp > 0) and (IA.hp > 0) :
        print ("\n\nTurn %d !" % (cpt+1))
        
        print ("Wizard : %d " % (Joueur1.hp))
        print ("Assassin : %d " % (Joueur2.hp))
        print ("Warrior : %d " % (Joueur3.hp))
        print ("AI : %d " % (IA.hp))
        
        if Joueur1.hp > 0:
            print "\nWizard attack"
            Joueur1.attack(IA)
        if Joueur2.hp > 0:
            print ("\nAssassin attack")
            Joueur2.attack(IA)
        if Joueur3.hp > 0:
            print ("\nWarrior attack")
            Joueur3.attack(IA)
        
        print ("\nThe AI attack")
        
        if IA.hp < 10500 and IA.attaqueCooldown[5]==6 :
            IA.attack(IA,5)
        else :
            
            choixAttack = IA.choixAttack()
            choixTarget = IA.choixTarget(Joueur3,Joueur1,Joueur2)            
            
            if choixTarget == 1:
                IA.attack(Joueur1,choixAttack)
            elif choixTarget == 2:
                IA.attack(Joueur2,choixAttack)
            elif choixTarget == 3:
                IA.attack(Joueur3,choixAttack)
        cpt += 1
        
    if Joueur1.hp <= 0 and Joueur2.hp <= 0 and Joueur3.hp <= 0 :
        print ("The AI won the fight")
        
    else : 
        print ("Players won the fight")
        
        
        
       
       
       
       
       
       
       
       

       
       
       
       
       
       
       
       
        
        
        
print "\n\n      Projet Transverse\n\n"
print "Notre IA va se retrouver en combat face a 3 personnages dont les "
print "          actions sont automatises par notre programme"

IA = Mob("AI")
Joueur1 = Wizard("Wizard")
Joueur2 = Assassin("Assassin")
Joueur3 = Warrior("Warrior")

test = analyses()

pause = input()

combat()

pause = input()



















