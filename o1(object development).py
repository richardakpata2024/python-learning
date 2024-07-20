
class Data:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def add(self):
        return self.x+self.y+self.z

o1= Data(2,4,6)
print(o1.add())
