class Bot:
    def __init__(self, name, age, energy, shield):
        self.name = name
        self.age = age
        self.energy = energy
        self.shield = shield

    def returninfo(self):
        return(self.name)
        return(self.age)
        return(self.energy)
        return(self.shield)

    def printinfo(self):
        full_energy = 10
        full_shield = 10
        print("Name:",self.name)
        print("Age:", self.age)
        print("Energy Level: "+self.energy*"▮"+(full_energy-self.energy)*"▯")
        print("Shield Level: "+self.shield*"▮"+(full_shield-self.shield)*"▯")        

b1=Bot("bop",2,7,9)

b1.printinfo()