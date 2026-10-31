
from domain.character import Character
from domain.classes import Snipper, Commando
from domain.battle import run_special_round


if __name__ == "__main__":
    soldiers = [Snipper("Snipper Soldier"), Commando("Commando Soldier")]
    enemy = Character("Enemy", 100, 10)

    for member in soldiers:
        run_special_round(member, enemy)
        print(f"{enemy.name} health after {member.name} attack is : {enemy.health}")