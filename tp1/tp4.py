import json

# On réutilise le pseudo-hash de l'Ex1 pour le lien entre blocs
def pseudo_hash_hex8(texte):
    total = 0
    for i, c in enumerate(texte):
        code = ord(c)
        total = (total * 31 + code * (i + 1)) & 0xFFFFFFFF
    return f"{total:08x}"

class Bloc:
    def __init__(self, index, data, previous_hash="00000000"):
        self.index = index
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculer_hash()

    def calculer_hash(self):
        contenu = json.dumps({
            "index": self.index,
            "data": self.data,
            "previous_hash": self.previous_hash
        }, sort_keys=True, ensure_ascii=False)
        return pseudo_hash_hex8(contenu)

    def __repr__(self):
        return f"Bloc(index={self.index}, hash={self.hash}, prev={self.previous_hash})"

# Chaîne de 3 blocs
b1 = Bloc(1, "Bloc de genèse")
b2 = Bloc(2, "Transaction: Amine -> Ahmed", b1.hash)
b3 = Bloc(3, "Transaction: Ahmed -> Karim", b2.hash)
blockchain = [b1, b2, b3]

def verifier_blockchain(bc):
    # Vérifie liens prev/hash + recalcul du hash courant
    for i in range(1, len(bc)):
        if bc[i].previous_hash != bc[i-1].hash:
            return False
        if bc[i].hash != bc[i].calculer_hash():
            return False
    return True

print("Chaîne initiale :", blockchain)
print("Valide au début ?", verifier_blockchain(blockchain))

# Modification d'un bloc intermédiaire (attaque)
b2.data = "Transaction: Amine -> Samir"
print("\nAprès modification b2.data :")
print("Valide maintenant ?", verifier_blockchain(blockchain))
