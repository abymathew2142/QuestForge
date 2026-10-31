from domain.character import Character

class Snipper(Character):
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=10)

    def special_ability(self, target: Character):
        bonus = int(self.attack_power * 2)
        target.take_damage(bonus)
        print(f"{self.name} uses bonus {bonus} damage the target {target.name}")


class Commando(Character):
    
    def __init__(self, name: str):
        super().__init__(name, health=100, attack_power=10)
        self.skillamount = 50

    def special_ability(self, target: Character):
        cost = 20
        if self.skillamount < cost:
            print(f"{self.name} don't have enough skillamount for using this weapon")
            return
        self.skillamount -= cost
        new_attack_power = self.attack_power * 3 
        target.take_damage(new_attack_power)
        print(f"{self.name} used a special weapon on target {target.name} with power {new_attack_power}")