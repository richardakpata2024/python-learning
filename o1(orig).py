from o1_ import Data
class Data2(Data):
    def __init__(self,x,y,z):
        super().__init__(x,y,z)
        self.a=self.x

a1= Data2(2,4,6)
print(a1.a)
        
