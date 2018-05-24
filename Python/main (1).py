import scipy
import numpy
import sklearn
from random import randint
from sklearn import datasets
        
#class 

class Wizard:
    
    def __init__(self,nom):
        self.nom = nom                                                          #String
        self.hp = 4000                                                            #int
        self.Armure = 200                                                        #int
        self.Cp_Critique = 35                                                    # %
        self.Block = 25
        self.Attack = 450 
        self.precision = 90                                                        # %
        self.attaqueCible = [0,1,0]        
        self.attaquesNom = ["Boule  de  feu","Chaine  d’eclairs","Meteore"]     #tab string
        self.attaqueDammage = [200,250,350]
        self.attaqueCooldown = [0,3,6]
        
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    if self.attaqueCooldown[2] == 6:
                        dmg = basedmg + self.attaqueDammage[2]
                        enemy.hp -= dmg * 2
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2))
                        self.attaqueCooldown[2] = 0
                    elif self.attaqueCooldown[1] == 4:
                        dmg = basedmg + self.attaqueDammage[1]
                        enemy.hp -= dmg * 2
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2))
                        self.attaqueCooldown[1] = 0
                    else:
                        dmg = basedmg + self.attaqueDammage[0]
                        enemy.hp -= dmg * 2
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2))
                elif self.attaqueCooldown[2] == 6:
                    dmg = basedmg + self.attaqueDammage[2]
                    enemy.hp -= dmg - enemy.Armure
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[2] = 0
                elif self.attaqueCooldown[1] == 4:
                    dmg = basedmg + self.attaqueDammage[1]
                    enemy.hp -= dmg - enemy.Armure
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[1] = 0
                else:
                        dmg = basedmg + self.attaqueDammage[0]
                        enemy.hp -= dmg  - enemy.Armure
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg))                     
            else: print ("\n[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: print ("\n[%s missed %s !]" % (self.nom,enemy.nom))
        self.attaqueCooldown[2] += 1
        self.attaqueCooldown[1] += 1
 
       
class Thief:
    
    def __init__(self,nom):
        self.nom = nom                                                          #String
        self.hp = 3500                                                           #int
        self.Armure = 153                                                         #int
        self.Cp_Critique = 45                                                    #%
        self.Block = 30
        self.Attack = 500 
        self.precision = 95                                                        #%
        self.attaqueCible = [0,0,0]        
        self.attaquesNom = ["Coup de dague","Lame fantome"]     #tab string
        self.attaqueDammage = [240,380]
        self.attaqueCooldown = [0,4]
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    if self.attaqueCooldown[1] == 4:
                        dmg = basedmg + self.attaqueDammage[1]
                        enemy.hp -= dmg * 2
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2)) 
                        self.attaqueCooldown[1] = 0
                    else:
                        dmg = basedmg + self.attaqueDammage[0]
                        enemy.hp -= dmg * 2
                        print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2)) 
                elif self.attaqueCooldown[1] == 4:
                    dmg = basedmg + self.attaqueDammage[1]
                    enemy.hp -= dmg - enemy.Armure
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg)) 
                    self.attaqueCooldown[1] = 0
                else:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg  - enemy.Armure
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg))              
            else: print ("\n[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: print ("\n[%s missed %s !]" % (self.nom,enemy.nom))
        self.attaqueCooldown[1] += 1
        
    def choixAttack(self) :
        if self.attaqueCooldown[4] >= 4 :
            return 4
        elif self.attaqueCooldown[1] >= 4 :
            return 1
        elif self.attaqueCooldown[3] >= 3 :
            return 3
        elif self.attaqueCooldown[2] >= 1 :
            return 2
        elif self.attaqueCooldown[0] >= 0 :
            return 0

class Warrior:
    
    def __init__(self,nom):
        self.nom = nom                                                          #String
        self.hp = 5000                                                            #int
        self.Armure = 250                                                         #int
        self.Cp_Critique = 25                                                    #%
        self.Block = 35
        self.Attack = 350 
        self.precision = 90                                                        #%
        self.attaqueCible = [0]        
        self.attaquesNom = ["Charge feroce"]     #tab string
        self.attaqueDammage = [150]
        self.attaqueCooldown = [0]
        
    def attack(self, enemy):
        basedmg = self.Attack
        if randint(1,100) <= self.precision:
            if randint(1,100) >= enemy.Block:
                if randint(1,100) <= self.Cp_Critique:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg * 2
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg*2)) 
                else:
                    dmg = basedmg + self.attaqueDammage[0]
                    enemy.hp -= dmg  - enemy.Armure
                    print ("\n[%s  has dealt %d dammage !]" % (self.nom,dmg))               
            else: print ("\n[%s blocked %s attack !]" % (enemy.nom,self.nom))
        else: print ("\n[%s missed %s !]" % (self.nom,enemy.nom))        
        
        
class Mob:
    
    def __init__(self,nom):
        self.nom = nom                                                          #String
        self.hp = 15000                                                         #int
        self.Armure = 300                                                       #int
        self.Cp_Critique = 40                                                   # %
        self.Block = 15
        self.Attack = 400 
        self.precision = 95
        self.attaqueCible = [0,1,0,0,1,0]        
        self.attaquesNom = ["Enchainement furieux","Impact monstrueux","Coup de griffe","Morsure","Souffle de feu","Regeneration"]     #tab string
        self.attaquesDammage = [250,330,270,350,300,-4500]
        self.attaqueCooldown = [0,4,1,3,4,6]
        
    def attack(self,enemy,choix):
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
                        dmg = dmg * 2 + enemy.Armure
                                
                if choix == 5 :
                    print ("\n[%s  heal himself of %d hp !]" % (self.nom,-dmg))
                    self.hp -= dmg
                else :
                    print ("\n[%s has dealt %d dammage to %s !]" % (self.nom,dmg,enemy.nom)) 
                    
                    enemy.hp -= dmg - enemy.Armure
                    
            elif choix != 5 : 
                print ("\n[%s attack on %s has been blocked!]" % (self.nom,enemy.nom))
            else :
                dmg =  self.attaquesDammage[5]
                enemy.hp -= dmg
                print ("\n[%s heal himself of %d hp !]" % (self.nom,-dmg))
                    
         else:
            print ("\n[%s missed %s !]" % (self.nom,enemy.nom))
         self.attaqueCooldown[choix] = -1
         i = 0
         while(i != 6):
             self.attaqueCooldown[i] += 1
             i+=1
    
print ("\n\n      Projet Transverse\n\n")
print ("Notre IA va se retrouver en combat avec 3 personnages dont les ")
print ("actions sont automatises par notre programme")

IA = Mob("IA")
Joueur1 = Wizard("Wizard")
Joueur2 = Thief("Thief")
Joueur3 = Warrior("Warrior")
#Joueur4 = Priest("Priest")

nbSample = 200

def combat():
    print ("Fight begin")
    cpt = 0
    while (Joueur1.hp > 0 or Joueur2.hp > 0 or Joueur3.hp > 0) and IA.hp > 0:
        print ("\nTurn ",cpt, " !")
        """print ("Wizard : ", Joueur1.hp)
        print ("Thief : ", Joueur2.hp)
        print ("Warrior : ", Joueur3.hp)"""
        print ("AI : ", IA.hp)
        if Joueur1.hp > 0:
            print ("\nWizard attack")
            Joueur1.attack(IA)
        if Joueur2.hp > 0:
            print ("\nThief attack")
            Joueur2.attack(IA)
        if Joueur3.hp > 0:
            print ("\nWarrior attack")
            Joueur3.attack(IA)
        if IA.hp > 0:
            print ("\nThe AI attack")
            choixAttack = randint(0,5)
            choixTarget = randint(1,3)
            if choixAttack == 5:
                IA.attack(IA,choixAttack)
            elif choixTarget == 1:
                if Joueur1.hp > 0:
                    IA.attack(Joueur1,choixAttack)
            elif choixTarget == 2:
                if Joueur2.hp > 0:
                    IA.attack(Joueur2,choixAttack)
            elif choixTarget == 3:
                if Joueur3.hp > 0:
                    IA.attack(Joueur3,choixAttack)
        cpt += 1
        
    if Joueur1.hp <= 0 and Joueur2.hp <= 0 and Joueur3.hp <= 0 :
        print ("\nThe AI won the fight")
        
    else : 
        print ("Players won the fight")
        
combat()