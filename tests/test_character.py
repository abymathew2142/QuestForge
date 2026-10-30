import sys
import unittest
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from domain.character import Character


class CharacterTest(unittest.TestCase):
    def test_healing_cannot_exceed_max_health(self):
        max_health = 100
        hero = Character("Aria", max_health, 15)

        hero.take_damage(40) 
        hero.heal(1000)

        self.assertEqual(hero.health, max_health)

    def test_heal_not_negative(self):
        hero = Character("Aria", 100, 15)

        hero.take_damage(20)
        hero.heal(10)

        self.assertEqual(hero.health, 90)  # Health should remain unchanged

if __name__ == "__main__":
    unittest.main()
