from Enemy import *
from Zombie import *
from Ogre import *
from Hero import *
from Weapon import *

def battle(e1: Enemy,e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print('---------------')
        e1.special_attack()
        e2.special_attack()
        print(f'I am a {e1.get_type_of_enemy()} and has health points of {e1.health_points}. I can inflict a damage of {e1.attack_damage}')
        print(f'I am a {e2.get_type_of_enemy()} and has health points of {e2.health_points}. I can inflict a damage of {e2.attack_damage}')
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    print('---------------')
    if e1.health_points > 0:
        print(f'{e1.get_type_of_enemy()} Wins!!!')
    else:
        print(f'{e2.get_type_of_enemy()} Wins!!!')

def hero_battle(hero: Hero, enemy: Enemy):
    
    while hero.health_points > 0 and enemy.health_points > 0:
        print('---------------')
        print(f'I am a Hero and has health points of {hero.health_points}. I can inflict a damage of {hero.attack_damage}')
        print(f'I am a {enemy.get_type_of_enemy()} and has health points of {enemy.health_points}. I can inflict a damage of {enemy.attack_damage}')

        enemy.special_attack()

        hero.attack()
        enemy.health_points -= hero.attack_damage
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        
    print('---------------')
    if hero.health_points > 0:
        print(f'Hero Wins!!!')
    else:
        print(f'{enemy.get_type_of_enemy()} Wins!!!')
        

zombie = Zombie(31, 3)
# ogre = Ogre(30,4)
# battle(zombie, ogre)
weapon = Weapon('Sword', 5)
hero = Hero(31, 3)

hero.weapon = weapon
hero.equip_weapon()

hero_battle(hero, zombie)


