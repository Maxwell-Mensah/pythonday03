
class Cat:
    def __init__(self, name=None):
        self.name=name
        if name:
            print(f"Meow {self.name} !")
        else:
            print("Meow")
    #Création de la methode __del__ pour supprimer un objet        
    def __del__(self):
        if self.name:
            print(f"Bye {self.name} !")
        else:
            print("Bye !")
    #création d'une méthode pour avoir l'attribut name d'un objet existant
    def get_name(self):
        return(self.name)

