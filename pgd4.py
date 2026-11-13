class Time:
    def __init__(self,hour,minute,second):
        self.hour=hour
        self.minute=minute
        self.second=second

    def __add__(self,other):
        sec = self.second + other.second
        minu=self.minute+other.minute+sec // 60
        hr=self.hour+other.hour+minu // 60
        return Time(hr % 24,minu % 60,sec  % 60)

    def display(self):
        print(f"{self.hour:02d}:{self.minute:02d}:{self.second:02d}")

t1=Time(10,40,30)
t2=Time(2,50,45)
t3=t1+t2
t3.display()