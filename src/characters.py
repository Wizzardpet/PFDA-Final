#define characters and their attributes (health, attack power, etc.)

import images




class Fighter():
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    def is_alive(self):
        return self.health > 0
    
class Zombie(Fighter):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def move_towards_player(self):
        print(f"{self.name} shambles towards the player!")
    
    def attack_player(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")

    
class Player(Fighter):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)

    def move_forward(self):
        print(f"{self.name} moves forward!")

    def move_backwards(self):
        print(f"{self.name} moves backwards!")

    def jump(self):
        print(f"{self.name} jumps!")

    def attack_zombie(self, other):
        other.health -= self.attack_power
        print(f"{self.name} attacks {other.name} for {self.attack_power} damage!")
