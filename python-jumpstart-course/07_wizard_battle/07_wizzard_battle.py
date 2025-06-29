# Modified exercise where I additional attributes have been added, also more complex game logic.

print('-'*160)
print(f'{"Wizard_Game":-^160}')
print('-'*160)

class Character():
    def __init__(self, name, health, attack_power, mana):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.mana = mana

    def spell_cast(self, target):
        if self.health < target.health and self.health <= 5:
            target.health -= 48
        else:
            target.health -= 15
        target.health = max(0, target.health)
        self.health = max(0, self.health)

    def attack(self, target):
        target.health -= self.attack_power

class Gandolf(Character):
    def __init__(self, name, health, attack_power, mana, level):
        super().__init__(name, health, attack_power, mana)
        self.level = level

class Evil_Wizard(Character):
    def __init__(self, name, health, attack_power, mana, level):
        super().__init__(name, health, attack_power, mana)
        self.level = level

class Creature():
    def __init__(self, name, health, level, attack_power):
        self.name = name
        self.health = health
        self.level = level
        self.attack = attack_power

    def fight(self, target):
        if self.level > target.level:
            target.health = max(0, target.health - self.attack)
        else:
            print(f'You cannot attack a creature with a higher level! Your level: {self.level}, Creature level: {target.level}')

    def rest(self):
        self.health += self.health * 0.1

class Chimera(Creature):
    def __init__(self, name, health, level, attack, shock):
        super().__init__(name, health, level, attack)
        self.shock = shock

    def el_shock(self, target):
        if target.health <= (0.2 * self.health):
            target.health -= 50
        else:
            target.health -= 20

class Ogre(Creature):
    def __init__(self, name, health, level, attack, defense):
        super().__init__(name, health, level, attack)
        self.defense = defense

    def shield(self, target):
        if isinstance(target, Chimera):
            self.health = 120
            print(f"When fighting {target.name}, Ogres get more HP!")
        else:
            self.health += self.defense
            print(f'Ogre gets defense added into HP when not fighting Chimera')
            self.health = min(140, self.health)

class Murlock(Creature):
    def __init__(self, name, health, level, attack, leap):
        super().__init__(name, health, level, attack)
        self.leap = leap

    def regen(self, target):
        if self.health < target.health:
            self.health += 20  # should regenerate 1 health per second
        else:
             target.health -=20

# defining the battle mechanics
gandolf = Gandolf('Gandolf', 200, 26, 86, 9)
evil_wiz = Evil_Wizard('Evil Wizard', 48, 21, 85, 8)
chimera = Chimera('Dragonfly', 25, 5, 15, 70)
ogre_mage = Ogre('Ogre Mage', 85, 5, 15, 30)
murlock = Murlock('Slark', 20, 4, 30, 'leap')

print(f"The wizard {gandolf.name} with HP {gandolf.health}, attack power of {gandolf.attack_power} and level {gandolf.level} sees a {evil_wiz.name}, and Evil Wizard with HP, Attack, Level and Mana {evil_wiz.health,evil_wiz.attack_power,evil_wiz.level,evil_wiz.mana}\nDo you [a]ttack or [r]un away, [l]ook around? ")

user_input = input().casefold().strip()
if user_input == 'r':
    print(f'The wizard {gandolf.name} ran away!')
elif user_input == 'a':
    while gandolf.health > 0 and evil_wiz.health > 0:
        action = input("Attack (a) or Cast spell (s)? ").casefold().strip()
        if action == 'a':
            gandolf.attack(evil_wiz)
            print(f'Evil Wizard HP: {evil_wiz.health}')
        elif action == 's':
            gandolf.spell_cast(evil_wiz)
            print(f'Evil Wizard HP: {evil_wiz.health}')

        if evil_wiz.health <= 0:
            print(f"{evil_wiz.name} has been defeated!")
            break

        if gandolf.health <= 0:
            print(f"{gandolf.name} has been defeated!")
            break

    if gandolf.health > 0 and evil_wiz.health <= 0:
        print(f"Gandolf won the battle with {gandolf.health} HP")
elif user_input == 'l':
    print(f'Gandolf sees:\n* A level {chimera.level} {chimera.name}\n* A level {ogre_mage.level} {ogre_mage.name}\n* A level {murlock.level} {murlock.name}')
    while gandolf.health > 0:
        if chimera.health > 0:
            chimera.el_shock(gandolf)
        if ogre_mage.health > 0:
            ogre_mage.shield(gandolf)
        if murlock.health > 0:
            murlock.regen(gandolf)

        print(f'Gandolf HP: {gandolf.health}')

        if gandolf.health <= 0:
            print('Gandolf is defeated!')
            break

        if chimera.health > 0:
            gandolf.spell_cast(chimera)
        if ogre_mage.health > 0:
            gandolf.spell_cast(ogre_mage)
        if murlock.health > 0:
            gandolf.spell_cast(murlock)

        print(f'\nAfter Gandolf attacks:')
        print(f'{chimera.name} HP: {chimera.health}')
        print(f'{ogre_mage.name} HP: {ogre_mage.health}')
        print(f'{murlock.name} HP: {murlock.health}')

        if chimera.health <= 0 and ogre_mage.health <= 0 and murlock.health <= 0:
            print("\nGandolf has defeated all the creatures!")
            break