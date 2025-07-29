# OBJECT ORIENTED PROGRAMMING

* OOPS - Object Oriented Programming Structure is a programming paradigm based on the concepts of objects, which can contain data and code.
* OOPS has benefits that include:
  * Scalability
  * Efficiency
  * Reusability

## Object

* An object is an identiafiable entity with some characteristics and behaviour.

## Class

* Collection of objects that share common characteristics and behavior.

## Example

* Dog.py

```py
class Dog:
    
    legs: int = 4
    ears: int = 2
    breed: str = "Goldendoodle"
    age: int = 5
    color: str = 'Yellow'
```

* Main.py

```py
from Dog import *

dog = Dog()

dog.legs
dog.ears
dog.breed
dog.age
dog.color
```

* With the `Class` in place, to create multiple `Dog` related files can be created by creating an object of Class Dog and invoking attributes of Dog defined in class.

## Pillars of OOPS

* Encapsulation
* Abstraction
* Inheritance
* Polymorphism

### Constructors 

### Default/Empty Constructors

* Pass

  ```py
  def __init__():
    pass
  ```

### no Argument Constructors

*

  ```py
  def __init__():
    print("No arguement constrcutor in Action!")
  ```

### Parameter Constructors

*

  ```py
   def __init__(self, type_of_enemy, health_points, attack_damage):
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
  ```

## Encapsulation

* Why use Encapsulation?
  - It helps to keep the related fields and methods together.
  - It makes our code cleaner and easier to read.
  - Provides more flexibility to our code.
  - It provides more reusability with our code.

* Declaring Private attributes in Class :

```py
# Definition in Enemy.py where Class is defined
def __init__(self, type_of_enemy, health_points, attack_damage):
        self.__type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage

def get_type_of_enemy(self):
        return self.__type_of_enemy

# Definition in main.py that creates the Object enemy=Enemy()
print(f'I am a {enemy.__type_of_enemy} and has health points of {enemy.health_points}. I can inflict a damage of {enemy.attack_damage}')

## Error 
## AttributeError: 'Enemy' object has no attribute '__type_of_enemy'
```

* To resolve this we add a getter function()

```py
    def get_type_of_enemy(self):
        return self.__type_of_enemy
```

* The getter function helps to retrieve the value of the Private Variable.
* [Online Reference](https://pythonbasics.org/getter-and-setter/)

```py
enemy = Enemy('Zombie', 30, 3)
print(f'I am a {enemy.get_type_of_enemy()} and has health points of {enemy.health_points}. I can inflict a damage of {enemy.attack_damage}')

## Output
## I am a Zombie and has health points of 30. I can inflict a damage of 3
```
