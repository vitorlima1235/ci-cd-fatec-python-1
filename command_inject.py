import os

def executar_comando_vulneravel(filename):
    # ❌ VULNERÁVEL: Execução de comando com input do usuário
    os.system(f"cat {filename}")  # CodeQL vai detectar aqui!
    # Atacante pode fazer: filename = "arquivo.txt; rm -rf /"
"""
# Como corrigir:
import subprocess

def executar_comando_seguro(filename):
    # ✅ SEGURO: Usar subprocess com lista de argumentos
    subprocess.run(["cat", filename], check=True)
"""