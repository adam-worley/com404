class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def display_name(self):
        x = len(self.name)
        print((x+2)*"-")
        print("|"+self.name+"|")
        print((x+2)*"-")
    
    def display_age(self):
        print("Age:")
        print(3*" "+2*"_"+str(self.age)+2*"_")
        print("  "+"|"+5*" "+"|")

    def display_energy(self):
        full_energy = 10
        print("Energy Level: "+self.energy*"▮"+(full_energy-self.energy)*"▯")

    def display_shield(self):
        full_shield = 10
        print("Shield Level: "+self.shield*"▮"+(full_shield-self.shield)*"▯")
    
    def display_summary(self):
        full_energy = 10
        full_shield = 10
        print("Name:",self.name)
        print("Age:", self.age)
        print("Energy Level: "+self.energy*"▮"+(full_energy-self.energy)*"▯")
        print("Shield Level: "+self.shield*"▮"+(full_shield-self.shield)*"▯")

    def __str__(self):
        print(self.name)
        print(self.age)
        print(self.energy)
        print(self.shield)


b1 = Bot("Beep", 1, 8, 9)

b1.display_summary()
print()
b1.__str__()
