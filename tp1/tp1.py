def pseudo_hash(texte):
    total = hex(sum(ord(c) for c in texte))
    return total % 1_000_000  # reste sur 6 chiffres

def pseudo_hash_hex8(texte):
    total = 0
    for i, c in enumerate(texte):
        code = ord(c)
        total = (total * 31 + code * (i + 1)) & 0xFFFFFFFF
    return f"{total:08x}"

mots = ["hello world", "blockchain", "bitcoin"]
for mot in mots:
    print(f"{mot} -> {pseudo_hash(mot)}")

print("\nEffet avalanche simplifié :")
a, b = "blockchain", "blockchaim"
print(f"{a} -> {pseudo_hash(a)}")
print(f"{b} -> {pseudo_hash(b)}")
