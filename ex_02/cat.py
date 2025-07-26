#Modification du constructeur
class Cat:
    def __init__(self, name=None):
        self.name=name
        if name: #name!=None
            print(f"Meow {self.name} !")
        else:
            print("Meow")