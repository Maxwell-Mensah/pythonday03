class Cat:
    def __init__(self, name=None, age=None ):
        self.name=name
        self.age=age
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
    
    
    #méthode focntionnant en fonction du type de l'argument pris en paramètre
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