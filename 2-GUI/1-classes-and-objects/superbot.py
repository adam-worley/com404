from bot_Q2 import Bot

class SuperBot(Bot):
  def __init__(self, name, age, energy, shield, super_power_level):
    super().__init__(name, age, energy, shield)
    self.super_power_level = super_power_level

  def display_summary_super(self):
    full_energy = 10
    full_shield = 10
    print("Name:",self.name)
    print("Age:", self.age)
    print("Energy Level: "+self.energy*"▮"+(full_energy-self.energy)*"▯")
    print("Shield Level: "+self.shield*"▮"+(full_shield-self.shield)*"▯")
    print("Super Power Level:",self.super_power_level)
