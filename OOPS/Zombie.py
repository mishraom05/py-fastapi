from Enemy import *
import random

class Zombie(Enemy):
    
    def __init__(self, health_points, attack_damage):
        super().__init__(type_of_enemy='Zombie', health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        return print(f'I am a {super().get_type_of_enemy()}. Grumbling... Grumbling...')
    
    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.health_points += 2
            print('Zombie regenerated health by 2HP!')
