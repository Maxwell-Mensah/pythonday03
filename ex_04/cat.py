class Cat:
    def __init__(self, age=None, name=None ):
        self.name=name
        self.age=age #ajout de l'attribut age a la class Cat
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
    
    #création d'une méthode pour avoir l'attribut age d'un objet existant
    def get_age(self):
        return self.age
    
    #création d'une méthode permettant de modifier l'attribut age d'un objet
    def set_age(self, new_age):
        self.age=new_age
    
    #méthode pemettant de connaître le statut d'un objet en fonction de son attribut age
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
            
        

