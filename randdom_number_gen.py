import random

def gerar_token_vulneravel():
    # ❌ VULNERÁVEL: random não é criptograficamente seguro
    return random.randint(1000, 9999)
"""
# Como corrigir:
import secrets

def gerar_token_seguro():
    # ✅ SEGURO: Usar secrets para dados sensíveis
    return secrets.token_hex(16)
"""