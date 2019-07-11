#   Michael Cooper

class Character():

    #based on class:
    #
    #   max hp
    #   hit die
    #   start wealth
    #   start inventory
    #   features
    #   saving throws

    #based on level:
    #
    #   proficiency bonus

    #based on stats
    #
    #   modifiers
    #   max hp
    #

    #based on race:
    #
    #   speed
    #   traits

    #need to generate:
    #
    #   Name
    #   Gender
    #   Age
    #   Weight
    #   Height
    #   Eye Color
    #   Skin Color
    #   Hair Color
    #   Level
    #   Class
    #   Race
    #   Background
    #   Alignment
    #   Skills
    #

    def __init__(self):
        self.Name = "undefined"
        self.Level = 1
        self.Class = "undefined"
        self.Class = "undefined"
        self.Stats = [0, 0, 0, 0, 0, 0]
        self.Money = [0, 0, 0, 0] #pp, gp, sp, cp
        self.MaxHP = 0
        self.HP = 0
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