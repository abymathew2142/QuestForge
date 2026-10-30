
class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def describe(self) -> str:
        return f"{self.name} has {self.health} HP and {self.attack_power} attack power"

    def attack(self, target: 'Character') -> None:
        target.health -= self.attack_power
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage")

    def heal(self, amount: int) -> None:
        self.health += amount
        print(f"{self.name} heals for {amount} HP, current health is now {self.health} HP")    