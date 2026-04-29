# =============================================================================
# EXEMPLO 5: WEAK CRYPTOGRAPHY (CWE-327) 🟠 MEDIUM
# =============================================================================
# O CodeQL detectará uso de algoritmos de criptografia fracos


import hashlib

def hash_senha_vulneravel(senha):
    # ❌ VULNERÁVEL: MD5 é considerado fraco
    return hashlib.md5(senha.encode()).hexdigest()
"""
# Como corrigir:
import bcrypt

def hash_senha_seguro(senha):
    # ✅ SEGURO: Usar bcrypt ou argon2
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt)
"""