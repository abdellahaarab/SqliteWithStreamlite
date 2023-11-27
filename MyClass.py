
class MyClass():
    name = ""
    poids = 0
    def __init__(self, name, poids) -> None:
        self.name = name
        self.poids = poids
        
    def afficher(self) -> None:
        return f"Nom : {self.name} - Poids : {self.poids}"