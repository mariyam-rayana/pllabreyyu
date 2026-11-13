class rectangle:
   def __init__(self,l,b):
       self.l=l
       self.b=b
   def area(self):
       return self.l*self.b
   def perimeter(self):
       return 2*(self.l+self.b)

r1=rectangle(4,5)
r2=rectangle(3,6)

if r1.area()>r2.area():
    print("r1 has the larger area")
elif r1.area()<r2.area():
    print("r2 has the smaller area")
else:
    print("r1 and r2 have the same area")