
import time
import random
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
from Adafruit_CharLCD import Adafruit_CharLCD

lcd = Adafruit_CharLCD(25,24,23,17,27,22,16,2,None)
lcd.clear()


class char:
    def __init__(self,name,hp,gp,br,inv):
        self.name=name
        self.hp=hp
        self.gp=gp
        self.br=br
        self.inv=inv

class healing:
    def __init__(self,name,heal,cost):
        self.name=name
        self.heal=heal
        self.cost=cost

    def __str__(self):
        return("You eat the \n"+self.name+".")


class enemy:
    def __init__(self,name,damage):
        self.name=name
        self.damage=damage
    def __str__(self):
        return("Attacked by \n"+self.name+"!")


#Player
player=char("player",100,30,0,[])
#Healing
bread=healing("Bread",10,5)
stew=healing("Stew",20,8)
meat=healing("Meat",50,20)

listOfHeals=[bread,stew,meat]

#Enemies
rat=enemy("Rat",1)
spider=enemy("Spider",2)
wolf=enemy("Wolf",3)
mugger=enemy("Mugger",4)
goblin=enemy("Goblin",5)
wizard=enemy("Wizard",6)
wraith=enemy("Wraith",7)
dragon=enemy("Dragon",8)
demon=enemy("Demon",9)
evilitself=enemy("Evil Itself",10)
listOfMobs=[rat,spider,wolf,mugger,goblin,wizard,wraith,dragon,demon,evilitself]

listOfChance=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2,2,1]

def fight():
    currentmob=random.choice(listOfMobs)
    lcd.message(currentmob)
    #print (currentmob)
    time.sleep(1)
    if player.hp>currentmob.damage:

        player.hp=player.hp-currentmob.damage
        player.br=player.br+1
        player.gp=player.gp+1
        print("*You emerge victorious!*")
    else:
        player.hp=player.hp-currentmob.damage
    print()

def shop():
    prompt=input("Welcome to the shop! Would you like to buy something? >")
    if prompt==("yes") or prompt==("Yes"):
        if len(player.inv)==1:
            print("*You empty your bag of the",player.inv[0]+"...*")
        del player.inv[:]
        chosenitem=random.choice(listOfHeals)
        player.inv.append(chosenitem)
        player.gp=player.gp-chosenitem.cost
        time.sleep(1)
        print ("*You purchase some",chosenitem.name,"and put it in your bag*")
    elif prompt==("No") or prompt ==("no"):
        print ("Maybe next time!")
        time.sleep(1)
    else:
        print("Sorry, can't hear ya! Come back another time!")
        time.sleep(1)
    print()


def eat():
    if len(player.inv)==0:
        print ("You have no food, what are you doing? >")
        time.sleep(1)
        print()
    print("*You eat the food in your bag...*")
    food=player.inv[0]
    player.hp=player.hp+food.heal
    if player.hp>100:
        player.hp=100
    del player.inv [:]
    time.sleep(1)
    print("Munch..")
    time.sleep(0.5)
    print("Munch..")
    time.sleep(0.5)
    print("Munch...")
    time.sleep(1)
    print("There! Much Better! Onwards!")
    print()
    time.sleep(1)

def sleep():
    print("Welcome to the Inn! Have a rest!")
    time.sleep(2)
    print("*You rest your eyes and sleep*")
    player.hp=player.hp+30
    time.sleep(1.5)
    print("...")
    time.sleep(2)
    print("*You awaken feeling refreshed, and continue on your journey.")
    print()

def stats():
    lcd.clear()
    if len(player.inv)==0:
        #print (str(player.hp)+"/100 "+str(player.gp)+"gp\nBag:Nothing")
        lcd.message(str(player.hp)+"/100 "+str(player.gp)+"gp\nBag:"+"Nothing")
    else:
        lcd.message(str(player.hp)+"/100 "+str(player.gp)+"gp\nBag:"+str(player.inv[0].name))
        #print (str(player.hp)+"/100 "+str(player.gp)+"gp\nBag:"+str(player.inv[0].name))
    print()

def die():
    time.sleep(0.5)
    print(".")
    time.sleep(0.8)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("Oh dear...")
    time.sleep(1.5)
    print("...you are dead.")
    time.sleep(2)
    print("FINAL BATTLE RANKING:",str(player.br)+"!")
    time.sleep(1)
    if (player.br>=50):
        print ("You are truly an accomplished warrior.")
    elif(player.br<=25):
        print ("You have a long way to go, my friend.")
    else:
        print ("Not too shabby.")

def main():
    print("~~~Your quest begins!~~~")
    time.sleep(3)
    print()

    while(player.hp>0):
        stats()
        turn=random.choice(listOfChance)
        if (turn==1):
            sleep()
        elif (turn==2):
            shop()
        choice=input("Would you like to continue on, or eat first? >")
        if choice==("eat") or choice==("Eat") or choice==("eat first") or choice==("Eat first"):
            eat()
        elif choice==("continue on") or choice==("continue") or choice==("Continue") or choice==("Continue on"):
            time.sleep(1)
        fight()
    die()
    time.sleep(5)
    input(">>>Press enter to quit.")
    lcd.clear()


main()
