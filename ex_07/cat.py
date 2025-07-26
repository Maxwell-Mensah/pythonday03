class Cat:
    def __init__(self, name=None, age=None, energy=100 ):
        self.name=name
        self.age=age
        self.energy=energy
        if name:
            print(f"Meow {self.name} !")
        else:
            print("Meow")
            
    def __del__(self):
        if self.name:
            print(f"Bye {self.name} !")
        else:
            print("Bye !")
    
    def get_name(self):
        return(self.name)
    
    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age=new_age
    
    def status(self):
        match self.age:
            case a if a==0:
                print("Unborn Cat")
            case a if a==1 or a==2:
                print("Kitten")
            case a if 3 <= a <= 10:
                print("Adult Cat")
            case a if 11 <= a <= 13:
                print("Old Cat")
            case _:
                print("Impossible Cat")
    
    def hello(self, exp=None):
        if type(exp)==str:
            if self.name:
                print(f"Hello {exp},  I'm {self.name}")
            else:
                print(f"Hello {exp}")
        elif type(exp)==int:
            if self.name:
                for i in range (exp):
                    print(f"Hello, I'm {self.name}")
            else:
                for i in range (exp):
                    print("Hello")
    
    def eat(self, food):
        if food.lower()== "fish":
            self.energy+=10
            if self.energy>=100:
                self.energy=100
            print("Yum!")
        elif food.lower()== "vegetable":
            self.energy-=10
            if self.energy<=0:
                self.energy=0
            print("Yuck!")
        else:
            print("I can't eat this")
            
    def get_energy(self):
        return self.energy
    
    def set_energy(self, new_energy):
        self.energy=new_energy

    def nap(self):
        if self.energy>=25:
            print("Zzz.....")
            self.energy-=9
        else:
            print("I'm too tired... I need to rest!")
            self.energy=50
