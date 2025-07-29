from Enemy import *

enemy = Enemy('Zombie', 30, 3)

print(f'I am a {enemy.get_type_of_enemy()} and has health points of {enemy.health_points}. I can inflict a damage of {enemy.attack_damage}')
enemy.talk()
enemy.walk_forward()
enemy.attack()