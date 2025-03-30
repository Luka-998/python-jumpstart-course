
# ChatGPT provided exercise done mostly by myself, I used ChatGPT propts to give me hints and to provide me with a guide how to start thinking when im stuck.
'''
 Create a Character class with the following attributes:

    name (string)

    health (integer, default: 100)

    attack_power (integer, default: 10)

    Add methods to the Character class:

    attack(target): Reduces the target's health by self.attack_power.

    heal(amount): Increases the character's health by the given amount (but max 100).

    __str__(): Returns a string representation of the character.'''



"""Next Steps for Your Exercise:

    Enhance the Creature class:

        Add more functionality like different types of creatures with different behaviors (e.g., some creatures might be immune to magic, or have their own special abilities).

    Make use of the attack and heal methods:

        You can now start a simulation where characters attack each other, heal, and use mana to cast spells.

    Introduce more attributes:

        For example, you can add a "defense" attribute to creatures or characters that can reduce incoming damage.

    Introduce a battle system:

        A simple battle system where a Creature and a Wizard face off and the one who reaches 0 health first loses could be the next logical step.

    Add Error Handling and User Input:

        Allow users to input mana values and health, and ensure that inputs are within the expected range.

    Create a Main Loop for Interaction:

        Create a main loop where you can interact with your characters: choosing to heal, attack, or cast spells."""

class Character():
    def __init__(self,name,health,attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    def attack(self,target): # Looking forward in the code
        target.health -= self.attack_power
    def heal(self,amount):
        if amount > 0:
            self.health=min(100,self.health+amount) # By using min(100, self.health + amount) - >"Out of the two values: 100 (the maximum health) and the result of adding the healing amount to the current health, pick the smaller value."
    def __str__(self):
        return(f'Character {self.name}, health: {self.health}, attack_power: {self.attack_power}')
    
class Creature(): 
    def __init__(self,name,health,level,attack_power):
        self.name = name
        self.health = health 
        self.level = level 
        self.attack_power = attack_power
    # -- defining the methods for creature class, but with modification, stats will depend on the creature level
    def attack(self,target):
        target.health -= (self.attack_power + self.level)
    def rest(self):
        self.health += min(100, 15 + self.level)
    def __str__(self):
        return(f'Creature {self.name}, Health: {self.health}, Level: {self.level}, Attack Power: {self.attack_power}')
    
    # i will make subclass for 2 monsters, that will inherit from the 'Creature' class.

class Lizard(Creature):
    def __init__(self, name, health, level, attack_power):
        super().__init__(name, health, level, attack_power)
        self.venom_spit = self.attack_power ** 2  
        
    def poison(self, target): 
        target.health -= self.venom_spit  
        self.health *= 0.9  # Reduces lizard's health by 10% when poison is used
class Turtle(Creature):
    def __init__(self, name, health, level, attack_power, shield=1):
        super().__init__(name, health, level, attack_power)
        self.shield = shield

    def magic_immunity(self, target):
        if self.shield == 1:
            self.health += 10  # Can exceed 100
        else:
            for _ in range(4):
                target.venom_spit = 0

class Wizard(Character):
    def __init__(self,name,health,level,attack_power,mana):
        super().__init__(name,health,attack_power) # when using super() method , self should be removed because it's passing self by itself calling
    def cast_spell(self,target):
        if isinstance(target,Turtle):
            target.heatlth -= 5
        else:
            target.health -= min(100,(target.health%10)*(self.mana/10))
    def mana_regen(self):
        self.mana*=.2
        self.mana = min(100,self.mana*1.2) # this ensures that max mana does not goes over 100 points
    def __str__(self):
        return (f'Wizard {self.name}, Health: {self.health}, Level: {self.level}, Attack Power: {self.attack_power} and Mana Points: {self.mana}')



### IMPORTANT

# - instances and classes should can not be compared,this was my huge mistake! If Creature == 'Turtle' ... it will lead to unexpected behavioura

def battle(player,enemy):
    turn = 0
    while player.health >0 and enemy.health > 0:
        if turn%2 ==0:
            #Player's turn:
            action=input('Choose action: 1) Attack, 2)Heal ')
            if action==1:
                player.attack(enemy)
            elif action==2:
                player.heal(10)
        else:
            #enemy's turn
            enemy.attack(player)
        print(player)
        print(enemy)
        turn+=1
        if player.health <=0:
            print(f"Player {player.name} has been defeated")
        else:
            print(f"{enemy.name} has been defeated!")

# Create characters and monsters
character1 = Character('Luka', 90, 99)
character2 = Character('Enemy', 25, 25)

# Create monsters
monster = Lizard("Lizard", 100, 5, 15)
monster_2 = Turtle("Turtle", 120, 5, 10)

# Simulate battle
battle(character1, monster)

