#   Michael Cooper

class Character():

    def __init__(self):
        self.Name = "undefined"
        self.Class = "undefined"
        self.Stats = [0, 0, 0, 0, 0, 0]

    def setName(self, Name):
        self.Name = Name

    def setStats(self, newStats):
        self.Stats = newStats

if __name__ == "__main__":
    char = Character()
    print(char.Name)
    char.setStats([1, 2, 3, 4, 5, 6])
    print(char.Stats)