from domain.character import Character
from domain.classes import Snipper, Commando


def run_special_round(attacker: Character, defender: Character) -> None:
    """Works for ANY Character subclass — this is polymorphism in action."""
    attacker.special_ability(defender)


def total_party_damage(party, target):
    party.attack(target)