#define characters and their attributes (health, attack power, etc.)

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

class Player(Fighter):
    def __init__(self, name, health, attack_power):
        super().__init__(name, health, attack_power)