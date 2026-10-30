
from domain.character import Character
from domain.classes import Mage, Warrior


if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)

    # joker = Character("Joker", 200, 10)
    # batman = Character("Batman", 200, 20)

    # joker.take_damage(50)
    # print(joker.describe())

    david = Mage("David")
    goliath = Warrior("Goliath")

    goliath.attack(david)
    david.special_ability(goliath)

