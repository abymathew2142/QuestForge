
class Character:
    def __init__(self, name: str, health: int, attack_power: int):
        self.name = name
        self._health = health
        self.attack_power = attack_power
        self.__max_health = health


    @property
    def health(self) -> int:
        return self._health

    # @health.setter
    # def health(self, value: int) -> None:
    #     if value < 0:
    #         raise ValueError("Health cannot be negative")
    #     self._health = value
   
    @property
    def is_alive(self) -> bool:
        return self._health > 0

    def take_damage(self, damageAmount: int) -> None:
        if damageAmount < 0:
          raise ValueError("Health cannot be negative")
        self._health = max(0, self._health - damageAmount)


    def describe(self) -> str:
        return f"{self.name} has {self._health} HP and {self.attack_power} attack power"

    def attack(self, target: 'Character') -> None:
        if not self.is_alive:
            return
        target.take_damage(self.attack_power) 
        print(f"{self.name} attacks {target.name} for {self.attack_power} damage")

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError(f"Healing amount cannot be negative. No healing applied to {self.name}.")
        self._health =  min(self.__max_health, self._health + amount)
        print(f"{self.name} heals for {amount} HP, current health is now {self._health} HP")    