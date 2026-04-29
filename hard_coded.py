# ❌ VULNERÁVEL: Credenciais no código
DATABASE_PASSWORD = "senha123"
API_KEY = "sk-1234567890abcdef"
"""
# Como corrigir:
import os
from dotenv import load_dotenv

# ✅ SEGURO: Usar variáveis de ambiente
load_dotenv()
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')
API_KEY = os.getenv('API_KEY')
"""