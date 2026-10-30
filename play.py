
from domain.character import Character


if __name__ == "__main__":
    hero = Character("Aria", 100, 15)
    goblin = Character("Goblin", 30, 5)

    joker = Character("Joker", 200, 10)
    batman = Character("Batman", 200, 20)

    print(hero.describe())
    print(goblin.describe())
    print(joker.describe())
    print(batman.describe())

    hero.attack(goblin)
    print(goblin.describe())

    goblin.heal(10)
    goblin.describe()


    joker.attack(batman)
    print(batman.describe())
    batman.attack(joker)
    print(joker.describe())