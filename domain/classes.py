from domain.character import Character

class Warrior(Character):
    def __init__(self, name: str):
        super().__init__(name, health=150, attack_power=20)

    def special_ability(self, target: Character):
        bonus = int(self.attack_power * 1.5)
        target.take_damage(bonus)
        print(f"{self.name} uses bonus {bonus} damage the target {target.name}")


class Mage(Character):
    
    def __init__(self, name: str):
        super().__init__(name, health=300, attack_power=25)
        self.balance = 50

    def special_ability(self, target: Character):
        cost = 20
        if self.balance < cost:
            print(f"{self.name} don't have enough balance for using this weapon")
            return
        self.balance -= cost
        new_attack_power = self.attack_power * 2 
        target.take_damage(new_attack_power)
        print(f"{self.name} used a special weapon on target {target.name} with power {new_attack_power} ----- {target.describe()}")