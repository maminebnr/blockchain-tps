from ecdsa import SigningKey, SECP256k1, util

# Paire de clés
sk = SigningKey.generate(curve=SECP256k1)
vk = sk.get_verifying_key()

message = "Amine envoie 2 BTC à Ahmed"
message_modifie = "Amine envoie 2 BTC à Ahmed"

print("Message           :", message)
print("Message modifié   :", message_modifie)

# Signature déterministe (même message -> même signature) au format DER
signature = sk.sign_deterministic(
    message.encode(),
    sigencode=util.sigencode_der
)
print("\nSignature (DER hex):", signature.hex())

# Vérification sur le message original (⚠️ sigdecode côté verify)
valide_original = vk.verify(
    signature,
    message.encode(),
    sigdecode=util.sigdecode_der
)
print("Signature valide (original) ?", valide_original)

# Vérification sur le message modifié
try:
    valide_modifie = vk.verify(
        signature,
        message_modifie.encode(),
        sigdecode=util.sigdecode_der
    )
    print("Signature valide (modifié) ?", valide_modifie)
except Exception:
    print("Signature valide (modifié) ? False — message changé → signature invalide")
