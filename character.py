#   Michael Cooper

class Character():

    def __init__(self):
        self.Name = "undefined"
        self.Class = "undefined"
        self.Stats = [0, 0, 0, 0, 0, 0]
        self.Money = [0, 0, 0, 0] #pp, gp, sp, cp
        self.MaxHP = "0"
        self.HP = "0"
        self.Skills = ["undefined"]


    def printAll(self):
        print(vars(self))

    def setName(self, newName):
        self.Name = newName

    def setClass(self, newClass):
        self.Class = newClass

    def setStats(self, newStats):
        self.Stats = newStats

    def setMoney(self, newMoney):
        self.Money = newMoney

    def setMaxHP(self, newMaxHP):
        self.MaxHP = newMaxHP

    def setHP(self, newHP):
        self.HP = newHP

    def setSkills(self, newSkills):
        self.Skills = newSkills

if __name__ == "__main__":
    char = Character()
    char.setStats([1, 2, 3, 4, 5, 6])
    char.printAll()