
from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)

    joker = Character("Joker", 200, 10)
    batman = Character("Batman", 200, 20)

    joker.take_damage(50)
    print(joker.describe())
