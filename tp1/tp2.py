from ecdsa import SigningKey, SECP256k1

sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()

x=vk.to_string()[32:]
y=vk.to_string()[:32]
prefix='02' if int.from_bytes(y,'big') % 2 == 0 else '03'
print('address',prefix + x.hex())

print("Clé privée :", sk.to_string().hex(),sk.to_string())
print("Clé publique :", vk.to_string().hex(),vk.to_string())
