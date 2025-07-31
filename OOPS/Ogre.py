import random
from Enemy import *

class Ogre(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Ogre', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        return print(f'I am a {super().get_type_of_enemy()}. Waves hands frantically...')
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.2
        if did_special_attack_work:
            self.health_points += 4
            print('Ogre regenerated health by 4HP!')