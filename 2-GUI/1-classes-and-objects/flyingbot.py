from superbot import SuperBot

class FlyingBot(SuperBot):
    def __init__(self, name, age, energy, shield, super_power_level,hover):
        super().__init__(name, age, energy, shield, super_power_level)
        self.hover = hover

    def display_summary_fly(self):
        full_energy = 10
        full_shield = 10
        print("Name:",self.name)
        print("Age:", self.age)
        print("Energy Level: "+self.energy*"▮"+(full_energy-self.energy)*"▯")
        print("Shield Level: "+self.shield*"▮"+(full_shield-self.shield)*"▯")
        print("Super Power Level:",self.super_power_level)
        print("hover Height:",self.hover)
