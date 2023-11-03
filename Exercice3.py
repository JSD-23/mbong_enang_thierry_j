class Exercice3:
    
    def __init__(self, capacite):
        # Implémenter la logique d'initialisation
        self.memoire = {}
        self.capacite = capacite
        self.ordre = []

    def get(self, cle):
        # Implémenter la logique de récupération
        if cle in self.memoire:
            self.ordre.append(cle)
            del(self.ordre[0])
            valeur = self.memoire.pop(cle)
            self.memoire[cle] = valeur
            return valeur
        else:
            return -1

    def put(self, cle, valeur):
        # Implémenter la logique d'insertion
        if cle in self.memoire:
            self.memoire.pop(cle)
        elif len(self.memoire) >= self.capacite:
            self.memoire.pop(self.ordre[0])
        self.memoire[cle] = valeur
    def free(self):
        # Implémenter la logique de libération
        self.memoire.clear()
# Teste de fonctionnement

cache = Exercice3(2)

cache.put(1,1)
cache.put(2,2)
print(cache.memoire)
print(cache.get(1))
cache.put(3,3)
print(cache.get(2))
cache.put(4,4)
print(cache.get(1))
print(cache.get(3))
print(cache.get(4))

